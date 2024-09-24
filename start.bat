@echo off
set currentPath=%~dp0
if exist "%currentPath%env\Scripts\activate.bat" (
    %currentPath%env\Scripts\activate.bat && python .
) else (
    python .
)
pause