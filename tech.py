import curses
import time
import datetime
import random

def draw_logo(stdscr):
    logo = """
    ██████╗ █████╗ ██╗     ██╗   ██╗███████╗
    ██╔══██╗██╔══██╗██║     ██║   ██║██╔════╝
    ██████╔╝███████║██║     ██║   ██║███████╗
    ██╔═══╝ ██╔══██║██║     ██║   ██║╚════██║
    ██║     ██║  ██║███████╗╚██████╔╝███████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
    """
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 2, logo)
    stdscr.attroff(curses.color_pair(1))

def draw_datetime(stdscr):
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    stdscr.addstr(curses.LINES - 2, curses.COLS - len(dt_string) - 2, dt_string)

def display_user_info(stdscr, email, password, balance):
    color = random.randint(1, 6)
    stdscr.attron(curses.color_pair(color))
    stdscr.addstr(16, 2, f"Email: {email}")
    stdscr.addstr(17, 2, f"Password: {password}")
    stdscr.addstr(18, 2, f"User: {email}")
    stdscr.addstr(20, 2, f"BTC Balance: {balance:.8f}")
    stdscr.attroff(curses.color_pair(color))

def display_history(stdscr, history):
    stdscr.addstr(22, 2, "BTC MULTIPLY history:")
    for index, entry in enumerate(history, start=1):
        stdscr.addstr(23 + index, 4, f"{index}. {entry}")

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)
    curses.init_pair(6, curses.COLOR_CYAN, -1)
    curses.init_pair(7, curses.COLOR_RED, -1)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    stdscr.addstr(10, 2, "TanoraTech")
    stdscr.addstr(14, 2, "Welcome to my application!")
    stdscr.refresh()

    stdscr.addstr(16, 2, "Enter your email: ")
    email = stdscr.getstr().decode('utf-8')
    stdscr.addstr(17, 2, "Enter your password: ")
    password = stdscr.getstr().decode('utf-8')

    user_balance = 0.12345678
    time.sleep(1)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, password, user_balance)
    stdscr.refresh()
    time.sleep(2)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, password, user_balance)
    stdscr.addstr(22, 2, "BTC MULTIPLY history:")
    stdscr.refresh()

    history = []

    while True:
        draw_datetime(stdscr)
        # Ajout d'un historique toutes les deux secondes
        entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: You won 0.00000092 BTC!"
        history.append(entry)
        display_history(stdscr, history)
        stdscr.refresh()
        time.sleep(2)

        # Gestion de la fermeture de l'application avec la touche 'q'
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
