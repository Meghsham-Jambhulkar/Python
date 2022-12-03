import requests
import re
from urllib.parse import urlparse
from sys import *
import os

def is_downloadable(url):
    h = requests.head(url,allow_redirects = True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def Downloader(url):
    allowed = is_downloadable(url)

    if allowed:
        try:
            res = requests.get(url , allow_redirects = True)
            res.raise_for_status()
            filename = get_filename_from_cd(url)
            fd = open(filename ,"wb")

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as E :
            return False
    else:
        return False
    


def main():
    print("----------Marvellous Infosystem Automations----------")

    print("Automation Script started with name : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1]== "-H"):
            print("Help : This script is used to download images with provided url ")
            exit()

        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Provide 1 url of downloadable image as input")
            exit()

    url = 'https://wallpaperaccess.com/full/17350.jpg'

    result = Downloader(url)

    if result:
        print("File Successfully Downloaded ")
    else:
        print("Failed To Download")

        
if __name__ == "__main__":
    main()
