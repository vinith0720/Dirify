# Drify
The File Organizer for your folder,it mainly used in (`Downloads`) Folder
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
3. **Enter the source and target directory paths when prompted**.
The source directory is the location where the files you want to organize are stored.
The target directory is where the files will be moved to, categorized by file extension.
## Example
```javascript
Enter the source directory: /path/to/source
Enter the target directory: /path/to/target
```
## Error Handling
The script will handle errors gracefully and print appropriate error messages, such as when the file is not found or when there's a permission issue.
## License
```
This project is licensed under the MIT License - see the LICENSE file for details.
```

## Contributions
Feel free to fork the repository and submit pull requests with improvements or bug fixes.

```css

This markdown file gives a complete description of your project, including its functionality, usage, and error handling, making it easy for others to understand and use.







