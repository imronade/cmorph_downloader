@echo off
echo Starting CMORPH downloads in multiple tabs...
echo.

REM Start 4 separate CMD windows, each processing a different file
start "CMORPH Download 1" cmd /k "download_cmorph_single.bat filelist_data1.txt"
start "CMORPH Download 2" cmd /k "download_cmorph_single.bat filelist_data2.txt"
start "CMORPH Download 3" cmd /k "download_cmorph_single.bat filelist_data3.txt"
start "CMORPH Download 4" cmd /k "download_cmorph_single.bat filelist_data4.txt"

echo All download processes started!
echo Each file is being processed in a separate window.
echo.
pause