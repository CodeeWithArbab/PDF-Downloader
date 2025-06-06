# PDF Downloader

A Python script for downloading PDF files from the internet with a visual progress bar.

## Features

- ✔ Downloads PDF files from any valid URL  
- 📊 Displays a progress bar with:
  - Download percentage
  - Visual progress indicator
  - Estimated time remaining
  - Download speed
- ✏ Allows custom naming of downloaded files
- 🔍 Validates URL format and file type
- ✅ Provides clear success/error messages

## Requirements
- Python 3.x
- `requests` library
- `progressbar2` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CodeeWithArbab/PDF-Downloader
```

## Usage
```bash
python pdfdown.py
```

## Example
```bash
$ python pdfdown.py

                                          PDF Downloader 
                             ---------- Download PDF from Internet  ---------
                                 ------- Developed by: Arbab Gul ------- 

Enter the URL of the PDF file you want to download: https://example.com/document.pdf
Enter Custom PDF name (default: document.pdf): my_custom_file.pdf
Downloading:  100% [████████████████████████████████████████] ETA: 00:00:00  1.2MB/s

✅ PDF saved to: /path/to/my_custom_file.pdf
```

## Authors

- [@CodeeWithArbab](https://github.com/CodeeWithArbab)
