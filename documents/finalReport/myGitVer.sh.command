#!/bin/sh

# shell script to get git version number and save to a text file  in the current directory.

# Notes: 
#  * The resulted file name is myGitVer.txt by default OR the file name passed to the script if any.
#  * The prouced file will be empty if the current directory is NOT a git repository (or any of the parent directories)

# Author: Mohammed Nour A. Ahmed
# Date: 2017.01.05
# Version: 1:00 

# To make a shell script change to the folder in which it is located
cd -- "$(dirname "$0")"


# check for file name or use the default if none is passed
OUTPUTFILENAME=${1:-myGitVer.txt}

# get git version number and save to file myGitVer.txt
git log -1 --pretty=format:"%h%x3b%ad" --date=format:"%Y%m%d-%H%M%S" > $OUTPUTFILENAME


echo "Results are saved in file: $OUTPUTFILENAME"


# in latex, you can call this script with:
# \immediate\write18{./myGitVer.sh.command \jobname.txt}
# \input{\jobname.txt}
