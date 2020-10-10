#!/usr/bin/python3

import os

TG_PATH = "/home/yhetman/Downloads/Telegram Desktop/"
TG_FILE_PATH = "/home/yhetman/Downloads/Telegram\ Desktop/"

DWN_PATH = "/home/yhetman/Downloads/"

download_files = os.listdir(DWN_PATH)

telegram_files = os.listdir(TG_PATH)

all_files = download_files + telegram_files


for file_name in telegram_files:
    _file_name = file_name.replace(" ", "-")
    _file_name = _file_name.replace("(", "-")
    _file_name = _file_name.replace(")", "-")

    extension = os.path.splitext(file_name)[-1].lower()
    fpath = os.path.join(TG_PATH, file_name)

    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        os.rename(fpath, "/home/yhetman/Pictures/" + _file_name)
        print ("Picture moved", fpath)
    elif extension in ['.xlsx', '.xls']:
        os.rename(fpath, DWN_PATH + "xlsx_files/" + _file_name)
        print("Excel file moved", fpath)
    elif extension in ['.pptx', '.ppt']:
        os.rename(fpath, DWN_PATH + "pptx_files/" + _file_name)
        print("Power point file moved", fpath)
    elif extension in ['.docx', '.doc', '.docs']:
        os.rename(fpath, DWN_PATH + "doc_files/" + _file_name)
        print("Document file moved", fpath)
    else:
        dir_name = str(extension[1:]) + "_files"
        dir_path = DWN_PATH + dir_name
        if os.path.exists(dir_path) == False:
            os.mkdir(dir_path)
        print(dir_path,"\t", dir_name)
        os.rename(fpath, dir_path + '/' + _file_name)

