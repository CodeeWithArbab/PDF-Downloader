# PDF Downloader Script
# This script downloads a PDF file from a given URL and provides a progress bar during the download process.
# Dependencies:
# requests: For making HTTP requests to download files.
# progressbar2: For displaying a progress bar during the download process.
# os: For handling file paths and directories.
# Developer: Arbab Gul
# Date: 06/06/2025
# Thanks for using this script! If you have any issues or suggestions, feel free to reach out.


import requests
from urllib.parse import urlparse
import os
import progressbar

def PDFExtact(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    if len(path_parts) < 2 or not path_parts[-1].lower().endswith('.pdf'):
        print("❌ Invalid URL format or not a PDF file")
        exit(0)
    return path_parts[-1].replace('%20','_')  if path_parts and path_parts[-1].lower().endswith('.pdf') else None

def PDFDown(url,save_path):

    try:
        response = requests.get(url, stream=True)    
        response.raise_for_status()

        file_size = int(response.headers.get('content-length', 0))

        widgets = [
            'Downloading: ',
            progressbar.Percentage(),
            ' ',
            progressbar.Bar(marker='█', left='[', right=']'),
            ' ',
            progressbar.ETA(),
            ' ',
            progressbar.FileTransferSpeed()
        ]
        bar = progressbar.ProgressBar(max_value=file_size, widgets=widgets)

        with open(save_path, 'wb') as f:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        bar.update(downloaded)
                bar.finish()

        print(f"\n✅ PDF saved to: {os.path.abspath(save_path)}")
    except Exception as e:
        print(f"\n❌ Download failed: {e}")

def main():
    print(r"""
    ██████╗ ██████╗ ███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║  ██║█████╗      ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
    ██╔═══╝ ██║  ██║██╔══╝      ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
    ██║     ██████╔╝██║         ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
    ╚═╝     ╚═════╝ ╚═╝         ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                This script downloads a PDF file from a given URL.
                                                Auther: Arbab Gul
                                                  Version: v2.0
    """)
    
    url = input("\nEnter the url of the PDF file you want to download: ").strip()
    url_data = PDFExtact(url)
    pdf_name = input(f"Enter Custom PDF name (default: {url_data}): ").strip()

    if pdf_name != '':
        if not pdf_name.lower().endswith('.pdf'):
            pdf_name += '.pdf'            
        PDFDown(url, pdf_name)
    else:
        PDFDown(url, url_data)

if __name__ == "__main__":
    main()
