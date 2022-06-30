# python-youtube-downloader

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Dependencies:**
 - [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) v4.60.1
 - [pytube](https://pypi.org/project/pytube/) v12.1.0


**Known issues:**
 - Crash when you pass any other link than youtube's 
 - Crash when youtube video's title has special characters that windows hate
 - Freezes while downloading, have to implement multiprocessing or something that will run downloads seperately