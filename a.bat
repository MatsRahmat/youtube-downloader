@echo off
set currentPath = %~dp0

if exist "%currentPath%env" (
    echo directory is exist
) else (
    echo directory not found
)
cmd /k