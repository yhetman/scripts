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
        if ".png" in file_path or ".jpeg" in file_path:
            continue
        replace(join(mypath, file_path), "/home/yhetman/Downloads/service-photos/", "/root/tf2-obj-det/models/research/object_detection/images/test/")
        replace(join(mypath, file_path), "<folder>service-photos</folder>", "<folder>test</folder>")

def main():
    func("/root/tf2-obj-det/models/research/object_detection/images/test/")
#   func("/root/tf2-obj-det/models/research/object_detection/images/train/")


if __name__ == "__main__":
    main()
