import os
import shutil


    
cwd = os.getcwd()


def get_input(prompt, default=cwd):
    if default is not None:

        prompt = f"{prompt} [{default}]: "
    user_input = input(prompt)
    if not user_input and default is not None:
        return default
    return user_input

source_path = get_input("Enter the source directory")
target_path = get_input("Enter the target directory")


# Using os.walk() to traverse through directories and files
for dirpath, dirnames, filenames in os.walk(source_path):
    for filename in filenames:
        # Construct the full file path
        file_path = os.path.join(dirpath, filename)
        print(file_path)

        # Get the file extension
        file_extension = filename.split('.')[-1]
        
    
        # Specify the directory path where you want to create directories based on file extensions
        directory_path = os.path.join(target_path, file_extension)
        
        # Check if the directory exists, if not, create it
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            
        # move the file into target directory
        destination_file_path = os.path.join(directory_path, filename)
        
        try:
         # Moving the file to the new directory
            shutil.move(file_path, destination_file_path)
            print(f"File '{filename}' moved to '{directory_path}' successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to move file '{filename}'.")
        except shutil.Error as e:
            print(f"Error: {e}")