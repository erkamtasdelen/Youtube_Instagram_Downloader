# Video Downloader Application

## Overview
This application automates the downloading of videos from YouTube Shorts and Instagram accounts based on a predefined account list. It also maintains a log of downloaded videos to avoid duplicates. The program is written in Python and uses the `yt_dlp` library for YouTube videos and the `instaloader` library for Instagram posts.

---

## Features
- Download videos from YouTube Shorts channels.
- Download videos from Instagram accounts.
- Categorize videos based on predefined categories.
- Automatically skip already downloaded videos using a tracking log.
- Flexible downloading options, including:
  - Downloading videos from all accounts.
  - Downloading videos from specific accounts.
  - Downloading videos based on categories.
- Configurable video download limit per session.

---

## Requirements
### Libraries
The following Python libraries are required:
- `yt_dlp`
- `instaloader`
- `os`

Install them using pip:
```bash
pip install yt-dlp instaloader
```

### Folder Structure
Ensure the following folder structure exists before running the program:
```
.
├── Genral_Infos
│   ├── ACCOUNTLAR.txt   # List of accounts with their platforms and categories
│   └── Downloaded_Videos.txt  # Log of downloaded videos
├── Videos               # Folder to store downloaded YouTube videos
└── Instagram            # Folder to store downloaded Instagram posts
```

---

## Input Files
### `ACCOUNTLAR.txt`
A list of accounts to download videos from. Each account is listed on a new line in the following format:
```
<account_username>
<platform> ("Youtube" or "Instagram")
<category>
```
Example:
```
the_blue_magazine
Youtube
nature

heyppme
Instagram
travel
```

### `Downloaded_Videos.txt`
This file tracks the video IDs of previously downloaded videos. Each video ID is stored on a new line.

---

## Usage
### Running the Program
Execute the Python script:
```bash
python script_name.py
```
### Interaction
1. At the start, you will see a list of available accounts and categories, along with an option to download from all accounts.
2. Enter your choice:
   - Type `ALL` to download videos from all accounts.
   - Enter the index of a specific account to download videos from that account.
   - Enter the index of a category to download videos from accounts in that category.
3. The program will automatically download videos and save them to their respective folders.

### Configuration
You can modify the maximum number of videos to download per session by changing the `Download_Limit` variable in the script:
```python
Download_Limit = 30
```

---

## Code Breakdown
### Main Components
- **`Youtube_Side` Class:**
  Handles video downloading from YouTube Shorts.

- **`Instagram_Side` Class:**
  Handles video downloading from Instagram accounts.

- **`PullIt`, `SaveIt`, `AskIt` Functions:**
  Manage the `Downloaded_Videos.txt` log to prevent duplicate downloads.

- **`ClassedAccounts` Function:**
  Groups accounts from `ACCOUNTLAR.txt` for easy selection.

- **`ALL`, `Sellected`, `FoundKtgs` Functions:**
  Handle different download options: all accounts, selected accounts, or accounts by category.

---

## Error Handling
The program handles errors gracefully, such as:
- Missing or invalid account information.
- Connection issues during video downloading.
- Permission errors when saving files.

Errors are printed to the console for debugging.

---

## Contribution
Feel free to fork this repository and contribute by submitting pull requests. Ensure your code follows best practices and includes appropriate error handling.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Instaloader](https://instaloader.github.io/)

