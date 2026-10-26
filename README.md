<h1><img src="docs/icon.png" width="40" align="top"> Maple Classic Exp Overlay (Mac)</h1>

**A free EXP tracker for MapleStory Classic World, built for Mac.** A small window sits next to the game and shows how fast you're leveling and making mesos.

This is a Mac-focused fork of [guddevbaddev/Maple-Classic-Exp-Overlay](https://github.com/guddevbaddev/Maple-Classic-Exp-Overlay), which is itself a fork of [beanguri/Maple-Classic-Exp-Overlay](https://github.com/beanguri/Maple-Classic-Exp-Overlay). It doesn't connect to the original best-maps website: it never shares your runs, and it has no **Best maps** button. The only time it goes online is the update check, which looks at this repository's releases.

**[Download the Mac app](../../releases/latest)** · [How to install](#how-to-install) · [What's different in this fork](#whats-different-in-this-fork)

> **This is a beta.** It works, but you might run into rough edges. I'm actively improving it, so check back for updates. If something doesn't work, please [tell me](../../issues)!

![The overlay next to MapleStory, while farming](docs/screenshot-game.jpg)

## What's different in this fork

This fork keeps the parent project's features (the Share card, crash logs, Save logs, PQ mode, the map log and the overlay itself) and adds:

- **Mac-only releases:** an Apple Silicon app for macOS 14 or newer, built and published by GitHub Actions.
- **Choose application:** if automatic window detection picks the wrong window, choose the MapleStory/CrossOver window from the **...** menu.
- **Mesos without opening the inventory:** mesos are counted from the game's pickup notifications, with the inventory total as a fallback.
- **EXP pickup notifications:** EXP from pickups is counted and reconciled with the EXP bar.
- **Stop button:** end a session and save it to the log immediately.
- **Menu placement:** the **...** menu opens beside the button, not under the overlay.
- **Automatic releases:** pushing a new `VERSION` to `main` builds and publishes the Mac release.

The downloads here are Mac-only. Windows builds live in the [upstream repositories](https://github.com/guddevbaddev/Maple-Classic-Exp-Overlay).

## What it shows

![The overlay up close, with its log open](docs/screenshot-main.png)

- **EXP per hour**, for your whole session and for the last 5 minutes
- **How long until your next level**, right under your EXP/hr (for example "Lv 31 in 36 min")
- **How much of a level you gained** in the last 5, 15 and 30 minutes and the last hour (under **Details**). Paused time doesn't count. Until you've tracked that long, it shows what you've gained so far ("2.40% so far").
- **Mesos per hour**, from the game's pickup notifications (no need to keep your inventory open) or your inventory total as a fallback
- **EXP from pickups**, counted as soon as the game shows it, so a pickup doesn't look like a missing gain
- **A log of every map you farm**: your EXP/hr and mesos/hr there, at which level and class, solo or in a party

You don't type anything in. It reads all of this from your game screen by itself.

## How to install

This fork releases the **Mac app** only. You need a Mac with Apple Silicon (M1 or newer) and macOS 14 (Sonoma) or newer, with MapleStory running through CrossOver, Whisky, Parallels or a game stream.

1. Go to the **[download page](../../releases/latest)**.
2. Under **Assets**, click the file ending in **-mac.zip** (for example `Maple-Classic-Exp-Overlay-v0.9.13-beta-mac.zip`). Don't click "Source code": that's for programmers.
3. Double-click the zip in your Downloads folder to unpack it, and drag **Maple Classic Exp Overlay** (the app) into your **Applications** folder.
4. Open it. macOS will say it can't check the app for malware, because it isn't from a registered Apple developer: click **Done**, then open **System Settings > Privacy & Security**, scroll down, and click **Open Anyway** next to Maple Classic Exp Overlay. You only need to do this once.
5. It asks for permission to record your screen (that's how it reads the game). Click **Open System Settings**, switch **Maple Classic Exp Overlay** on under **Screen Recording**, then open the app again.

On macOS 15 and later, macOS re-confirms screen recording about once a month, so that prompt can come back even though the toggle is on; click **Allow**. After an update, if it asks again and the toggle for the new version is off, switch it off and on. **Hotkeys aren't available in the Mac app yet**, so use the buttons. If automatic window detection picks the wrong window, use **...** > **Choose application** (see below).

## How to use it

1. **Start MapleStory.** Windowed, borderless or fullscreen all work, at any size.
2. **Open Maple Classic Exp Overlay.** It finds the game window by itself.
3. **Move the overlay so it doesn't cover these parts of the game:**
   - the minimap (top left)
   - the EXP bar (bottom)
   - the mesos at the bottom of your inventory (only needed if pickup notifications aren't showing)
   - the party list

   The overlay reads them from your screen, so it can't see through itself. If it's in the way, it tells you at the bottom of its window. It remembers where you put it.
4. **Press Start** and play normally. You only need to press it once:
   - It **pauses by itself** when you get no EXP for 15 seconds or leave the map, and carries on at your next EXP gain. Paused time doesn't count, so EXP/hr only covers your farming.
   - On a different map, the numbers start from zero for that map.
   - Press **Stop** to end the session and save it to the log immediately.
5. **Mesos are tracked automatically** from the game's pickup notifications. If they don't show up (some setups don't show pickup text), keep your inventory open on any tab as a fallback.
6. **Wrong window?** If it reads another application, open **...** > **Choose application** and pick the MapleStory/CrossOver window.

Within a few seconds it shows your level and how much EXP you have. The per-hour numbers fill in once you've gained a little EXP.

| Button | What it does |
|---|---|
| **Start / Pause / Resume** | Starts tracking. **Pause** stops it until you press **Resume**. |
| **Stop** | Ends the session and saves it to the log right away. |
| **Reset** | Starts a new session from zero, and looks for the minimap, inventory and party list again (handy after moving them around) |
| **Don't log** | Keeps the current run out of the log, for example while you're testing a map or waiting for your party. Everything is still shown on screen. It turns itself off when you leave the map or stop getting EXP, so your next run is logged as usual. |
| **Select area** | Lets you drag a box around the EXP numbers, if it ever can't find them. The button then turns into **Follow game**, which goes back to finding them by itself. |
| **View capture** | Shows exactly what it read from your screen |
| **PQ mode** | For party quests (in the **...** menu). See [PQ mode](#pq-mode) below. |
| **...** | Menu: **Choose application** (Mac), **Select area**, **View capture**, **PQ mode**. |
| **Share** | Makes a picture of your session (EXP/hr, mesos/hr, the map) and copies it, to paste into Discord. See [Sharing your session](#sharing-your-session) below. |
| **⚙** | Settings |
| **>** | Opens the log |
| **Compact** | A much smaller window with just EXP/hr, when you'll level, the last 5 minutes, mesos/hr and Start/Pause. The button then says **Full**, to bring everything back. Double-clicking the big number does the same. |

### PQ mode

A party quest goes through several maps, and a stage can go minutes without EXP until it's cleared. Normally the overlay pauses when you change maps (and starts that map's numbers from zero), and after 15 seconds without EXP. Both would spoil a PQ, so turn on **PQ mode** in the **...** menu (it then says **PQ mode: on**) before you start:

- **Changing maps doesn't reset anything.** EXP/hr, mesos/hr and the time carry on through the whole quest.
- **It only pauses by itself after 10 minutes without EXP**, so the EXP you get when a stage is cleared counts.
- **The log puts the PQ on one line called "Party Quest"**, whatever maps it went through. Right-click it and choose **Rename map** to call it, say, "Kerning PQ".
- The status at the top says **PQ** while it's tracking.

It turns itself off when you close the overlay, so your normal farming isn't affected if you forget. To turn it off sooner, choose **PQ mode: on** in the menu again.

### Sharing your session

Click **Share** (bottom right) to show off how your farming is going. It makes a picture card in the overlay's gold-and-dark look with:

- your **EXP per hour**, big and glowing, with the trend line of your session
- your **mesos per hour** (from pickup notifications, or your inventory total) and how long you've been tracking
- the **map** you're on, your **level**, **class** and **party size** (in PQ mode it says "Party Quest")
- how much of a level you're getting per hour

It's **copied straight away**: click in Discord's message box and press **Cmd+V**, then Enter. It also opens in a window, where **Copy again** copies it again and **Show file** shows the saved picture (`share-card.png` in the data folder), in case you'd rather drag it in. The card never shows your character's name, and nothing is sent anywhere by the overlay: you choose where to paste it.

## Hotkeys

**Hotkeys aren't available in the Mac app yet.** Use the buttons. (The upstream Windows build has hotkeys; this fork's releases are Mac-only.)

## The log

Click **>** at the top right of the overlay to open the log. It's the table on the right in the close-up picture above.

- **After 5 minutes of non-stop farming**, it adds a line for that map, your level and your party size.
- **Every 5 more minutes** it updates that line, so the numbers get more accurate the longer you farm.
- **Time** shows how long a line is based on. It grows by 5 minutes with each update.
- **Class** is read from the status bar (never your character's name). Different classes get separate lines.
- **15-minute runs:** under the log it also counts toward 15 minutes of non-stop farming on one map with the same party size ("15-min run: 7 of 15 min"). A level-up doesn't stop it; a break, a new map or a new party size starts it over. Finished runs are saved separately in your log file.
- **Greyed-out lines** were changed outside the overlay. Every line the overlay writes is sealed, so a line edited or added by hand is easy to spot. Deleting a line, or renaming a map in the overlay, is fine.
- **Taking a break restarts the 5-minute timer.** A break means no EXP for 15 seconds (you can change this in ⚙). Changing maps or party size restarts it too.
- **Don't want a run logged?** Press **Don't log**. It switches back on its own when that run ends.
- **Solo** means just you. **4ppl** means a party of 4.
- **?** under Mesos/hr means no mesos were seen yet: no pickup notifications, and no inventory total.
- **Right-click a line** to:
  - **Copy line**, to paste it into Discord or anywhere else
  - **Rename map**, if it read the name wrong (it remembers the fix for next time)
  - **Delete entry**
- **Playing in a party?** A map's party sizes on one day share one line (e.g. **4–5ppl ▸**), with the numbers over all that time. Click it to see a line for each party size.
- **Notes:** click a line and write whatever you like about it in the box under the log: the party, the pots, the loot, why you left. A ✎ in the **Note** column marks the lines that have one. Notes save as you type, and **they only ever stay on your Mac**, in your log file, and are never sent anywhere. Renaming a map, updating the overlay, or farming more on a line keeps its note. Deleting a line deletes its note too, and asks you first.
- **Can't see a whole column?** Drag the lines between the column titles to make columns narrower or wider. While the log is open, you can also make the window bigger by dragging its edge. It remembers both.

## Settings (⚙)

- **Pause tracking after no EXP for...** How long you can go without EXP before it pauses by itself. This also restarts the log's 5-minute timer. The default is 15 seconds.
- **Window transparency.** Makes the overlay see-through, up to 40%. (More and it could fade out of sight, with Settings in it.)
- **Size.** Makes the text and the whole window smaller or bigger, from 60% to 200%. The smallest text stops at a readable size, so it never gets too small to read. It's sized for each screen, so a window moved to a screen with different scaling (like a 5K and a 1440p screen) looks the same size on both.
- **Hotkeys (Windows only).** Turn them on or off, and change them. They aren't available in the Mac app yet.
- **Always on top of other windows.** Keeps the overlay above the game. It's on by default.
- **Check for updates when it starts.** On by default. See [Updates](#updates).
- **Open data folder.** Opens the folder where your log and settings are saved.
- **Check for updates.** Checks right now.
- **Report a bug.** See below.

## How accurate is it?

It double-checks everything it reads before counting it:

- **EXP:** the number and the % have to agree with each other, and with the EXP your level needs.
- **Pickup EXP:** credited when the notification appears, then reconciled with the EXP bar so it isn't counted twice.
- **Mesos:** pickup notifications are counted once; an inventory total has to show up in several readings in a row.
- **Sudden jumps:** an EXP jump or a level-up has to be confirmed before it counts. A mesos amount that looks like an extra or missing digit is ignored.
- **Dying:** the EXP you lose isn't taken off your EXP/hr. It says how much you lost, then carries on from there.
- **When in doubt, it waits.** If it can't read something clearly, it skips it instead of guessing.

Every version is tested against thousands of misread numbers, and against real screenshots of the game pasted over many different backgrounds at different window sizes.

## Something not working?

**Did it close by itself?** Open it again: it says it closed unexpectedly, and offers to save what happened. You can also do it any time in ⚙ with **Save logs**: it makes one zip (in the `logs` folder of the data folder) with `overlay.log` (what it was doing), `errors.log` and `crash.log` (where it was when it closed). Send that zip, or attach it to a bug report.

**Click View capture first.** It shows exactly what the overlay read, with a box around every digit:

![View capture](docs/screenshot-capture.png)

| Problem | Try this |
|---|---|
| macOS says it can't check the app for malware | See step 4 in [How to install](#how-to-install): click **Done**, then **Open Anyway** in System Settings. |
| "MapleStory window not found" | Start the game first. If it's minimized, bring it back up. |
| It reads the wrong application | Open **...** > **Choose application** and pick the MapleStory/CrossOver window. |
| "Can't find the EXP bar" | Make sure nothing covers the EXP bar at the bottom of the game, including the overlay. If the game window is very small, make it bigger. |
| View capture shows the wrong part of the screen | If the button says **Follow game**, click it, or use **...** > **Choose application**. |
| Mesos says "waiting for mesos" | Keep playing: mesos are counted from pickup notifications. If your setup doesn't show them, open your inventory on any tab as a fallback, and make sure its mesos aren't hidden. In small game windows the chat bar can cover them, so drag the inventory up a bit. |
| The log says "Map not read yet" | Make sure the minimap is open at the top left of the game, and the overlay isn't covering it. |
| The map name is wrong | Right-click the log line and choose **Rename map**. |
| "This window is covering..." | Drag the overlay to another spot. |
| Numbers stopped updating, or anything else | Please report it (see below). |

**To report a bug,** click **Report a bug** in ⚙ (or **Something's wrong? Report a bug** in View capture):
1. Your browser opens a bug report on GitHub, already filled in with your version and what the overlay was reading. Nothing personal is included, and nothing is sent until you click Submit.
2. A folder opens with **bug-report.png** (what the overlay read: the EXP bar, mesos, class and map name) and **bug-report.txt** (how it's doing: your screen and game window size, what it found, what it last said, and any errors). Drag both into the report. Neither has your character name or your computer user name. It also asks if you want to save a small picture of the whole game window: that one can show chat and names, so it's saved only if you say yes, and you choose whether to attach it.
3. Write a sentence about what went wrong, and click **Submit**. (You need a free GitHub account.)

## Is it safe? Is it allowed?

- **It only looks at your screen, like a screen recorder.** It never touches the game's files or memory, and never presses keys or clicks for you.
- **It only goes online for one thing:** asking GitHub whether there's a newer version when it starts. Nothing about who you are is sent, and it can be turned off in ⚙. See [Privacy](#privacy).
- **macOS may warn about it the first time.** Gatekeeper asks you to allow the app because it isn't notarized by Apple; see [How to install](#how-to-install). All of the code is public right here, so anyone can check what it does.
- **It isn't made by or affiliated with Nexon.** Like any third-party tool, you use it at your own risk.

## Privacy

- **Your log, your notes and your settings stay on your Mac**, in `~/Library/Application Support/MapleEXP`. (The upstream Windows build uses `%APPDATA%\MapleEXP`.) Notes are part of your log file: they are never sent anywhere, and the overlay's tests check that.
- **A copy of your log is kept for each day** (the last 7 days), in the `backups` folder next to it, so if anything ever goes wrong there's a recent one. To go back to one, close the overlay and copy it over `exp_log.json`.
- **The update check** (on by default, can be turned off in ⚙) asks GitHub for the newest version and what's new in it. Nothing about you is sent.
- **Nothing from your log is ever sent anywhere**, including your 15-minute runs. There's no sharing and no website.
- **Bug reports** only go to GitHub if you click Submit there yourself.

## Where the download comes from

Downloads on the [Releases page](../../releases) are built by GitHub from the code in this repository ([Build workflow](.github/workflows/build.yml)), not on anyone's own computer. Each build:

- installs exact package files, each checked against its SHA-256 ([requirements-build-mac.txt](requirements-build-mac.txt)),
- runs all the tests,
- signs the app with the project's own certificate when one is configured (so macOS keeps Screen Recording permission across updates),
- records a signed **attestation**: which workflow built which file, from which commit,
- puts the zip's **SHA-256** on the release page (`SHA256SUMS.txt`).

**Check your download** with the free [GitHub CLI](https://cli.github.com):

```
gh attestation verify "the zip you downloaded.zip" --repo Kewee123/Maple-Classic-Exp-Overlay-mac
```

It tells you whether that exact file was built here, and from which commit. Or compare the file's SHA-256 with `SHA256SUMS.txt` on its release page (`shasum -a 256 "the zip you downloaded.zip"` on a Mac).

The same zip is also kept on the page of the build that made it (Actions, the run, the file at the bottom; you need a GitHub account to download it). Build runs since October 17 keep it exactly as it is, so the SHA-256 GitHub shows there is the zip's own, the same as on the release page.

**This fork's releases** start at v0.9.13-beta. It is a Mac-focused fork of [guddevbaddev/Maple-Classic-Exp-Overlay](https://github.com/guddevbaddev/Maple-Classic-Exp-Overlay), whose releases start at v0.9.10-beta. That fork is based on [beanguri/Maple-Classic-Exp-Overlay](https://github.com/beanguri/Maple-Classic-Exp-Overlay), whose releases go up to v0.9.9-beta and whose repository also has the best-maps website code this fork doesn't include or use.

### Code signing policy

The Mac app is **signed locally (ad hoc, or with the project's own certificate when configured) and not notarized by Apple**, so macOS asks you to allow it the first time (see [How to install](#how-to-install)). The Build workflow builds it from this repository; only builds made by that workflow are attested.

- Committers and reviewers: [Kewee123](https://github.com/Kewee123)
- Approvers: [Kewee123](https://github.com/Kewee123)
- Privacy policy: see [Privacy](#privacy) above. In short: your log and notes stay on your Mac, and the overlay only contacts another system to check GitHub for a newer version (can be turned off in Settings).

## Updates

This is a beta, and I'm still adding features and fixing things.

**New name:** since v0.9.3 it's called Maple Classic Exp Overlay. It used to be Maple EXP/hr. Your log and settings carry over.

**When a new version is out,** the overlay tells you when you start it, and shows what's new. Click **Get the update** to open the download page, or **Not now** / **Skip this version** if you'd rather wait.

**To update:** click **Update now** in the window that says a new version is out (from 0.9.13-beta on). It downloads the new version from this page, checks its SHA-256, and restarts the overlay as the new version; nothing is installed if the check fails. Screen Recording permission survives updates when the release is signed with the same identity, but macOS may still re-confirm it periodically. If macOS asks and the toggle is off, switch it off and on for the new version. Or, as before, download the newest zip from the [download page](../../releases/latest) and use it instead of the old folder. Your log, notes and settings stay, because they're saved separately (⚙ → **Open data folder** shows where).

**To remove it:** drag the app to the Trash. To also delete your log and settings, delete the folder that **Open data folder** opens.

See [CHANGELOG.md](CHANGELOG.md) for what changed in each version.

---

<details>
<summary><b>For developers</b></summary>

**Run from source (Mac).** You need Python 3.10 or newer and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for map names:

```
brew install tesseract
python3 -m pip install -r requirements.txt
python3 maple_exp.py
```

The first time, allow your Terminal (or Python) in **System Settings > Privacy & Security > Screen Recording**, then start it again. The window is found by "MapleStory" in its title; if it isn't, use **...** > **Choose application** or **Select area**. Hotkeys aren't available on macOS yet.

If automatic window detection chooses the wrong source, open the **...** menu and choose **Choose application**, then select the MapleStory/CrossOver window. The selected window is scanned for both the EXP bar and mesos pickup notifications, so mesos/hr works without opening the inventory. The inventory total remains a fallback when the game is not showing pickup text.

Everything that differs between Windows and macOS (finding the game window, screen scaling, hotkeys, the one-copy-at-a-time lock) is in `platforms/`: one `Platform` interface in `base.py`, one implementation per OS, and `create_platform()` picks the one for the OS it's on.

**Build the Mac download** (puts `Maple-Classic-Exp-Overlay-v<version>-mac.zip` in `release/`):

```
brew install tesseract dylibbundler
python3 -m pip install --require-hashes -r requirements-build-mac.txt
python3 build.py
```

It includes its own copy of Tesseract and the libraries it needs.

**Keep Screen Recording permission across updates (Mac).** macOS ties the permission to the app's code signature. An ad-hoc build gets a new identity every time, so macOS treats every update as a new app and asks again. Sign every build with the same certificate instead — a free self-signed one is enough:

1. In **Keychain Access** → **Certificate Assistant** → **Create a Certificate…**, use **Identity Type: Self Signed Root** and **Certificate Type: Code Signing**. Name it, for example, `Maple Exp Signing`.
2. Select it under **My Certificates**, then export it with its private key as a `.p12`.
3. Build with `MAC_SIGN_IDENTITY` set to its name:

   ```
   MAC_SIGN_IDENTITY="Maple Exp Signing" python3 build.py
   ```

   The first time, macOS may ask to let `codesign` use the key; click **Always Allow**.

4. For GitHub releases, add these **Actions secrets** to the repository:
   - `MACOS_CERT_P12`: the `.p12`, base64-encoded (`base64 -i cert.p12 | pbcopy`)
   - `MACOS_CERT_PASSWORD`: its export password
   - `MACOS_CERT_IDENTITY` (optional): the certificate's name, if the workflow can't find it

   The Build workflow imports the certificate and signs the app with it. Without these secrets it still builds, ad hoc.

Keep the private key secret, and use the same identity for local and GitHub builds if you want them to share the permission. The certificate doesn't need to be trusted by macOS (Gatekeeper still asks the first time), and the app remains unnotarized. macOS 15 and later still re-confirm Screen Recording periodically; that prompt is macOS's own and can't be disabled by the app.

**Tests use their own data folder:** with `MAPLE_EXP_DATA` set, the overlay keeps its log and settings there, away from your real ones.

**Run the tests:**

```
python3 tests/test_logic.py
python3 tests/test_screen.py
python3 tests/test_ui.py     # opens the real window for a few seconds (the notes box)
```

GitHub runs the logic tests on every push ([Tests workflow](.github/workflows/tests.yml)). The [Build workflow](.github/workflows/build.yml) runs all the tests, builds and attests the Mac zip, then publishes it. **To release a new version:** change `VERSION` in `maple_exp.py`, add its section to `CHANGELOG.md`, and push both to `main` in the same commit. The workflow tags that commit `v` + `VERSION` and publishes the release, with the `CHANGELOG.md` section as its notes. Pushing a version tag does the same. To publish the current version without bumping it, run **Build** > **Run workflow** on `main` with **release** ticked. Releases are only ever made those ways.

**How it reads the screen:**
- It finds the MapleStory window (on a Mac, through CrossOver, Whisky, Parallels or a game stream), then the EXP numbers (like `12,345 [12.34%]`) in the status bar.
- Each digit is resized to a standard size and compared against saved examples of the game's font in `assets/`.
- A reading only counts if the EXP and % agree with how much EXP that level needs, so misreads are ignored.
- Mesos are read from pickup notifications, with the inventory total as a fallback. The inventory box is found by its outline, which also works while the inventory is see-through.
- The party size is the number of HP bars in the party list.
- Map names are read with Tesseract.
- Settings, the log and `errors.log` are saved in `~/Library/Application Support/MapleEXP` (from its old name, Maple EXP/hr, so updates keep them).

**Windows builds** are in the [upstream repository](https://github.com/guddevbaddev/Maple-Classic-Exp-Overlay); this fork's Build workflow only builds the Mac app.

</details>

## Credits

- Based on [Maple Classic Exp Overlay](https://github.com/beanguri/Maple-Classic-Exp-Overlay) by [beanguri](https://github.com/beanguri) (MIT License), with the Windows/Mac work, Share card, crash logs, Save logs and other improvements from [guddevbaddev's fork](https://github.com/guddevbaddev/Maple-Classic-Exp-Overlay).
- This Mac-focused fork adds the Mac app releases, **Choose application**, mesos pickup tracking, the **Stop** button, the **...** menu placement fix, and automatic GitHub releases.
- The Classic World EXP table is from [meowdb](https://meowdb.com/msclassic/guides/exp-table-level-1-to-100). It's used to work out your level.
- Map names are read with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (Apache 2.0 license), which is included in the download.
- The typeface is [Manrope](https://github.com/googlefonts/manrope) (SIL Open Font License, included as `assets/fonts/OFL.txt`).

## License

[MIT](LICENSE): free to use, change and share.
