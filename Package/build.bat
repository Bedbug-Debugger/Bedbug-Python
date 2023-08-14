@ECHO off
rmdir /s /q bedbug.egg-info
rmdir /s /q src\bedbug.egg-info
PAUSE

py -m build
