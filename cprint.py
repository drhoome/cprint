#!/usr/bin/env python
# Version 0.0.2 Beta

# cprint - Coloured print for command line python softwares.
# Copyright (C) 2014  Artur 'hoOmE' Paiva

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For more info please visit https://github.com/drhoome/cprint.

# Import all necessay modules
from sys import version_info, platform,stdout
from os import system

# Check version of python and operating system
if version_info[0] < 2 or (version_info[1] < 5 and version_info[0] == 2):
    raise EnvironmentError("Version of python too old, cprint need at least version 2.5 of Python.")

if platform.startswith("win"):
    raise EnvironmentError("cprint is designed for Unix operating systems and cannot run on Windows.")

# Function that process the markup
def _cmarkup(string):
    string = string.replace("<black>","\033[30m")
    string = string.replace("<red>","\033[31m")
    string = string.replace("<green>","\033[32m")
    string = string.replace("<yellow>","\033[33m")
    string = string.replace("<blue>","\033[34m")
    string = string.replace("<pink>","\033[35m")
    string = string.replace("<cyan>","\033[36m")
    string = string.replace("<white>","\033[37m")
    string = string.replace("<default>","\033[m")

    string = string.replace("<normal>","\033[0m")
    string = string.replace("<bold>","\033[1m")
    string = string.replace("<underline>","\033[4m")
    string = string.replace("<blink>","\033[5m")
    string = string.replace("<reverse>","\033[7m")

    return(string)


# Configure background
def _cbackg(string,color):
    if color == "black":
        string = "\033[40m" + string
    elif color == "red":
        string = "\033[41m" + string
    elif color == "green":
        string = "\033[42m" + string
    elif color == "yellow":
        string = "\033[43m" + string
    elif color == "blue":
        string = "\033[44m" + string
    elif color == "pink":
        string = "\033[45m" + string
    elif color == "cyan":
        string = "\033[46m" + string
    elif color == "gray":
        string = "\033[47m" + string
    elif color == "default":
        string = "\033[m" + string
    return(string)

# Function to print on screen
def cprint(string,background="default"):
    string = _cbackg(string,background)
    string = _cmarkup(string)
    string += "\033[m"
    stdout.write(string)

# Function to print on screen with a newline
def cprintln(string,background="default"):
    string = _cbackg(string,background)
    string = _cmarkup(string)
    string += "\033[m"
    stdout.write(string+"\n")

# Print some predeterminated dialogs
def cok(string=""):
    cprint("<bold><white>[ <green>OK<white> ]<default> %s" % string)

def cwarning(string=""):
    cprint("<bold><white>[ <yellow>WARNING<white> ]<default> %s" % string)

def cerror(string=""):
    cprint("<bold><white>[ <red>ERROR<white> ]<default> %s" % string)

def cinfo(string=""):
    cprint("<bold><white>[ <blue>info<white> ]<default> %s" % string)

# Clear the screen
def cclear(background="default"):
    string = _cbackg("",background)
    stdout.write(string+"\n")
    system("clear")

# Reset to default
def creset():
    stdout.write("\033[m"),

# Add a new line
def cnewline():
    stdout.write("\n")

# About cprint
def cabout():
    cprintln("<bold><yellow>cprint<default><bold> - <green>Coloured print for command line python softwares<default><bold>.")
    cprintln("<bold>Developed by Artur 'hoOmE' Paiva - <underline>dr.hoome@gmail.com<default><bold>.")
    cnewline()
    cprintln("<bold>For more info, please visit <underline>https://github.com/drhoome/cprint<default><bold>.")
    cnewline()
    cprintln("<bold>This program comes with <red>ABSOLUTELY NO WARRANTY<default><bold>.")
    cprintln("<bold>This is free software, and you are welcome to redistribute it under certain conditions.")
