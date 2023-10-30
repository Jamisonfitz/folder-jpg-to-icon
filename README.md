
# Folder.jpg to Icon Processor

A Python script that automates the process of setting custom icons for folders based on `folder.jpg` images present within them.

## Features

- **Automated Icon Setting**: Recursively scans the selected directory for `folder.jpg` files and sets them as custom folder icons.
- **ICO Generation**: Automatically creates `.ico` files corresponding to each `folder.jpg`.
- **Refresh Option**: Provides the ability to refresh and update existing icons based on updated `folder.jpg` images.

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
