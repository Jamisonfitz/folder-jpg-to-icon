@echo off
:: This batch script is designed to clear the Windows icon cache.
:: It achieves this by terminating the explorer.exe process, deleting the cache files, and then restarting explorer.exe.

:: Always be careful when running scripts, especially those that modify or delete files.
:: Ensure you have backups or system restore points before running such scripts.

:: --------------
:: STEP 1: Terminate explorer.exe
:: --------------
:: The /F flag ensures the task is forcefully terminated, and the /IM flag specifies the image name of the process to be terminated.
taskkill /F /IM explorer.exe

:: Give the system a moment after killing the process
timeout /T 3 /NOBREAK

:: --------------
:: STEP 2: Navigate to the directory containing the icon cache
:: --------------
:: %userprofile% is an environment variable that points to the current user's profile directory.
cd %userprofile%\AppData\Local\Microsoft\Windows\Explorer

:: --------------
:: STEP 3: Delete the cache files
:: --------------
:: The /F flag is used to force the deletion of read-only files.
:: The /Q flag ensures the operation runs in quiet mode, so it doesn't ask for confirmation.
del /F /Q *

:: Give the system a moment after deleting the files
timeout /T 3 /NOBREAK

:: --------------
:: STEP 4: Restart the explorer.exe process
:: --------------
:: The start command is used to begin a new process, in this case, explorer.exe.
start explorer.exe
