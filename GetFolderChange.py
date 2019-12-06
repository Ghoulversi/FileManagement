import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#_path = input("Enter path to folder ('folder inclusive')")
_path = "/mnt/c/Users/Me/Downloads/"

def get_is_downloading(file_path):
    st = os.stat(file_path).st_size
    current_size = st
    
    time.sleep(0.5)
        
    while (st != os.stat(file_path).st_size):
        time.sleep(0.5)
    
    return True


def change_file_location(file_name, folder_name):
    
    st = os.stat(file_name).st_size
    current_size = st
    time.sleep(0.5)
        
    while (st != os.stat(file_name).st_size):
        time.sleep(0.5)
    
    print("go dalise")
                
    file_name_list = file_name.split("/")
    _file_name = file_name_list[-1]
    
    folder_list = folder_name.split("/")
    _folder_name = folder_list[-1]
    
    current_file = _path + _file_name
    destination_folder = _path + _folder_name
    
    if os.path.isdir(destination_folder):
        print("file exist")
    else:
        print('file doesn\'t exist')
        os.mkdir(_path + _folder_name)
        
    print("file name: " + _file_name + " current file: " + current_file)
    try:
        os.replace(current_file, destination_folder  + "/" + _file_name)
    except:
        print('Invalid file')
   
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_name = event.src_path
        file_format = file_name[-4:]
        
        try:                               
            if file_format == '.txt':
                change_file_location(file_name, "Text")
            elif file_format.upper() == '.OBJ' or file_format.upper() == '.FBX':           
                change_file_location(file_name, "Models")
            elif file_format == '.rar' or file_format == '.zip':
                change_file_location(file_name, "Archive")
            elif file_format == '.png':
                change_file_location(file_name, "png_format")
            elif file_format == '.jpg' or file_format == '.jpeg':
                change_file_location(file_name, "jpg_format")
        except:
            print("something went wrong")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()