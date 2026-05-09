@echo off
echo Installing dependencies...
python -m pip install -r requirements.txt

echo.
echo Generating fresh test PCAP file...
python generate_test_pcap.py

echo.
echo Running DPI Analyzer...
python main.py

pause
