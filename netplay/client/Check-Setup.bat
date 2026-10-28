@echo off
rem FE9 co-op Netplay client: validation checklist only (changes nothing, starts nothing).
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\client.ps1" -Check %*
pause
