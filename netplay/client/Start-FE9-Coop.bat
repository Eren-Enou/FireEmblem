@echo off
rem FE9 co-op Netplay client: checks the setup, then starts Dolphin with this folder's settings.
rem You can drag Dolphin.exe onto this file the first time.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\client.ps1" %*
if errorlevel 1 pause
