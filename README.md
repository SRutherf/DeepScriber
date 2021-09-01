# Setting up locally

1. Get VS Code
2. Download Python 3.8.x and install (3.8 for numpy to work)
4. Install python extension in vs code (ms-python.python)
5. upgrade pip
	py -m pip install --upgrade pip
6. install tensorflow
	py -m pip install tensorflow
7. (Optional) Install GPU features
	1. Update GPU drivers
	2. Download the CUDA toolkit and cuDNN sdk
	3. Copy cuDNN files into CUDA directory (https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)
8. Install spleeter
	pip install ffmpeg-python (ffmpeg seemed to cause an error, might need to pip uninstall/install again if getting no attribute probe errors)
	download libsndfile (http://www.mega-nerd.com/libsndfile/#Download)
	pip install spleeter
	download ffmpeg package and add to path (https://www.ffmpeg.org/)
	use command 'py -m spleeter separate input.mp3 -p spleeter:5stems -o output' in command line to run

9.  Section for Sheet-Midi-Sheet setup
	1. Install musescore command line tools (https://musescore.org/en/node/274034)
	2. Download musdl library to dowload musescore sheetmusic (https://pypi.org/project/musdl/)
	3.  
10. 
11. 

# Setting up with Docker

## Run Docker Container
1. install docker
2. install tensorflow docker image (docker pull tensorflow)
3. run the container
	- (CPU only) docker run -it --rm tensorflow/tensorflow bash
	- (GPU only) docker run -it --rm --runtime=nvidia tensorflow/tensorflow:latest-gpu python

# Tensorflow GPU logging
## To ignore add the following lines
	import os
	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
	import tensorflow as tf

	0 = all messages are logged (default behavior)
	1 = INFO messages are not printed
	2 = INFO and WARNING messages are not printed
	3 = INFO, WARNING, and ERROR messages are not printed

# Setting up on mac m1 and jupyter
1. add the link from macbook, then copy the instructions.
https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706
