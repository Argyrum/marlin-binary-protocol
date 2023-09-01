#!/usr/bin/env python3

"""

Curse-based helper script to manage files and updates on a 3d printer running under marlin with support for binary transfer

Features:
    L)oad list      WIP
    U)pload file    WIP
    R)emove file    WIP
    P)rint file     WIP
    C)hange port    WIP
    Q)uit           Done
    
"""


import curses


menulines = 5
menutitle = " Marlin Binary Transfer Helper "


def display_menu(stdscr):
    stdscr.addstr(linmax - menulines + 1, 4, 
        'Use the arrow keys to select')
    stdscr.addstr(linmax - menulines + 3, 4,
        'L)oad list    U)pload file    R)emove file    P)rint file    C)hange port    Q)uit')
    stdscr.noutrefresh()

def display_list(listscr):
    listscr.box()
    listscr.addstr(0, int(colmax/2 - len(menutitle)/2), menutitle)


def process_input(listscr):
    pass


def main(stdscr):
    # Get screen size and parameters
    #linmax = curses.LINES - 1 # y coord c [0 linmax]
    #colmax = curses.COLS - 1 # x coord c [0 volmax]
    global linmax, colmax
    linmax, colmax = stdscr.getmaxyx()
    listscr = stdscr.derwin(linmax - menulines, colmax, 0,0)

    # Configure transparency and cursor
    curses.use_default_colors()
    curses.curs_set(0)

    # Print overlay
    stdscr.clear()
    display_menu(stdscr)
    display_list(listscr)

    # Main loop - Wait for input
    while True:
        key = listscr.getkey() # Includes a refresh
        if key == "q":
            curses.endwin()
            break
        else:
            process_input(listscr)


if __name__ == "__main__":
    curses.wrapper(main)

# Misc commands

#stdscr.refresh() # Updates window (Mark pending + doupdate)
#stdscr.noutrefresh() # Marks window for update
#curses.doupdate # Updates pending windows
# f("blabla {i}") -> fstring, casts variable i into an string and inserts it (Python 3.6>=)

"""
Manual implementation of box()

    hborder = "+" + ((colmax - 2) * "-") + "+"
    stdscr.addstr(0, 0, hborder)
    for y in range(1, linmax - menulines - 1):
        stdscr.addch(y, 0, "|")
        stdscr.addch(y, colmax - 1, "|")
    stdscr.addstr(linmax - menulines - 1, 0, hborder)

"""