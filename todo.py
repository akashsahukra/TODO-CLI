import datetime
import sys
import os
import colorama
from colorama import Fore, Style


def help1():

    print(Fore.YELLOW)
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo lsdone           # Show completed todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')

    print(Style.RESET_ALL)


def error():
    print(Fore.LIGHTRED_EX)
    print("Invalid Argument \t" + Fore.LIGHTGREEN_EX + "Refer help doc")
    print(Style.RESET_ALL)
    help1()


def add1():
    print(Fore.RED)
    print('Error: Missing todo string. Nothing added!')
    print(Style.RESET_ALL)


def done1():
    print(Fore.RED)
    print('Error: Missing NUMBER for marking todo as done.')
    print(Style.RESET_ALL)


def report1():
    f = open("todo.txt", "a")
    f.close()
    f1 = open("done.txt", "a")
    f1.close()
    with open("todo.txt", "r") as todo:
        pending = len(todo.readlines())
    with open("done.txt", "r") as done:
        completed = len(done.readlines())
    print(Fore.YELLOW + str(datetime.date.today()) + Fore.LIGHTRED_EX+' Pending : ' +
          str(pending) + Fore.LIGHTGREEN_EX+' Completed : ' + str(completed))
    print(Style.RESET_ALL)


def add(item):
    f = open(file="todo.txt", mode='a')
    f.write(item + '\n')
    f.close()
    print(Fore.GREEN)
    print('Added todo: "' + item + '"')
    print(Style.RESET_ALL)


def del1(num):
    line_no = int(num)
    f = open("todo.txt", "a")
    f = open("todo.txt", 'r+')
    lines = f.readlines()
    if line_no > len(lines) or line_no == 0:
        print(Fore.RED)
        sys.stdout.write('Error: todo #'+num +
                         ' does not exist. Nothing deleted.')
        print(Style.RESET_ALL)
        return
    f.seek(0)
    for i in lines:
        if i != lines[line_no - 1]:
            f.write(i)
    f.truncate()
    print(Fore.LIGHTCYAN_EX)
    print("Deleted todo #" + num)
    print(Style.RESET_ALL)
    f.close()


def ls1():

    with open("todo.txt", "a") as f:
        f = open("todo.txt", "r")
        lines = f.readlines()
        n = len(lines)
        if n == 0:
            print(Fore.LIGHTCYAN_EX)
            print('There are no pending todos!')
            print(Style.RESET_ALL)
            return
        for i in range(n - 1, -1, -1):

            print(colors[i % c_len])
            print('[' + str(i + 1) +
                  '] ' + lines[i][:-1])
        print(Style.RESET_ALL)


def lsdone1():
    with open("done.txt", "a") as f:
        f = open("done.txt", "r")
        lines = f.readlines()
        n = len(lines)
        if n == 0:
            print(Fore.LIGHTCYAN_EX)
            print('There are no completed todos!')
            print(Style.RESET_ALL)
            return
        for i in range(n - 1, -1, -1):
            l = lines[i][:-1]
            print(colors[i % c_len])
            print('[' + str(i + 1) + '] ' + l)
        print(Style.RESET_ALL)


def done(num):
    line_no = int(num)
    f = open("todo.txt", 'r+')
    lines = f.readlines()
    if line_no > len(lines) or line_no == 0:
        print(Fore.RED)
        print('Error: todo #' +
              num + ' does not exist.')
        print(Style.RESET_ALL)
        return
    f.seek(0)
    for i in lines:
        if i != lines[line_no - 1]:
            f.write(i)
        else:
            over = i
    f.truncate()
    with open("done.txt", "a") as f2:
        f2.write(over)
    print(Fore.GREEN)
    print('Marked todo #' + num + ' as done.')
    print(Style.RESET_ALL)
    f.close()


if __name__ == '__main__':

    colorama.init()

    over = ""
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.GREEN,
              Fore.YELLOW, Fore.RED, Fore.LIGHTCYAN_EX, Fore.LIGHTBLACK_EX, Fore.BLUE, Fore.LIGHTYELLOW_EX, Fore.LIGHTRED_EX]
    c_len = len(colors)
    if len(sys.argv) == 1:
        help1()
    elif sys.argv[1] == 'del':

        sys.argv[1] = "del1"
        if len(sys.argv) == 2:
            print(Fore.RED)
            print(
                'Error: Missing NUMBER for deleting todo.')
            print(Style.RESET_ALL)
        else:
            try:
                globals()[sys.argv[1]](sys.argv[2])
            except:
                error()

    elif len(sys.argv) == 2:
        try:
            globals()[sys.argv[1]+"1"]()
        except:
            error()
    else:
        # print(sys.argv)
        try:
            globals()[sys.argv[1]](sys.argv[2])
        except:
            error()
