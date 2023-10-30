
# Folder.jpg to Icon Processor

A Python script that automates the process of setting custom icons for folders based on `folder.jpg` images present within them.

![Before and After Comparison](https://github.com/Jamisonfitz/folder-jpg-to-icon/raw/main/assets/before_after.png)

## Features

- **Automated Icon Setting**: Recursively scans the selected directory for `folder.jpg` files and sets them as custom folder icons.
- **ICO Generation**: Automatically creates `.ico` files corresponding to each `folder.jpg`.
- **Refresh Option**: Provides the ability to refresh and update existing icons based on updated `folder.jpg` images.

## Prerequisites

- This tool is designed specifically for Windows operating systems.
- It assumes the presence of `folder.jpg` files within folders. The script does not generate `folder.jpg` files but uses them to create and set custom folder icons.

## Installation

1. Clone this repository or download as a ZIP file.
2. Extract the contents to your desired location.
3. Ensure you have Python installed. If not, download and install Python from [here](https://www.python.org/downloads/).
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the directory containing the script.
2. Run the script using the command:

```bash
python main.py
```

3. A GUI dialog will prompt you to select the directory you wish to process.
4. After selecting the directory, you will be prompted to decide if you want to refresh existing icons:
   - **Yes**: If chosen, the script will regenerate and overwrite existing `.ico` files based on the `folder.jpg` images. This is particularly useful if any `folder.jpg` images have been updated or changed.
   - **No**: If chosen, the script will skip folders that already have an associated `.ico` file and will only process new ones.
5. The script will then process the selected directory, creating icons for the folders.

## Demo

The provided demo folder contains a few sample folders with `folder.jpg` images to demonstrate the functionality of the script.

### Demo Photos Attribution

All photos used in the demo are under the **Public Domain Dedication (CC0)** license. Proper credits are provided below:

- **Robin** photo by [Wildlife Terry](https://www.flickr.com/photos/wistaston/)
- **Cardinal & Blue Jay** photo by [Stephen Rahn](https://www.flickr.com/photos/srahn/)
- **Yellowhammer** photo by [Stein Arne Jensen](https://www.flickr.com/photos/steinarnejensen/)

## Acknowledgments

- This project utilizes the [Pillow](https://python-pillow.org/) library for image processing.

## Troubleshooting

### Icons Not Displaying After Processing

If after running the main script, some icons do not display correctly, it might be due to the Windows icon cache not updating properly. You can resolve this by clearing the icon cache.

#### Using the `delete_cache.bat` Script

1. **Close All Open Programs**: Before you run the `delete_cache.bat` script, it's essential to close all running applications to prevent any issues.
2. Navigate to the directory where you have the `delete_cache.bat` script.
3. Right-click on the `delete_cache.bat` file and choose "Run as administrator."
4. The script will forcefully close `explorer.exe`, delete the icon cache, and then restart `explorer.exe`.
5. After running the script, check the folders again. The icons should now display correctly.

**Note**: Always proceed with caution when running scripts that modify system processes or files. Ensure you have backups or a system restore point in place. Ive extensively commented the batch for transparency.
