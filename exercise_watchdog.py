import os
import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Target:
    watchDir = os.getcwd()
    
    def __init__(self, filename):
        self.obs = Observer()
        self.filename = filename

    def run(self):
        event_handler = Handler(filename=self.filename)
        self.obs.schedule(event_handler, self.watchDir, recursive=False)
        self.obs.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.obs.stop()
            print("Error")
            self.obs.join()

class Handler(FileSystemEventHandler):

    def __init__(self, filename):
        self.filename = filename

    def on_moved(self, event):
        pass

    def on_created(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        if not Path(event.src_path).name == self.filename:
            return
        subprocess.call(f'python {self.filename}')

if __name__ == "__main__":
    w = Target('test.py')
    w.run()