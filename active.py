
#!/bin/bash env python3

import concurrent.futures
import requests
import warnings
from colorama import Fore, Style
import sys

warnings.filterwarnings("ignore", message=".*Unverified HTTPS request.*")

def main(url):

   try:
     r=requests.get(url,verify=False)
     if r.status_code==200:
        save=open('output.txt', 'a').write(r.url+'\n')

   except:
   
    return  ''

def threads(url):
   with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    futures = [executor.submit(main, url) for url in url]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
        continue


if __name__ =='__main__':
   with open(sys.argv[1],'r') as file:
     
      url=[files.strip() for files in file.readlines()]

   threads(url)
