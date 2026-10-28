FIRE EMBLEM: PATH OF RADIANCE - TWO-PLAYER CO-OP (NETPLAY CLIENT, PLAYER 2)
Package @@PACKAGE_VERSION@@ - codes @@CODES@@ - code fingerprint @@FINGERPRINT@@

This is an experimental fan modification. Player 1 (the host) plays Ike's blue army; you, Player 2,
play the yellow army: the characters the host's ownership table gives to Player 2 (in this test
build: Oscar, Boyd, Shinon and Gatrie), plus the game's own yellow partner units (e.g. Lethe and
Mordecai in Chapter 9). Turns go blue phase -> yellow phase -> enemy phase. You can only move your
units in the yellow phase; the host can only move theirs in the blue phase.

This ZIP contains NO game, NO game files and NO save data. You need your own:
  * Dolphin @@DOLPHIN_VERSION@@ for Windows (exactly this version, see step 1)
  * Fire Emblem: Path of Radiance, USA, game ID GFEE01, revision 0, as a disc image you dumped
    yourself (.iso, .rvz, .ciso, .gcz or .gcm)

The package uses its own private Dolphin user folder (the "User" folder next to this README).
Your normal Dolphin settings, memory cards and save states are never read or changed.


1. INSTALL DOLPHIN @@DOLPHIN_VERSION@@
   Download Dolphin @@DOLPHIN_VERSION@@ for Windows x64 from https://dolphin-emu.org/download/
   (release versions are listed there; the host will tell you if the version changed) and extract it,
   e.g. to C:\Games\Dolphin-x64. If Dolphin offers an update later, say no until the host updates too:
   Netplay only works when both players run the same version.

2. EXTRACT THIS ZIP
   Right-click the ZIP > Extract All. Put the extracted folder anywhere, e.g. next to Dolphin-x64.
   Do not run anything from inside the ZIP window.

3. FIRST START
   Double-click Start-FE9-Coop.bat (or drag Dolphin.exe onto it). It will:
     * find Dolphin.exe (or ask you to pick it) and check its version
     * ask for the folder that contains your game (once)
     * run the checklist below, then start Dolphin with this package's settings
   If Windows shows "Windows protected your PC", choose More info > Run anyway (it is a plain text
   script; open tools\client.ps1 in Notepad to read it).

4. CHECK THE GAME (once)
   In Dolphin, right-click Fire Emblem: Path of Radiance > Properties > Info: Game ID GFEE01,
   Revision 0. Optional: Properties > Verify > Verify Integrity. The host's copy gives
   SHA-1 @@GAME_SHA1@@ (a different value is not necessarily a problem; Netplay's own check in
   step 6 is what counts).

5. JOIN THE HOST
   In Dolphin: Tools > Start NetPlay... > Connect tab.
     Connection Type: Traversal Server (already selected)
     Host Code:       the room code the host sends you (8 characters, e.g. a1b2c3d4)
   Click Connect. You should see the host and yourself in the player list.
   No port forwarding is needed for the Traversal Server; if it cannot connect, see TROUBLESHOOTING.

6. BEFORE THE HOST PRESSES START (both players check)
   * Both players show the same Dolphin version in the NetPlay window.
   * Game: Fire Emblem: Path of Radiance (GFEE01). The host clicks "SHA1 Digest" > Current game:
     the NetPlay window must report that the hashes match.
   * Pad mapping (host: Assign Controller Ports): GC Port 1 = host, GC Port 2 = you, Ports 3 and 4
     empty. Your own controller 1 is what plays GC Port 2.
   * Data (host's menu): "Load Host's Save Data Only" (nothing is written to anyone's card) and
     "Sync AR/Gecko Codes" ticked. The host's codes are sent to you; your copy is only a check.
   * Tell the host your code fingerprint from the checklist window: @@FINGERPRINT@@

7. CONTROLS (your controller 1 = keyboard; change it in Controllers > Port 1 > Configure)
     Stick / cursor   Arrow keys          A (confirm)   X
     B (cancel)       Z                   X button      C
     Y button         S                   Z button      D    (map menu, e.g. End)
     Start            Enter               L / R         Q / W
     C-stick          I J K L             D-pad         T F G H
   Click into the game window before pressing keys (keys only reach the focused window).
   A USB gamepad works too: Controllers > Port 1 > Standard Controller > Configure, Device = your pad.

8. VALIDATION CHECKLIST
   Check-Setup.bat prints it again at any time without changing anything:
     [OK] Dolphin @@DOLPHIN_VERSION@@     [OK] game folder found     [OK] cheats enabled
     [OK] controller 1 configured         [OK] traversal server       [OK] code fingerprint
   All lines must say [OK]. Anything marked [FIX] says what to do.


FIRST TEST SESSION (about 30 minutes; the host leads)
   The host starts from their own memory card; nothing you play is saved on either side.
   1. Host: Title > Restart Chapter > the chapter the host names. Skip scenes with Start.
   2. Blue phase: only the host's keys move units. Press X on one of your yellow units: nothing.
   3. Yellow phase (banner "Partner Phase"): move each of your units, attack an enemy once and
      watch the EXP bar fill, then open the map menu (D) > End. The host's keys do nothing now.
   4. Enemy phase: watch; enemies may attack either army.
   5. Play at least 3 full turns. Both of you compare: same turn number, same units, same HP and
      the same EXP for the unit that fought (Status screen).
   6. At the end, the host stops the game. Then, if you both agree, test a disconnect: start again,
      and in the yellow phase close your NetPlay window. Tell the host what each screen did.
   Report: Dolphin version, chapter and turn reached, any "desync" message in the chat (with the
   turn and the last action), and anything that looked wrong.


TROUBLESHOOTING
   * "Version mismatch" / cannot join: both players need exactly Dolphin @@DOLPHIN_VERSION@@.
   * "Failed to connect" with Traversal: try again with a new code; if it keeps failing, the host can
     host with Direct Connection on port 2626 (router port forwarding) and you connect by IP.
   * "Game not found" or a digest mismatch: wrong region or revision, or Dolphin does not list the
     game. Re-run Start-FE9-Coop.bat and choose the right folder.
   * The yellow phase is played by the computer: codes did not sync. The host checks "Sync AR/Gecko
     Codes" and that cheats are enabled on the host.
   * Desync (the two screens differ): stop, note the turn and action, and start the chapter again.
     Loading save states is disabled in Netplay.
   * Keys do nothing: click into the game window first.

FILES
   Start-FE9-Coop.bat    setup checks + start Dolphin with this folder's settings
   Check-Setup.bat       the validation checklist only
   tools\client.ps1      the script both .bat files run (plain text)
   User\                 the private Dolphin user folder (settings, controller, codes)
   MANIFEST.txt          versions, code fingerprint and a SHA-256 for every file in this package
