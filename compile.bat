@echo off
setlocal enabledelayedexpansion

set SRC_DIR=src
set OBJ_DIR=objects
set DIST_DIR=dist
set OUTPUT_EXE=%DIST_DIR%\Sattela.exe

REM Check if src directory exists
if not exist "%SRC_DIR%" (
    echo Error: Source directory '%SRC_DIR%' not found!
    pause
    exit /b 1
)

REM Create directories if they don't exist
if not exist "%OBJ_DIR%" mkdir "%OBJ_DIR%"
if not exist "%DIST_DIR%" mkdir "%DIST_DIR%"

REM Compile all .cpp files (recursively) into object files
echo Compiling .cpp files...
set OBJ_FILES=
for /r "%SRC_DIR%" %%f in (*.cpp) do (
    echo Compiling %%f...
    g++ -std=c++17 -I"%SRC_DIR%" -c "%%f" -o "%OBJ_DIR%\%%~nf.o"
    if errorlevel 1 (
        echo Error compiling %%f!
        exit /b 1
    )
    set OBJ_FILES=!OBJ_FILES! "%OBJ_DIR%\%%~nf.o"
)

REM Link all object files into the executable
echo Linking object files...
g++ !OBJ_FILES! -o "%OUTPUT_EXE%"
if errorlevel 1 (
    echo Error linking!
    exit /b 1
)

REM Delete the objects directory
echo Cleaning up...
rmdir /s /q "%OBJ_DIR%"

echo Build successful! Output: %OUTPUT_EXE%