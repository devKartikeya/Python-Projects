from pathlib import Path
import shutil as sh
import sys

def organize_directory(target_dir_path):
    """Organizes files in the specified directory into subfolders by extension."""
    dir_path = Path(target_dir_path)

    # Validate that the provided directory exists
    if not dir_path.is_dir():
        print(f"Error: The directory '{dir_path}' does not exist.")
        return

    print(f"\nOrganizing files in: {dir_path.resolve()}\n")

    for file in dir_path.iterdir():
        if file.is_file():
            ext = file.suffix[1:].lower()  # Get the file extension without the dot
            
            if ext:  # Check if there is an extension
                target_folder = dir_path / ext
                target_folder.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
                
                # Move the file to the target folder
                destination = target_folder / file.name
                if not destination.exists():
                    sh.move(str(file), str(destination))
                else:
                    print(f"Skipping {file.name}: A file with this name already exists in '{ext}'.")
                    
    print("All Done !")

if __name__ == "__main__":
    print("Welcome to the Py-File-Organizer\nYour Ultimate Directory Cleaner!\n")
    
    # Get the directory path from user input
    user_path = input("Enter the full path of the directory you want to organize: ").strip()
    
    # Remove surrounding quotes (common when users drag-and-drop folders into the terminal)
    if user_path.startswith(("'", '"')) and user_path.endswith(("'", '"')):
        user_path = user_path[1:-1]
        
    organize_directory(user_path)
