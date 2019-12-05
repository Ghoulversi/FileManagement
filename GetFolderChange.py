import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

_path = input("Enter path to folder ('folder inclusive')")

def change_file_location(file_name, folder_name):
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
    
    os.replace(current_file, destination_folder  + "/" + _file_name)
    
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_name = event.src_path
        file_format = file_name[-4:]
        if file_format == '.txt':
            change_file_location(file_name, "Text")
        elif file_format == '.obj' or file_format == '.fbx':
            change_file_location(file_name, "Models")
        elif file_format == '.rar' or file_format == '.zip':
            change_file_location(file_name, "Archive")
        elif file_format == '.png':
            change_file_location(file_name, "png_format")
        elif file_format == '.jpg' or file_format == '.jpeg':
            change_file_location(file_name, "jpg_format")
        else:
            change_file_location(file_name, "Unknown")
        


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