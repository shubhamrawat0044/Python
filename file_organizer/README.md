# Python File Organizer

A simple Python script that automatically organizes files into separate folders based on their file extensions.

## Features

- Organizes images into an `Images` folder.
- Organizes documents into a `Documents` folder.
- Organizes videos into a `Videos` folder.
- Organizes compressed files into an `Archives` folder.
- Organizes scripts into a `Scripts` folder.
- Moves unrecognized file types into an `Others` folder.
- Prevents overwriting files by renaming duplicates with a number suffix.
- Handles file-moving errors using exception handling.

## Technologies Used

- Python 3
- `pathlib` — for handling file and folder paths.
- `shutil` — for moving files.

## How It Works

1. The script scans the specified directory.
2. It checks each item's file extension.
3. It creates the appropriate category folder if it does not exist.
4. It moves the file into the matching folder.
5. If a file with the same name already exists, it adds a number to the filename to avoid overwriting it.
6. If an error occurs while moving a file, the script prints an error message.

## Configuration

Update the `folder_path` variable in the script to specify the directory you want to organize.

```python
folder_path = Path(r"")
```

Replace the path with your target folder.

## How to Run

1. Install Python 3 if it is not already installed.
2. Save the script as `file_organizer.py`.
3. Open a terminal in the project directory.
4. Run:

```bash
python file_organizer.py
```

On Windows, you can also use:

```bash
py file_organizer.py
```

## Safety Notes

- Test the script with sample files before using it on important data.
- The script moves files rather than copying them.
- Files with unsupported extensions are moved to `Others`.
- Keep a backup of important files before running the script.

## Future Improvements

- Add a dry-run mode to preview file movements.
- Add logging to record moved and skipped files.
- Support additional file extensions.
- Allow the user to select the target directory at runtime.
