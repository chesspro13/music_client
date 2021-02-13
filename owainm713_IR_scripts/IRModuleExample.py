#!/usr/bin/env python3
"""IRModuleExample1, program to practice using the IRModule

Created Apr 30, 2018"""

"""
Copyright 2018 Owain Martin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import RPi.GPIO as GPIO
import IRModule
import time

def remote_callback(code):        

    # Codes listed below are for the
    # Sparkfun 9 button remote

#   print("Code: " + str(code))


#   if code == 16753245:
    if code == 0xFFA25D:
        print('Power Button')
    elif code == 0xFFE21D:
        print('Menu Button');
    elif code == 0xFF22DD:
        print('Testing')
    elif code == 0xFF02FD:
        print('Volume Up')
    elif code == 0xFFC23D:
        print('Restart')
    elif code == 0xFFE01F:
        print('Back')
    elif code == 0xFFA857:
        print('Play')
    elif code == 0xFF906F:
        print('Forward')
    elif code == 0xFF9867:
        print('Volume Down')
    
#   else:
#       print('.')  # unknown code

    return
