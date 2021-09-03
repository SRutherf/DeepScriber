import logging
import shutil
import subprocess
from typing_extensions import runtime
from musdl import OnlineScore

"""
TODO: 
scrape musescore for public domain songs.  Extract the id for naming and add the url to a list for downloading

for now let's just read a list of urls until scraper is done

add a function that sorts the list of urls.  Output one file with downloadable files and one file with lameo files

add a timeout to the musdl.py url get.  without it, scores not in the dataset will take forever to fail
 with self.session.get(mscz_cid_url, timeout=10) as res:

use classicmans musescore account for downloads.  high quality and public domain.  Currently have all pages until page 4 in the list
"""

# VARS
_log = logging.getLogger('fileDownloader')

MSCORE_EXE = shutil.which('musescore3') or shutil.which('musescore')

msczFolder = 'scores/mscz/'
midFolder = 'scores/mid/'
mxlFolder = 'scores/mxl/' 
pdfFolder = 'scores/pdf/' 

msczExt = '.mscz'
midExt = '.mid'
mxlExt = '.mxl'
pdfExt = '.pdf'

scores = 'webscraper/urls/list.txt'
goodScores = 'webscraper/urls/goodlist.txt'
badScores = 'webscraper/urls/naughtylist.txt'

# FUNCTIONS
def main():
    scorelist = readMusescoreList(scores)
    downloadFiles(scorelist)

def readMusescoreList(path):
    list = {} #{id : url}
    with open(path) as file:
        while (line := file.readline().rstrip()):
            split = line.split('/')
            for i in range(len(split)):
                if split[i] == 'scores':
                    list[split[i+1]] = line
    return list

def writeMusescoreList(url, list):
    file = open(list, 'r+')
    if url not in file.read():
        file.write(url+'\n')
    file.close()

def downloadFiles(dicts):
    for key in dicts:
        msczFile = msczFolder + str(key) + msczExt
        midFile = midFolder + str(key) + midExt
        mxlFile = mxlFolder + str(key) + mxlExt
        pdfFile = pdfFolder + str(key) + pdfExt

        #get the file and save locally
        try:
            score = OnlineScore(dicts[key])
        except:
            writeMusescoreList(dicts[key], badScores)
            print(key + " not available in the dataset")
        else:
            writeMusescoreList(dicts[key], goodScores)
            score.export('mscz', msczFile)

            # save as mid and mxl files
            try:
                subprocess.run(
                    [MSCORE_EXE, msczFile, '-o', midFile], 
                    check=True,
                )
                subprocess.run(
                    [MSCORE_EXE, msczFile, '-o', mxlFile], 
                    check=True,
                )
                subprocess.run(
                    [MSCORE_EXE, msczFile, '-o', pdfFile], 
                    check=True,
                )

            except subprocess.CalledProcessError as e:
                _log.error(f'failed to export: {e.output}')
                raise
            
            finally: 
                print('Finished downloading score with id: ' + key)

main()