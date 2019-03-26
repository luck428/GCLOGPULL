# GCLOGPULL    GEOCACHING LOGBOOK READING TOOL #

GCLOGPULL pulls the **complete** list of logs from any geocache and stores them as CSV files on your PC.

Whereas other tools only download a limited number of logs or turned disfunctional through geocaching.com changes in their webpage
this little tool uses the Geocaching WEB API

It is mainly aimed at cache owners who want to keep statistics of their own caches or be able to quickly check who has visited their caches already
The only other tool providing a similar solution is GSAK. This is the free alternative.


This little tool is ready to use for windows, the windows executable can be downloaded here.
https://github.com/luck428/GCLOGPULL/releases/download/V15/GCLOGPULL.exe

It runs at commandline level and has no GUI. The output is provided in 2 CSV files which can easliy be processed further in a spreadsheet program.
A program requires two mandatory input files to run "can be downloaded here".

for more details check here
[ link to input files] (inputfiles/gc_cachelist.txt)


## How to run the program as .EXE ##

you can put the .EXE into any subdirectory.
The same directory must contain your input files which you have to prepare before:

### Input files ###
#### .gc_credentials ####
This file must contain you Geocaching User name and password.
pls watch for the special format of this file, it is in JSON. The format must be contained using the brackets.
Simply open in notepad and overwrite the "UUUUUU" and "1234".

```
{ "username": "UUUUUUU", "password": "1234" }
```

Special note: 
The name of this file is as prerequisite from pychaching library which was not developped under windows.
That is the reason why it has no proper file extension.


#### gc_cachelist.txt ####
This file contains a list of all caches for which you want to download the complete log list.
example file:

```
GC1000
GC10
GCF
GC4
```

### Output files ###
Two outputfiles are being generated.

#### logdata.csv ####
#### cachedata.csv ####
If a file with the same name already exists from a previous run, then a copy of the existing file is created add a time stamp in the fiel name
and the current downloaded data is written to a new fresh file.

## How to run the program as python script ##



### Technical prerequisites ###
if you want to execute the python script you need to have following libraries avaiable (which are all required by pycaching):


python 3.4
 	pycaching 
 		beautiful soup





### Dependencies ###
no gui



### Warranty ###
use at your won risk
BE AWARE of the consequences and groundspeak policies monitoring


