import logging
import os
import tkinter as tk
from os.path import exists, join, splitext
from shutil import move
from tkinter import filedialog, messagebox

logging.basicConfig(level=logging.INFO)


def get_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = (
        filedialog.askdirectory()
    )  # Show the "Open" dialog box and return the path to the selected directory
    logging.info(f"Now cleaning {directory}. Please sit back and relax!")
    return directory


def ask_dry_run():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    dry_run = messagebox.askyesno("Dry Run", "Do you want to do a dry run?")
    return dry_run


source_dir = get_directory()
dry_run = ask_dry_run()

directories = {
    "audio": {
        "dir": "F:\\Music",
        "extensions": [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"],
    },
    "video": {
        "dir": "F:\Videos",
        "extensions": [
            ".webm",
            ".mpg",
            ".mp2",
            ".mpeg",
            ".mpe",
            ".mpv",
            ".ogg",
            ".mp4",
            ".mp4v",
            ".m4v",
            ".avi",
            ".wmv",
            ".mov",
            ".qt",
            ".flv",
            ".swf",
            ".avchd",
        ],
    },
    "image": {
        "dir": "F:\\Pictures",
        "extensions": [
            ".jpg",
            ".jpeg",
            ".jpe",
            ".jif",
            ".jfif",
            ".jfi",
            ".png",
            ".gif",
            ".webp",
            ".tiff",
            ".tif",
            ".psd",
            ".raw",
            ".arw",
            ".cr2",
            ".nrw",
            ".k25",
            ".bmp",
            ".dib",
            ".heif",
            ".heic",
            ".ind",
            ".indd",
            ".indt",
            ".jp2",
            ".j2k",
            ".jpf",
            ".jpf",
            ".jpx",
            ".jpm",
            ".mj2",
            ".svg",
            ".svgz",
            ".ai",
            ".eps",
            ".ico",
        ],
    },
    "document": {
        "dir": "F:\\Documents",
        "extensions": [
            ".doc",
            ".docx",
            ".odt",
            ".pdf",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
        ],
    },
    "compressed": {
        "dir": None,
        "extensions": [".zip", ".rar", ".7z", ".tar", ".gz"],
    },
    "isos": {
        "dir": "F:\\ISO",
        "extensions": [
            ".iso",
            ".img",
            ".vhd",
            ".dmg",  # Disk image formats
            ".exe",
            ".msi",
            ".bat",
            ".cmd",
            ".sh",  # Executable formats
            ".deb",
            ".rpm",
            ".apk",
            ".app",
            ".dmg",  # Package formats
        ],
    },
}


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        os.rename(oldName, newName)
    move(entry, dest)


def on_cleaner(directory, dry_run=False):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                _, ext = splitext(entry.name)
                ext = ext.lower()
                for category, data in directories.items():
                    if ext in data["extensions"]:
                        if category == "compressed":
                            if dry_run:
                                logging.info(
                                    f"Would delete compressed file: {entry.name}"
                                )
                            else:
                                os.remove(entry.path)
                                logging.info(f"Deleted compressed file: {entry.name}")
                        else:
                            if dry_run:
                                logging.info(
                                    f"Would move {category} file: {entry.name} to {data['dir']}"
                                )
                            else:
                                move_file(data["dir"], entry.path, entry.name)
                                logging.info(
                                    f"Moved {category} file: {entry.name} to {data['dir']}"
                                )
                        break


on_cleaner(source_dir, dry_run)
