import curses
from curses import wrapper

def get_input(stdscr, r, c, prompt_string):
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()

    while True:
        c = stdscr.getch()
        if c == 8 or c == 127 or c == curses.KEY_BACKSPACE: 
            stdscr.addstr("\b \b")
        elif c != ord('\n'):
            stdscr.addch(c)
        else:
            input = stdscr.getstr(nlines - 1, 1, 200)
            return input
    

            

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.noecho()
    nlines = curses.LINES

    with open('todo.txt', "r") as f: 
        lines = f.readlines() 
    
    for i in range(len(lines)): 
        stdscr.addstr(i, 0, lines[i])

    # first, be able to type to the screen 
    while True:
        c = stdscr.getch()
        if c == ord('q'): 
            # save in an external file
            break 
        elif c == 8 or c == 127 or c == curses.KEY_BACKSPACE: 
            stdscr.addstr("\b \b")  
        elif c == ord('a'):
            input = get_input(stdscr, nlines - 1, 1, "Task Name: ")

    stdscr.refresh()

wrapper(main)