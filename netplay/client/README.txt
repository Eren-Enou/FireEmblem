FIRE EMBLEM: PATH OF RADIANCE - TWO-PLAYER CO-OP (NETPLAY CLIENT, PLAYER 2)
Package @@PACKAGE_VERSION@@ - codes @@CODES@@ - code fingerprint @@FINGERPRINT@@

This is an experimental fan modification. Player 1 (the host) plays Ike's blue army; you, Player 2,
play the yellow army: the characters the host's ownership table gives to Player 2 (in this test
build: Oscar, Boyd, Shinon and Gatrie), plus the game's own yellow partner units (e.g. Lethe and
Mordecai in Chapter 9). Turns go blue phase -> yellow phase -> enemy phase. You can only move your
units in the yellow phase; the host can only move theirs in the blue phase.

This ZIP contains NO game, NO Dolphin, NO save data and NO programs or scripts - only settings
files and this README. You need:
  * Dolphin @@DOLPHIN_VERSION@@ for Windows, already installed (exactly this version: Netplay refuses
    to connect two different versions; check in Dolphin with Help > About)
  * Fire Emblem: Path of Radiance, USA, game ID GFEE01, revision 0, as a disc image you dumped
    yourself (.iso, .rvz, .ciso, .gcz or .gcm)

The "User" folder in this ZIP is a separate Dolphin settings folder for the co-op game. Starting
Dolphin with it (step 2) leaves your normal Dolphin settings, memory cards and save states alone.


1. EXTRACT THIS ZIP
   Right-click the ZIP > Extract All, e.g. to C:\Games\FE9-Coop-Client.
   Do not use the files from inside the ZIP window.

2. START DOLPHIN WITH THE CO-OP SETTINGS FOLDER
   Make a shortcut once: right-click Dolphin.exe > Show more options > Create shortcut. Right-click
   the new shortcut > Properties, and add the User folder to the end of "Target", e.g.:
     "C:\Games\Dolphin-x64\Dolphin.exe" --user "C:\Games\FE9-Coop-Client\User"
   (use your own two paths; keep both pairs of quotes). Click OK, rename the shortcut to
   "FE9 Co-op", and always start the co-op game from it.
   Check: the game list is empty the first time, and Help > About shows @@DOLPHIN_VERSION@@.

3. ADD YOUR GAME (once, in the Dolphin started from the shortcut)
   Config > Paths > Add... > choose the folder that contains your disc image. The game appears in
   the list. Right-click it > Properties > Info: Game ID GFEE01, Revision 0.
   Optional: Properties > Verify > Verify Integrity. The host's copy gives
   SHA-1 @@GAME_SHA1@@ (the host's checksum in step 5 is the check that counts).

4. CHECK THE CODES (optional; the host's codes are what actually runs)
   Open PowerShell (Start menu > type PowerShell) and run, with your own path:
     Get-FileHash "C:\Games\FE9-Coop-Client\User\GameSettings\GFEE01.ini"
   The Hash must be (check before changing anything in Gecko Codes, which rewrites the file):
     @@CODES_SHA256@@
   In Dolphin, right-click the game > Properties > Gecko Codes: "EXP-16 ..." and "COOP-P5 ..." are
   ticked, and Config > General > Enable Cheats is ticked.

5. JOIN THE HOST
   Tools > Start NetPlay... > Connect tab.
     Connection Type: Traversal Server (already selected)
     Host Code:       the room code the host sends you (8 characters)
   Click Connect. You should see the host and yourself in the player list.
   No port forwarding is needed for the Traversal Server; if it cannot connect, see TROUBLESHOOTING.

6. BEFORE THE HOST PRESSES START (both players check)
   [ ] Both players show Revision @@DOLPHIN_VERSION@@ in the NetPlay player list.
   [ ] Game: Fire Emblem: Path of Radiance (GFEE01). The host clicks Checksum > Current game:
       the NetPlay window must say "The hashes match!".
   [ ] Pad mapping (player list "Mapping" column; host: Assign Controller Ports): GC Port 1 = host,
       GC Port 2 = you, Ports 3 and 4 empty. Your own controller 1 is what plays GC Port 2.
   [ ] Data (host's menu): "Load Host's Save Data Only" (nothing is written to anyone's card) and
       "Sync AR/Gecko Codes" ticked.
   [ ] Code fingerprint for this package: @@FINGERPRINT@@ (the host compares it with theirs).
   [ ] Your step 4 hash matched (or you skipped it).

7. CONTROLS (your controller 1 = keyboard; change it in Controllers > Port 1 > Configure)
     Stick / cursor   Arrow keys          A (confirm)   X
     B (cancel)       Z                   X button      C
     Y button         S                   Z button      D    (map menu, e.g. End)
     Start            Enter               L / R         Q / W
     C-stick          I J K L             D-pad         T F G H
   Click into the game window before pressing keys (keys only reach the focused window).
   A USB gamepad works too: Controllers > Port 1 > Standard Controller > Configure, Device = your pad.


FIRST TEST SESSION (about 30 minutes; the host leads)
   The host starts from their own memory card; nothing you play is saved on either side.
   1. Host: Title > Restart Chapter > the chapter the host names. Skip scenes with Start.
   2. Blue phase: only the host's keys move units. Press X and the arrows: nothing happens.
   3. Yellow phase: move each of your units, attack an enemy once and watch the EXP bar fill, then
      open the map menu (D) > End. The host's keys do nothing now.
   4. Enemy phase: watch; enemies may attack either army.
   5. Play at least 3 full turns. Both of you compare: same turn number, same units, same HP and
      the same EXP for the unit that fought (Status screen).
   6. In turn 3's yellow phase, both press Shift+F1 (saves a state; allowed in Netplay) and send
      the file User\StateSaves\GFEE01.s01 to the host.
   7. At the end, the host stops the game. Then, if you both agree, test a disconnect: start again,
      and in the yellow phase close your NetPlay window. Tell the host what each screen did.
   Report: Dolphin version, chapter and turn reached, any "desync" message in the chat (with the
   turn and the last action), and anything that looked wrong.


TROUBLESHOOTING
   * Version mismatch / cannot join: both players need exactly Dolphin @@DOLPHIN_VERSION@@.
   * "Failed to connect" with Traversal: try again with a new code; if it keeps failing, the host can
     host with Direct Connection on port 2626 (router port forwarding) and you connect by IP
     (Connection Type: Direct Connection).
   * "Game not found" or a checksum mismatch: wrong region or revision, or the game folder is not
     added in THIS Dolphin (step 3; the co-op shortcut has its own game list).
   * The yellow phase is played by the computer: codes did not sync. The host checks "Sync AR/Gecko
     Codes" and that cheats are enabled on the host.
   * Settings look like your normal Dolphin: you started Dolphin without the shortcut from step 2.
   * Desync (the two screens differ): stop, note the turn and action, and start the chapter again.
     Loading save states is disabled in Netplay.
   * Keys do nothing: click into the game window first.
   * Slow game, stretched audio, both PCs at the same low FPS (e.g. 40): the host raises Buffer in
     the NetPlay window (it can be changed while playing). Buffer 18 kept 58-60 FPS at 23-33 ms
     ping in the first internet test; the delay it adds hardly matters in this game.

FILES
   README.txt                      this file
   User\Config\Dolphin.ini         co-op settings: cheats on, controller 1, Traversal Server, nickname
   User\Config\GCPadNew.ini        controller 1 keyboard layout
   User\GameSettings\GFEE01.ini    the co-op code definitions (@@CODES@@ enabled)
   User\GC\USA\Card A\             empty memory card folder (Netplay uses the host's save data)
   MANIFEST.txt                    versions, code fingerprint and a SHA-256 for every file
