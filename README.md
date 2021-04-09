# YT-CLI

A YouTube viewer for the command line

## How to use:

### Prerequisites:

- A "True Colour" capable terminal, run the following command to check (it should output the word "TRUECOLOUR" in orange):
```sh
echo "\x1b[38;2;255;100;0mTRUECOLOR\x1b[0m\n"
```
- [youtube-dl](https://github.com/ytdl-org/youtube-dl#installation) - Downloads the video
- [ffmpeg](https://ffmpeg.org/download.html) - Performs the conversion from video to images
- [pillow](https://pillow.readthedocs.io/en/stable/installation.html) - Used to read the image files

### How to run:

Clone the repository and then cd into the folder and run `./yt-cli.py --url <video url>`. _**Make sure to use it in a directory where there are no sub-directories named `video` or `images` because the script recursively deletes the folders while running**_

## How it works:

The python script uses `youtube-dl` to download the video to `video/` (in the current directory), converts said video to image frames using `ffmpeg` (`.bmp`) in `images/` (in the current directory), loads all of the frames into a List with each element being a List of Tuples which each represent a pixel (using `pillow`). This list of frames is then looped through and each frame is printed out as a string containing unicode block characters (for each pixel) coloured using ANSI escape codes (24 bit colour, works in most modern terminals).

## Demo

[link to video](https://user-images.githubusercontent.com/20072738/114243090-e82d9900-9983-11eb-96f4-aa15d5a29216.mp4)
