#!/usr/bin/python3

import os

def push():
    branch = input("Choose branch to push: ")
    command = "git push origin " + branch
    os.system(command)


if __name__ == "__main__":
    push()
