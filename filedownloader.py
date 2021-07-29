import logging
import shutil
import subprocess
from musdl import OnlineScore

_log = logging.getLogger("fileDownloader")

MSCORE_EXE = shutil.which("musescore3") or shutil.which("musescore")

msczFolder = 'scores/mscz/'
midFolder = 'scores/mid/'
mxlFolder = 'scores/mxl' 

msczExt = '.mscz'
midExt = '.mid'
mxlExt = '.mxl'

# make a function that gets the musescore id for the sheet music so we can make that the id

# look into openscore from musescore for downloading junk that i can get for free


#loop start
# variables
id = 1
msczFile = msczFolder + str(id) + msczExt
midFile = midFolder + str(id) + midExt
mxlFile = mxlFolder + str(id) + mxlExt

#get the file and save locally
score = OnlineScore('https://musescore.com/user/101554/scores/117279')
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

# figure out a way to catch this and move on to the next thing in the loop
except subprocess.CalledProcessError as e:
    _log.error(f"failed to export: {e.output}")
    raise

finally: 
    # move on to next id in the field
    print('completed')