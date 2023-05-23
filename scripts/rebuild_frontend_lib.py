# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Directory to monitor
directory = "../frontend/lib"

# Command to run on file change
command = "cd ../frontend && yarn buildLib"

# File extensions to monitor
extensions = [".ts", ".tsx", ".js", ".jsx"]

# Directories to ignore
ignored_directories = ["dist"]


class FileChangeHandler(FileSystemEventHandler):
    def should_ignore_directory(self, directory):
        for ignored_dir in ignored_directories:
            if ignored_dir.lower() in directory.lower():
                return True
        return False

    # when a new file is created
    def on_created(self, event):
        self.execute_command(event)

    # when a new file is modified
    def on_modified(self, event):
        self.execute_command(event)

    # rebuild the library
    def execute_command(self, event):
        if not event.is_directory:
            _, file_extension = os.path.splitext(event.src_path)
            if (
                file_extension.lower() in extensions
                and not self.should_ignore_directory(event.src_path)
            ):
                print(f"File {event.src_path} changed. Running {command}...")
                subprocess.call(command, shell=True)


if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        print(f"Watching directory '{directory}' for file changes...")
        observer.join()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()