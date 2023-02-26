@echo off
title Batch Script for Running the Converter Application

REM Activate the Python virtual environment (if you're using one)
REM activate env

REM Run the Convert_logic.py file in the background
start /B python Convert_logic.py

REM Run the Converter_UI.py file in the foreground
python Converter_UI.py

REM Deactivate the Python virtual environment (if you're using one)
REM deactivate
