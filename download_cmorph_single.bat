@echo off
setlocal EnableDelayedExpansion

REM Get the filename parameter (default to filelist_data.txt if not provided)
set "listfile=%1"
if "%listfile%"=="" set "listfile=filelist_data.txt"

echo ============================================
echo Processing file: %listfile%
echo ============================================
echo.

REM Check if the list file exists
if not exist "%listfile%" (
    echo ERROR: File %listfile% not found!
    echo.
    pause
    exit /b 1
)

REM Count total lines for progress tracking
for /f %%i in ('type "%listfile%" ^| find /c /v ""') do set "total=%%i"
set "current=0"

echo Total files to process: %total%
echo.

for /f %%i in (%listfile%) do (
    set /a current+=1
    set "url=%%i"
    for %%f in ("%%~nxi") do (
        set "filename=%%~nxf"
        set "filenameonly=%%~nxf"
    )

    echo [!current!/%total%] Processing: !filenameonly!

    if exist "!filename!" (
        REM Ambil ukuran file lokal
        for %%A in ("!filename!") do set "localsize=%%~zA"

        REM Ambil ukuran file remote via PowerShell
        for /f %%s in ('powershell -Command "(Invoke-WebRequest -Uri '!url!' -Method Head).Headers['Content-Length']"') do (
            set "remotesize=%%s"
        )

        echo [CHECK] !filenameonly! - Local: !localsize! bytes - Remote: !remotesize! bytes

        if "!localsize!"=="!remotesize!" (
            echo [SKIP] File complete: !filenameonly!
        ) else (
            echo [RESUME] Resuming download: !filenameonly!
            curl -O --retry 5 --retry-delay 5 -C - "!url!"
        )
    ) else (
        echo [DOWNLOAD] File not found locally, downloading: !filenameonly!
        curl -O --retry 5 --retry-delay 5 "!url!"
    )
    echo.
)

echo ============================================
echo Completed processing %listfile%
echo Total files processed: %total%
echo ============================================
echo.
pause