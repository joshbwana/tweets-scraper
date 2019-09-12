# tweets-scraper
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup in linux)
* [Setup](#setup in windows)

## General info
This project is a simple python script for scrapping twitter accounts. The script works by the user providing a twitter account name,it then scraps ones' tweets and displays in then starting with the latest tweet. The script runs in linux and windows machine with python 3 installed on them.
	
## Technologies
Project is created with:
* python: 3.7
* Beautifulsoup4 library

	
## Setup in linux
To run this project, locally in linux:

```
$ chmod +x tweets-scraper.py
$./tweets-scraper.py

## Setup in windows
To run this project, locally in windows as an executable file:

```
$ Install python 3.7 with pip installer found here:
"https://www.python.org/"

$ pip install pyinstaller
$ pyinstaller --onefile "tweets-scraper.py"
$ In the dist directory double click 'tweets-scraper.exe' to run the executable
