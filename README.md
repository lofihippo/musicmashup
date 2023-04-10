# Music Mashup
Python based application that uses ffmpeg to import audio files in mp3 format, cut each file, then combine each cut or uncut audio file into a finalized audio file.

to run:
do cmd in your address bar in the file view then type:

pip install pydub

after, click in the address bar for the folder mp3_song_mashup_project and type "cmd" without quotes and hit enter. 
Once the command line pops up, type python main.py to run the app

Please note that you will have to have ffmpeg installed to work (which may have been installed previously for your system) If you need to install it, follow the steps below:
(also as part of the .7zip file)

___

Follow these steps to install ffmpeg on Windows 10:
    Download the ffmpeg package for Windows from the official website: https://www.ffmpeg.org/download.html. Choose the "Windows builds" option from the download section.

    Once downloaded, extract the contents of the zip archive to a folder. For example, you can extract it to C:\ffmpeg.

    Add the ffmpeg executable to your system's PATH:
    a. Press the Windows key, type "Environment Variables" and open "Edit the system environment variables".
    b. Click the "Environment Variables..." button near the bottom right corner of the System Properties window.
    c. In the "System Variables" section, find the variable named Path and click "Edit...".
    d. In the "Edit environment variable" window, click "New" and add the path to the bin folder inside the extracted ffmpeg folder. 
	For example, if you extracted ffmpeg to C:\ffmpeg, add C:\ffmpeg\bin to the Path variable.
    e. Click "OK" to save your changes and close all open windows.

    Restart your command prompt or any other running terminals to ensure the new PATH settings take effect. You can test if the ffmpeg installation was successful by running the following command in a new command prompt:

    ffmpeg -version

    If the installation was successful, this command should display the version information for ffmpeg.
Once ffmpeg is installed and added to your system's PATH, you should be able to run your main.py script without encountering the error.
