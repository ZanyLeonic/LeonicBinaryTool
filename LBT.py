#!/usr/bin/python
import time
import os
import os.path
import sys
import webbrowser
import configparser
import logging
import lbtlib

appname="Leonic Binary Tool"
version="0.1a"
release="alpha"
configfilename="config.ini"
configfilereadname=r"config.ini"
licenseabout="""
    Leonic Binary Tool
    Copyright (C) 2016 Leo Durrant

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

def readconfig():
    if os.path.isfile(configfilename):
        print("The file exists.")
    else:
        #print("The file doesn't exist")
        createconfig()

def createconfig():
    config = configparser.ConfigParser()
    config['general'] = {'createlog': '1'}
    config['updater'] = {'checkforupdatesonstartup': '1'}
    with open(configfilename, 'w') as configfile:
        config.write(configfile)
    
def setloggingoptions():
    config = configparser.ConfigParser()
    config.readfp(open(configfilereadname))
    createlograw = config.get('general', 'createlog')
    createlog = int(createlograw)
    if createlog == 1:
        logfilename = 'log.log'
        handler = logging.FileHandler(logfilename)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        if "-debuglogging" in sys.argv:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(filename=logfilename, level=logging.DEBUG)
        logger = logging.getLogger("[LBT]")
        logger.addHandler(handler)
        logger.debug('Started %s at %s on %s', appname, time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y"))
    elif createlog == 0:
        null = ""
    else:
        null = ""
def delay_print(s):
    if("noanimtext" in sys.argv):
        print(s)
    else:
        for c in s:
            sys.stdout.write( '%s' % c )
            sys.stdout.flush()
            time.sleep(0.05)

def about():
    aboutmenu = True
    while aboutmenu:
        print("============================================")
        print(appname)
        print("Version", version)
        print("Libraries in use:")
        print(lbtlib.conlib.appname + " " + lbtlib.conlib.version + " " + lbtlib.conlib.release)
        print(lbtlib.iolib.appname + " " + lbtlib.iolib.version + " " + lbtlib.iolib.release)
        print("This is release is an", release,"release.")
        print("Written by Leo Durrant on the 5/02/16.")
        print(licenseabout)
        print("============================================")
        print("""
        Please type the number of a function.
            1. Wordpress
            2. Github
            3. Back to main menu
        """)
        print("============================================")
        aboutmenu=input(">>> ")
        if aboutmenu == "1":
            webbrowser.open("http://leonicweb.wordpress.com/")
            print("Attempted to open 'http://leonicweb.wordpress.com/' in your default webbrowser.")
            print("If it failed to do so, enter the url in your browser.")
            aboutmenu = True
        elif aboutmenu == "2":
            webbrowser.open("http://github.com/ZanyLeonic/LeonicBinaryTool/")
            print("Attempted to open 'http://github.com/ZanyLeonic/LeonicBinaryTool/' in your default webbrowser.")
            print("If it failed to do so, enter the url in your browser.")
            aboutmenu = True
        elif aboutmenu == "3":
            aboutmenu = False
        else:
            print("Invalid selection.")
            mainmenusel = True

def converttext2binary():
    ct2b = True
    while ct2b:
        print("============================================")
        print("Welcome to", appname,"!")
        print("Version", version)
        print("Mode: Text to binary")
        print("============================================")
        print("""
        Please type the number of a function.
            1. Open a text file to convert
            2. Type text to convert
            3. Back to main menu
        """)
        print("============================================")
        ct2b = input(">>> ")
        
        if ct2b == "1":
            print("Please enter a path to the text file you wish to convert.")
            path=input(">>> ")
            text=lbtlib.iolib.readfromtextfile(path)
            convertedtext=lbtlib.conlib.text2binary(text)
            print("Your text file has been converted into binary and now reads:")
            print(convertedtext)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedtext)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
                    
            ct2b=True
        elif ct2b == "2":
            print("Please input the text you want to converted into binary below.")
            text=input(">>> ")
            
            convertedtext=lbtlib.conlib.text2binary(text)
            print("Your text has been converted into binary and now reads:")
            print(convertedtext)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedtext)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
            
        elif ct2b == "3":
            ct2b = False

def convertbinary2text():
    cb2t = True
    while cb2t:
        print("============================================")
        print("Welcome to", appname,"!")
        print("Version", version)
        print("Mode: Binary to text")
        print("============================================")
        print("""
        Please type the number of a function.
            1. Open a text file to convert
            2. Type text to convert
            3. Back to main menu
        """)
        print("============================================")
        cb2t = input(">>> ")
        
        if cb2t == "1":
            print("Please enter a path to the text file you wish to convert.")
            path=input(">>> ")
            binary=lbtlib.iolib.readfromtextfile(path)
            convertedbinary=lbtlib.conlib.binary2text(binary)
            print("Your text file has been converted into text and now reads:")
            print(convertedbinary)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedtext)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
                    
            cb2t=True
        elif cb2t == "2":
            print("Please input the binary you want to converted into text below.")
            binary=input(">>> ")
            
            convertedtext=lbtlib.conlib.binary2text(binary)
            print("Your binary has been converted into text and now reads:")
            print(convertedtext)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedtext)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
            
        elif cb2t == "3":
            cb2t = False

def convertint2binary():
    ci2b = True
    while ci2b:
        print("============================================")
        print("Welcome to", appname,"!")
        print("Version", version)
        print("Mode: Integer to binary")
        print("============================================")
        print("""
        Please type the number of a function.
            1. Open a text file to convert
            2. Type text to convert
            3. Back to main menu
        """)
        print("============================================")
        ci2b = input(">>> ")
        
        if ci2b == "1":
            print("Please enter a path to the text file you wish to convert.")
            path=input(">>> ")
            integer=lbtlib.iolib.readfromtextfile(path)
            convertedinteger=lbtlib.conlib.int2binary(integer)
            print("Your text file has been converted into text and now reads:")
            print(convertedinteger)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedinteger)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
                    
            ci2b=True
        elif ci2b == "2":
            print("Please input the integer you want to converted into binary below.")
            integer=input(">>> ")
            
            convertedinteger=lbtlib.conlib.int2binary(integer)
            print("Your integer has been converted into binary and now reads:")
            print(convertedinteger)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted integer as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedinteger)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
            
        elif ci2b == "3":
            ci2b = False

def convertbinary2int():
    cbti = True
    while cbti:
        print("============================================")
        print("Welcome to", appname,"!")
        print("Version", version)
        print("Mode: Binary to integer")
        print("============================================")
        print("""
        Please type the number of a function.
            1. Open a text file to convert
            2. Type text to convert
            3. Back to main menu
        """)
        print("============================================")
        cbti = input(">>> ")
        
        if cbti == "1":
            print("Please enter a path to the text file you wish to convert.")
            path=input(">>> ")
            binary=lbtlib.iolib.readfromtextfile(path)
            convertedbinary=lbtlib.conlib.binary2int(binary)
            print("The binary inside your text file has been converted into an integer and now reads:")
            print(convertedbinary)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedbinary)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
                    
            cbti=True
        elif cbti == "2":
            print("Please input the binary you want to converted into an integer below.")
            binary=input(">>> ")
            
            convertedbinary=lbtlib.conlib.binary2int(binary)
            print("Your binary has been converted into an integer and now reads:")
            print(convertedbinary)
            
            writetotextfilemenu=True
            while writetotextfilemenu:
                print("Do you want to save the converted binary as a text file?")
                print("1. Yes")
                print("2. No")
                writetotextfilemenu=input(">>> ")

                if writetotextfilemenu == "1":
                    lbtlib.iolib.writetotextfile(convertedbinary)
                    writetotextfilemenu=False

                elif writetotextfilemenu == "2":
                    writetotextfilemenu=False

                else:
                    print("Invalid selection")
                    writetotextfilemenu=True
            
        elif cbti == "3":
            cbti = False

def settings():
    catsets = True
    while catsets:
        print("============================================")
        print("Welcome to", appname,"!")
        print("Version", version)
        print("Settings")
        print("============================================")
        print("""
        Please type the number of a settings category.
            1. General
            2. Updater
            3. Back to main menu
        """)
        print("============================================")
        catsets = input(">>> ")
        
        if catsets == "1":
            sets = True
            while sets:
                print("============================================")
                print("Welcome to", appname,"!")
                print("Version", version)
                print("Settings>General")
                print("============================================")
                print("""
                Please type the number of a settings category.
                1. General
                2. Updater
                3. Back to main menu
                """)
                print("============================================")
                sets = input(">>> ")
    
mainmenusel = True
while mainmenusel:
    readconfig()
    setloggingoptions()
    print("============================================")
    print("Welcome to", appname,"!")
    print("Version", version)
    print("============================================")
    print("""
    Please type the number of a function.
        1. Convert text to binary
        2. Convert binary to text
        3. Convert integer to binary
        4. Convert binary to integer
        5. Settings
        6. About
        7. Exit
    """)
    print("============================================")
    mainmenusel = input(">>> ")
    if mainmenusel == "1":
        converttext2binary()
        mainmenusel = True
    elif mainmenusel == "2":
        convertbinary2text()
        mainmenusel = True
    elif mainmenusel == "3":
        convertint2binary()
        mainmenusel = True
    elif mainmenusel == "4":
        convertbinary2int()
        mainmenusel = True
    elif mainmenusel == "5":
        print("TODO: Add function.")
        mainmenusel = True
    elif mainmenusel == "6":
        about()
        mainmenusel = True
    elif mainmenusel == "7":
        print("See ya!")
        mainmenusel = False
    elif mainmenusel != "":
        print("Invalid selection.")
        mainmenusel = True
    else:
        print("Invalid selection.")
        mainmenusel = True
        
