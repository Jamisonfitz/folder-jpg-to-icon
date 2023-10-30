import os
import hashlib
from tkinter import Tk, filedialog
from PIL import Image

def select_directory():
    """
    Prompt the user to select a directory using a GUI.

    Returns:
        str: Path to the selected directory.
    """
    root = Tk()
    root.withdraw()  # Hide the main window to only show the dialog
    folder_selected = filedialog.askdirectory()
    return folder_selected

def generate_unique_id(path):
    """
    Generate a unique identifier based on the folder path using SHA256.
    
    Parameters:
        path (str): Path to the folder.

    Returns:
        str: SHA256 hash of the folder path.
    """
    return hashlib.sha256(path.encode()).hexdigest()

def process_folder(input_dir, icons_dir, refresh=False):
    """
    Process the selected folder and its subdirectories.

    Parameters:
        input_dir (str): Path to the input directory containing folders with 'folder.jpg'.
        icons_dir (str): Path to the directory where .ico files will be saved.
        refresh (bool): If True, regenerate and overwrite existing .ico files.
    """
    # Ensure the icons directory exists
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower() == "folder.jpg":
                # Full path to the folder.jpg
                full_path = os.path.join(root, file)
                
                # Generate unique ID for the folder to avoid name collisions
                unique_id = generate_unique_id(root)
                ico_path = os.path.join(icons_dir, f"{unique_id}.ico")
                
                # If refresh is True or .ico doesn't exist, generate the .ico
                if refresh or not os.path.exists(ico_path):
                    with Image.open(full_path) as img:
                        img.save(ico_path, format="ICO")
                    # Since we're updating the .ico, we'll also update the desktop.ini
                    update_desktop_ini = True
                else:
                    update_desktop_ini = False
                
                # Update the desktop.ini content for the folder, if needed
                if update_desktop_ini:
                    desktop_ini_path = os.path.join(root, "desktop.ini")
                    with open(desktop_ini_path, "w") as f:
                        f.write("[.ShellClassInfo]\n")
                        f.write(f"IconResource={ico_path},0\n")
                    
                    # Hide the desktop.ini file and set its attributes to System
                    os.system(f'attrib +S +H "{desktop_ini_path}"')
                    
                    # Set the folder attributes to System
                    os.system(f'attrib +S "{root}"')

if __name__ == "__main__":
    ICONS_DIR = r"C:\Temp\Icons"
    
    # Allow the user to select the input directory via a GUI dialog
    input_directory = select_directory()

    # Determine if refresh mode should be enabled
    refresh_mode = input("Do you want to refresh existing icons? (yes/no): ").strip().lower() == "yes"

    if input_directory:
        # Process the selected directory
        process_folder(input_directory, ICONS_DIR, refresh=refresh_mode)
        print("Processing complete. Icons have been set for the folders.")
    else:
        print("No directory selected. Exiting.")
