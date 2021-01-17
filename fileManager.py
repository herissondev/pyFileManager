from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import json
import os


class MyHandler(FileSystemEventHandler):
    def __init__(self):
            self.events = []
            self.observers = Observer() 


    def on_modified(self,event):
        for event in self.events:

            for filename in os.listdir(event[0]):
                src = event[0] + "/" + filename

                if filename.lower().endswith(event[2]):
                    os.rename(src,event[1] + "/" + filename)

    def newEvent(self, baseFolder, destFolder, extension):
        self.events.append((baseFolder, destFolder, extension))

    def start(self):
        for i in self.events:
            targetPath = str(i[0])
            self.observers.schedule(self, targetPath, recursive=True)
        
        self.observers.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observers.stop()
        self.observers.join()


    def stop(self):
        self.observers.stop()



