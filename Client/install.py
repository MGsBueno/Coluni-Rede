from ast import Constant
import os, constant, shutil


def create_directory():
    try: 
        os.mkdir(constant.APP)
        print("Directory created")
    except FileExistsError:
        print("directoryalready exists!\n")


def copy_files():
    current_directory = os.getcwd()
    destination_directory = constant.APP

    for file_name in os.listdir(current_directory):
        if file_name != "install.py":
            try:    
                if file_name.endwith(".py") or file_name.endwith(".pyw"):
                    source = current_directory+file_name
                    destination = destination_directory+file_name
                    shutil.copy(source,destination)
                    print("copied" + file_name)
            
                    
            
            
            except:print("not copied "+ file_name + ", archive alredy exist!")


create_directory()
copy_files()