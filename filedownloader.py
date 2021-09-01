import logging
import shutil
import subprocess
from musdl import OnlineScore

"""
TODO: 
scrape musescore for public domain songs.  Extract the id for naming and add the url to a list for downloading

for now let's just read a list of urls until scraper is done
"""

# VARS
_log = logging.getLogger('fileDownloader')

MSCORE_EXE = shutil.which('musescore3') or shutil.which('musescore')

msczFolder = 'scores/mscz/'
midFolder = 'scores/mid/'
mxlFolder = 'scores/mxl/' 

msczExt = '.mscz'
midExt = '.mid'
mxlExt = '.mxl'

classicalScores = 'webscraper/urls/classical.txt'
jazzScores = 'webscraper/urls/jazz.txt'

# FUNCTIONS
def main():
    classicalList = getMusescoreList(classicalScores)
    jazzList = getMusescoreList(jazzScores)
    downloadFiles(classicalList)
    #downloadFiles(jazzList)

def getMusescoreList(path):
    list = {} #{id : url}
    with open(path) as file:
        while (line := file.readline().rstrip()):
            split = line.split('/')
            for i in range(len(split)):
                if split[i] == 'scores':
                    list[split[i+1]] = line
    return list

def downloadFiles(dicts):
    for key in dicts:
        msczFile = msczFolder + str(key) + msczExt
        midFile = midFolder + str(key) + midExt
        mxlFile = mxlFolder + str(key) + mxlExt

        print('downloading score: ' + key + ' with url ' + dicts[key])

        #get the file and save locally
        score = OnlineScore(dicts[key])
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

        # figure out a way to catch this and move on to the next thing in the loop in case one of them errors out
        except subprocess.CalledProcessError as e:
            _log.error(f'failed to export: {e.output}')
            raise
        
        # move on to next id in the field
        finally: 
            print('Finished downloading score with id: ' + key)

main()