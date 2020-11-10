#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   search_replace.py                                                        *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2020/11/03 00:02:38 by yhetman                                  *#
#*   Updated: 2020/11/03 10:45:51 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#



from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from os import listdir
from os.path import isfile, join
import re

def replace(file_path, pattern, subst):
    file_handle = open(file_path, 'r')
    file_string = file_handle.read()
    file_handle.close()

    file_string = (re.sub(pattern, subst, file_string))
    file_handle = open(file_path, 'w')
    file_handle.write(file_string)
    file_handle.close()


def func(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file_path in files:
        replace(join(mypath, file_path), "By: yhetman <marvin@42.fr>          ", "By: yhetman <yhetman@student.unit.ua>")
    for file_path in files:
        replace(join(mypath, file_path), "by yhetman", "by yhetman ")

def main():
    func("./libft/srcs/")
    func("./libft/includes/")
    func("./libft/srcs/ft_printf/")


if __name__ == "__main__":
    main()