#!/usr/bin/python3

import os

def script():
    times = int(input("Set number of commits: "))
    commit = input("Input commit: ")
    for i in range(times):
        command = ("echo \"\n|"
                + str(i)
                + "|"
                + str(commit)
                + "|\" > latest-commit")
        os.system(command)
        os.system("git add --all;git status")
        command = ("git commit -m \"" + str(commit) + "\"")
        os.system(command)

if __name__ == "__main__":
    script()
