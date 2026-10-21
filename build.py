"""Builds the download for the OS it runs on:
release/Maple-Classic-Exp-Overlay-v<version>.zip on Windows, and
release/Maple-Classic-Exp-Overlay-v<version>-mac.zip on a Mac.

It packs the program, Python and everything it needs into one folder with
"Maple Classic Exp Overlay.exe" (on a Mac: "Maple Classic Exp Overlay.app"),
adds Tesseract OCR (for reading map names), and zips it up for a GitHub release.

On a Mac it needs Tesseract and dylibbundler from Homebrew (brew install tesseract
dylibbundler): dylibbundler copies the libraries Tesseract needs into the app, so it runs
on Macs without Homebrew. The app is signed ad hoc (not by a registered developer).

Needs Python with the packages from requirements.txt plus PyInstaller, and Tesseract
installed (https://github.com/UB-Mannheim/tesseract/wiki):
    py -3 -m pip install -r requirements.txt pyinstaller
    py -3 build.py
Set TESSERACT_DIR if Tesseract isn't in C:\\Program Files\\Tesseract-OCR.

It also puts a copy to use right away in the project folder: "Maple Classic Exp Overlay.exe"
and the _internal folder it needs (Tesseract goes inside it). Only changed files are copied.

    py -3 build.py zip <folder>
zips an already built folder again (for example after its .exe was signed).

    py -3 build.py root
copies the last build to the project folder again (if the overlay was running and its
files couldn't be replaced).
"""
import filecmp
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAME = "Maple Classic Exp Overlay"                 # the folder and the .exe
ZIP_NAME = NAME.replace(" ", "-")                  # GitHub turns spaces in downloads into dots
VERSION = re.search(r'^VERSION = "([^"]+)"', (ROOT / "maple_exp.py").read_text(encoding="utf-8"), re.M)[1]
TESSERACT = Path(os.environ.get("TESSERACT_DIR", r"C:\Program Files\Tesseract-OCR"))
BUILD, RELEASE = ROOT / "build", ROOT / "release"
MAC = sys.platform == "darwin"

# Parts of the libraries that are never used, left out to make the download smaller:
# OpenCV's video player (the screen is read with mss, never from a video) and Pillow's
# AVIF support (only PNGs are made). Both are only loaded when they're used.
UNUSED = ["_internal/cv2/opencv_videoio_ffmpeg*.dll", "_internal/PIL/_avif*.pyd"]

READ_ME_FIRST = f"""{NAME} v{VERSION}  (beta)

1. Double-click "{NAME}.exe" to start it.
   If Windows says "Windows protected your PC", click "More info", then "Run anyway".
2. Start MapleStory and press Start in the overlay.

Keep this whole folder together: the .exe needs the files next to it.
The full guide is on the GitHub page you downloaded this from.
"""


READ_ME_FIRST_MAC = f"""{NAME} v{VERSION}  (beta), for Macs with Apple Silicon (M1 or newer), macOS 14 or newer

1. Drag "{NAME}" (the app) into your Applications folder, and open it from there.
   If macOS says it can't check the app for malware: click Done, then open System Settings >
   Privacy & Security, scroll down, and click "Open Anyway" next to {NAME}.
2. It asks to record your screen (that's how it reads the game): click Open System Settings,
   switch {NAME} on under Screen Recording, then open it again.
3. Start MapleStory (in CrossOver, Whisky, Parallels or a game stream) and press Start.

Hotkeys aren't available on a Mac yet: use the buttons.
The full guide is on the GitHub page you downloaded this from.
"""


def main():
    if MAC:
        return main_mac()
    if not (TESSERACT / "tesseract.exe").exists():
        sys.exit(f"Tesseract wasn't found in {TESSERACT}. Install it, or set TESSERACT_DIR.")
    shutil.rmtree(BUILD, ignore_errors=True)
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--windowed",
                    "--onedir", "--name", NAME, "--icon", str(ROOT / "assets" / "icon.ico"),
                    "--add-data", f"{ROOT / 'assets'};assets",
                    "--distpath", str(BUILD / "dist"), "--workpath", str(BUILD / "work"),
                    "--specpath", str(BUILD), str(ROOT / "maple_exp.py")], check=True)
    app = BUILD / "dist" / NAME

    # Tesseract: the program, its DLLs, and the English language data.
    tess = app / "tesseract"
    (tess / "tessdata").mkdir(parents=True)
    for f in TESSERACT.iterdir():
        if f.name.lower() == "tesseract.exe" or f.suffix.lower() == ".dll":
            shutil.copy2(f, tess)
    shutil.copy2(TESSERACT / "tessdata" / "eng.traineddata", tess / "tessdata")
    for folder in ("configs", "tessconfigs"):
        if (TESSERACT / "tessdata" / folder).is_dir():
            shutil.copytree(TESSERACT / "tessdata" / folder, tess / "tessdata" / folder)
    for notice in ("LICENSE", "LICENSE.txt", "doc/LICENSE", "doc/AUTHORS"):
        if (TESSERACT / notice).is_file():
            shutil.copy2(TESSERACT / notice, tess / f"{Path(notice).name}.txt")

    for pattern in UNUSED:
        for f in app.glob(pattern):
            print(f"Leaving out {f.relative_to(app)} ({f.stat().st_size / 1e6:.0f} MB, not used)")
            f.unlink()

    (app / "READ ME FIRST.txt").write_text(READ_ME_FIRST, encoding="utf-8")
    make_zip(app)
    copy_to_root(app)


def main_mac():
    tesseract = Path(os.environ.get("TESSERACT_BIN") or shutil.which("tesseract") or "/opt/homebrew/bin/tesseract")
    if not tesseract.is_file():
        sys.exit("Tesseract wasn't found. Install it (brew install tesseract), or set TESSERACT_BIN.")
    if not shutil.which("dylibbundler"):
        sys.exit("dylibbundler wasn't found. Install it: brew install dylibbundler")
    tesseract = tesseract.resolve()                      # (Homebrew's is a link into its Cellar)
    prefix = tesseract.parent.parent
    tessdata = Path(os.environ.get("TESSDATA_DIR") or prefix / "share" / "tessdata")
    if not (tessdata / "eng.traineddata").is_file():
        sys.exit(f"Tesseract's English data wasn't found in {tessdata}. Set TESSDATA_DIR.")
    shutil.rmtree(BUILD, ignore_errors=True)
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--windowed",
                    "--onedir", "--name", NAME, "--icon", str(ROOT / "assets" / "icon.ico"),
                    "--osx-bundle-identifier", "io.github.guddevbaddev.maple-classic-exp-overlay",
                    "--add-data", f"{ROOT / 'assets'}:assets",
                    "--distpath", str(BUILD / "dist"), "--workpath", str(BUILD / "work"),
                    "--specpath", str(BUILD), str(ROOT / "maple_exp.py")], check=True)
    app = BUILD / "dist" / f"{NAME}.app"
    contents = app / "Contents"

    # Tesseract and the libraries it needs go in Contents/Frameworks/tesseract (where the
    # overlay looks: next to its own files), its English data in Contents/Resources (macOS
    # wants only programs in Frameworks), with a link to it from next to the program.
    tess = contents / "Frameworks" / "tesseract"
    tess.mkdir(parents=True)
    shutil.copy2(tesseract, tess / "tesseract")
    (tess / "tesseract").chmod(0o755)
    subprocess.run(["dylibbundler", "--overwrite-files", "--bundle-deps", "--create-dir",
                    "--fix-file", str(tess / "tesseract"), "--dest-dir", str(tess / "libs"),
                    "--install-path", "@executable_path/libs/",
                    "--search-path", str(prefix / "lib"), "--search-path", "/opt/homebrew/lib"], check=True)
    data = contents / "Resources" / "tesseract" / "tessdata"
    data.mkdir(parents=True)
    shutil.copy2(tessdata / "eng.traineddata", data)
    for folder in ("configs", "tessconfigs"):
        if (tessdata / folder).is_dir():
            shutil.copytree(tessdata / folder, data / folder)
    (tess / "tessdata").symlink_to(Path("..") / ".." / "Resources" / "tesseract" / "tessdata")
    for notice in ("LICENSE", "COPYING", "AUTHORS"):
        if (prefix / notice).is_file():
            shutil.copy2(prefix / notice, data.parent / f"{notice}.txt")

    # Every program and library ad hoc signed again (copying and fixing them broke their
    # signatures; Apple Silicon Macs won't run unsigned code), then the whole app.
    for f in [tess / "tesseract", *sorted((tess / "libs").glob("*"))]:
        subprocess.run(["codesign", "--force", "--sign", "-", str(f)], check=True)
    subprocess.run(["codesign", "--force", "--deep", "--sign", "-", str(app)], check=True)
    check_mac_app(app)

    folder = RELEASE / "mac" / NAME
    shutil.rmtree(folder.parent, ignore_errors=True)
    folder.mkdir(parents=True)
    # ditto keeps the app as it is (links, signature); Python's zipfile wouldn't.
    subprocess.run(["ditto", str(app), str(folder / app.name)], check=True)
    (folder / "READ ME FIRST.txt").write_text(READ_ME_FIRST_MAC, encoding="utf-8")
    zip_path = RELEASE / f"{ZIP_NAME}-v{VERSION}-mac.zip"
    zip_path.unlink(missing_ok=True)
    subprocess.run(["ditto", "-c", "-k", "--sequesterRsrc", "--keepParent", str(folder), str(zip_path)], check=True)
    shutil.rmtree(folder.parent)
    print(f"\nDone: {zip_path} ({zip_path.stat().st_size / 1e6:.0f} MB)")


def check_mac_app(app):
    """The app is whole: its signature holds, and its Tesseract runs on its own (no library
    from Homebrew, and its English data found)."""
    subprocess.run(["codesign", "--verify", "--deep", "--strict", str(app)], check=True)
    tess = app / "Contents" / "Frameworks" / "tesseract"
    for f in [tess / "tesseract", *sorted((tess / "libs").glob("*"))]:
        links = subprocess.run(["otool", "-L", str(f)], capture_output=True, text=True, check=True).stdout
        outside = [line.split()[0] for line in links.splitlines()[1:]
                   if line.strip() and not line.split()[0].startswith(("@", "/usr/lib/", "/System/"))]
        if outside:
            sys.exit(f"{f.name} still uses libraries from outside the app: {outside}")
    env = {"PATH": "/usr/bin:/bin", "TESSDATA_PREFIX": str(tess / "tessdata")}
    langs = subprocess.run([str(tess / "tesseract"), "--list-langs"], capture_output=True, text=True, env=env)
    if "eng" not in langs.stdout.split():
        sys.exit(f"The app's Tesseract doesn't run, or has no English data: {langs.stdout} {langs.stderr}")
    print("Checked: the app's signature, and its own Tesseract (with English)")


def make_zip(app):
    """release/<name>-v<version>.zip, with everything in a "Maple Classic Exp Overlay" folder."""
    RELEASE.mkdir(exist_ok=True)
    zip_path = RELEASE / f"{ZIP_NAME}-v{VERSION}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(app.rglob("*")):
            z.write(f, Path(NAME) / f.relative_to(app))
    print(f"\nDone: {zip_path} ({zip_path.stat().st_size / 1e6:.0f} MB)")


def copy_to_root(app):
    """The built program in the project folder, ready to double-click: the .exe and _internal,
    with Tesseract inside _internal (the program looks there too). Only changed files are
    copied, and files the new build doesn't have any more are removed."""
    want = {ROOT / f"{NAME}.exe": app / f"{NAME}.exe"}
    for folder, into in ((app / "_internal", ROOT / "_internal"), (app / "tesseract", ROOT / "_internal" / "tesseract")):
        for f in folder.rglob("*"):
            if f.is_file():
                want[into / f.relative_to(folder)] = f
    changed = [dest for dest, src in want.items() if not dest.exists() or not filecmp.cmp(src, dest, shallow=False)]
    stale = [f for f in (ROOT / "_internal").rglob("*") if f.is_file() and f not in want] \
        if (ROOT / "_internal").exists() else []
    # A running overlay keeps its files locked: check first, so nothing is left half updated.
    for f in [d for d in changed if d.exists()] + stale:
        try:
            with open(f, "r+b"):
                pass
        except PermissionError:
            print(f"\nThe project folder's copy wasn't updated: {f.name} is in use. Close the overlay, "
                  "then run:  py -3 build.py root")
            return
    for f in stale:
        f.unlink()
    for dest in changed:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(want[dest], dest)
    print(f"Ready to use: {ROOT / (NAME + '.exe')} ({len(changed)} files updated, {len(stale)} removed)")


if __name__ == "__main__":
    if sys.argv[1:2] == ["zip"] and len(sys.argv) == 3:
        make_zip(Path(sys.argv[2]))
    elif sys.argv[1:] == ["root"]:
        copy_to_root(BUILD / "dist" / NAME)
    else:
        main()
