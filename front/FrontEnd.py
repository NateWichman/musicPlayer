import curses
import curses.textpad

import sys
import exceptions
import time
import os

class FrontEnd:
    def __init__(self, player):
        hasPrinted = False
        while True:
            try:
                self.player = player
                # self.player.play(sys.argv[1])
                curses.wrapper(self.menu)
            except exceptions.CLI_Audio_Screen_Size_Exception:
                if not hasPrinted:
                    print("Window is too small, please resize")
                    hasPrinted = True;
                time.sleep(.1)
            else:
                break

    def menu(self, args):
        self.stdscr = curses.initscr()

        '''throwing error if height or width are too small'''
        height, width = self.stdscr.getmaxyx()
        if(height < 20):
            raise exceptions.CLI_Audio_Screen_Size_Exception
        if(width < 20):
            raise exceptions.CLI_Audio_Screen_Size_Exception
        '''End of inserted code'''

        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                for root, dirs, files in os.walk("."):
                    for filename in files:
                        print(filename)
    
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        try:
             changeWindow = curses.newwin(5, 40, 5, 50)
             changeWindow.border()
             changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
             self.stdscr.refresh()
             curses.echo()
             path = changeWindow.getstr(1,1, 30)
             curses.noecho()
             del changeWindow
             self.stdscr.touchwin()
             self.stdscr.refresh()
             self.player.stop()
             #self.player.play(path.decode(encoding="utf-8"))
        except CLI_Audio_File_Exception:
            pass
        

    def quit(self):
        self.player.stop()
        exit()
