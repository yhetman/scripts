#!/usr/bin/python3

import os

DWN_PATH = "/home/yhetman/Downloads/"

def moving_files(path):
    files_list = os.listdir(path)

    for file_name in files_list:
       fpath = os.path.join(path, file_name)
       if os.path.isdir(fpath):
           print("Directory ", file_name, " !")
           continue
       _file_name = file_name.replace(" ", "-")
       _file_name = _file_name.replace("(", "-")
       _file_name = _file_name.replace(")", "-")
       extension = os.path.splitext(file_name)[-1].lower()
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


def main():
    TG_PATH = "/home/yhetman/Downloads/Telegram Desktop/"
    moving_files(DWN_PATH)
    moving_files(TG_PATH)



if __name__ == "__main__":
    main()
