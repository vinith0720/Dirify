# File Organizer

## Overview
This Python script is designed to organize files from a source directory into subdirectories based on their file extensions. It takes a source directory and a target directory as inputs, then moves the files into corresponding subdirectories within the target directory, categorized by their file extensions.

## Requirements
- Python 3.x
- `os` and `shutil` standard libraries (no additional installations required)

## Script Description

### 1. Getting User Input
The script prompts the user for two directory paths:
- **Source Directory**: The path from which the files will be moved.
- **Target Directory**: The path where files will be organized.

If no input is provided, the script defaults to the current working directory (`cwd`) for the source directory and uses the provided target directory.

### 2. Directory Traversal
The script uses `os.walk()` to traverse through all the files and directories within the source directory. For each file, it:
- Determines the file extension.
- Creates a corresponding subdirectory under the target directory (if it doesn't already exist).
- Moves the file into the appropriate subdirectory.

### 3. Error Handling
The script includes error handling for common issues like:
- File not found (`FileNotFoundError`).
- Permission issues when moving files (`PermissionError`).
- General errors during the move operation (`shutil.Error`).

## How to Use

1. **Clone the repository or download the script**.
2. **Run the script** in a Python environment.
   ```bash
   python file_organizer.py
```
