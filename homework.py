import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:\TinyTake\Images\DragImages"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Oi, {event.src_path} has been created!")

    def on_deleted(self, end):
        print(f"Aiyo, somebody deleted {event.src_path}!")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
