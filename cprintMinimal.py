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
from sys import version_info,platform,stdout

# Check version of python and operating system
if version_info[0] < 2 or (version_info[1] < 5 and version_info[0] == 2):
    raise EnvironmentError("Version of python too old, cprint need at least version 2.5 of Python.")

if platform.startswith("win"):
    raise EnvironmentError("cprint is designed for Unix operating systems and cannot run on Windows.")

# Function to print on screen
def cprint(string,background="default"):
    if background == "black":
        string = "\033[40m" + string
    elif background == "red":
        string = "\033[41m" + string
    elif background == "green":
        string = "\033[42m" + string
    elif background == "yellow":
        string = "\033[43m" + string
    elif background == "blue":
        string = "\033[44m" + string
    elif background == "pink":
        string = "\033[45m" + string
    elif background == "cyan":
        string = "\033[46m" + string
    elif background == "gray":
        string = "\033[47m" + string
    elif background == "default":
        string = "\033[m" + string
    else:
        string = "\033[m" + string

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

    string += "\033[m"

    stdout.write(string)

# Function to print on screen with a newline
def cprintln(string,background="default"):
    cprint(string,background)
    stdout.write("\n")
