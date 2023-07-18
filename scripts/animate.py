import time
import os

def animate(s, delay=0.5):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(delay)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        animate('kubi 💞️')
        time.sleep(1)

if __name__ == "__main__":
    main()