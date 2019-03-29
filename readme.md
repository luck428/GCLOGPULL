# GCLOGPULL #
## GEOCACHING LOGBOOK READING TOOL ##

GCLOGPULL pulls the **complete** list of logs from any geocache and stores them in CSV format on your PC.

Whereas other tools only download a limited number of logs (C:geo, browser) or turned disfunctional through geocaching.com changes in their webpage,
this little tool uses the Geocaching WEB API.

It is mainly aimed at cache owners who want to keep statistics of their own caches or be able to quickly check who has visited their caches already. One other tool providing a similar solution is GSAK, but this is the free alternative.


This little tool is ready to use for windows, the windows executable can be downloaded here.
[GCLOGPULL.EXE latest version](https://github.com/luck428/GCLOGPULL/releases/download/V15/GCLOGPULL.exe).

The program runs at commandline level and has no GUI. The output is provided in 2 CSV files which can easliy be processed in a spreadsheet programs.
The program requires two mandatory input files to run.
for more details check here
[ link to input files] (Inputfiles/.gc_credentials)
[ link to input files] (Inputfiles/gc_cachelist.txt)

## How to run the program as .EXE ##

You can put the .EXE file into any subdirectory. Only the input files must located in the same directory which you should prepare before:

### Input files ###
#### 1) ".gc_credentials" ####
This file must contain you Geocaching User name and password.
pls watch for the special format of this file, it is in JSON. The format must be contained using the brackets.
Simply open in notepad and overwrite the "UUUUUU" and "1234".

```
{ "username": "UUUUUUU", "password": "1234" }
```
[Download here](https://github.com/luck428/GCLOGPULL/blob/master/Inputfiles/.gc_credentials)

Special note: 
The name of this file is as prerequisite from pychaching library which was not developped under windows.
That is the reason why it has no proper file extension. If you want to change the filename directly in the fiel explorer, this will not work.
you have to open the file in notepad (or similar program) and store it under the new name.



#### 2) "gc_cachelist.txt" ####
This file contains a list of all caches for which you want to download the complete log list.
example file:

```
GC1000
GC10
GCF
GC4
```
[Download here](https://github.com/luck428/GCLOGPULL/blob/master/Inputfiles/gc_cachelist.txt)

### Output files ###
Two outputfiles are being generated. If a file with the same name already exists from a previous run, then a copy of the existing file is created add a time stamp in the fiel name
and the current downloaded data is written to a new fresh file. eg cachedata20190327122357.csv

#### 1) "logdata.csv" ####
Example data, lines were removed and names shortened
```
GCCODE;"LogDate";"Logtype";"LogAuthor"
GC1000;"2006-02-20";"Type.archive";"K"
GC1000;"2006-01-29";"Type.temp_disable_listing";"K"
GC1000;"2005-06-12";"Type.needs_archive";"T"
GC1000;"2001-01-31";"Type.found_it";"C"
GC10;"2008-02-06";"Type.note";":-)"
GC10;"2007-07-29";"Type.didnt_find_it";"B"
GC10;"2000-04-01";"Type.found_it";"K"
GCF;"2008-08-16";"Type.note";"L"
GCF;"2000-10-22";"Type.found_it";"m"
GC4;"2001-01-07";"Type.didnt_find_it";"m"
GC4;"2000-08-27";"Type.found_it";"J"

```

#### 2) "cachedata.csv" ####
```
GCCODE;"cachetype";"Cachename";"Difficulty";"Terrain"
GC1000;"Type.traditional";"Isle Swatara";"3.0";"3.0"
GC10;"Type.traditional";"First Divine";"1.0";"1.0"
GCF;"Type.traditional";"The Original Stash";"1.0";"1.0"
GC4;"Type.traditional";"Mike's First";"1.0";"1.0"
```

## How to run the program as python script ##
You need to install a number of libraries.

### Technical prerequisites ###
If you want to execute the python script then you need to have following libraries avaiable (which are all required by pycaching):

- python 3.4
- pycaching 
- beautiful soup
- unittest
- win_unicode_console
- csv
- sys 
- os
- json
- datetime

### Dependencies ###
The program has no gui because pycaching has no gui.
the pycaching library is used unchanged as-is.

### Warranty ###

# Important #
Use at your won risk !
Especially -> BE AWARE of the consequences of groundspeak (Geocaching HQ) monitoring policies.
Limitation as "free" user -> For non premium members the limits are 3 full caches per day.
Limitation as "premium" user -> the limits are currently 6,000 full caches per day (+10,000 "lite" caches).
Your account can be blocked anytime if you exceed these limitations. You have been warned.

