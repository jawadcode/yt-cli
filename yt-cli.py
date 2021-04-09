#!/usr/bin/env python3

import os
import sys
import time
import shutil
import subprocess
from typing import List, Tuple
from PIL import Image


def main():
    url = get_flag('url')
    if url == '':
        print('Usage: ./yt-cli.py {-u/--url} <url>')
        return
    
    if os.path.isdir('./images') or os.path.isdir('./videos'):
        print('Please make sure that there are no subdirectories in the working directory named "videos" or "images", as the script will delete them recursively.')
        return

    frames = get_frames(url)

    print('\x1b[38;2;0;128;0mStarting video...\x1b[0m\n')
    time.sleep(0.5)
    draw(frames)


def draw(frames: List[List[Tuple[int, int, int]]]):
    print('\x1b[2J')
    for fr in frames:
        frame = ''
        for i in range(0, 4608):
            val = fr[i]
            red, green, blue = val
            frame += f'\x1b[38;2;{red};{green};{blue}m█\x1b[0m'

            # Speedy modulo :)
            if not ((i + 1) & 127):
                frame += '\n'

        time.sleep(0.08)
        print('\x1b[2J')
        print(frame)


def get_frames(url: str) -> List[List[Tuple[int, int, int]]]:
    shutil.rmtree('./images', ignore_errors=True)
    shutil.rmtree('./video', ignore_errors=True)
    os.mkdir('./images')
    os.mkdir('./video')

    print(
        '\x1b[38;2;0;128;0mDownloading video and converting...\x1b[0m',
    )
    subprocess.run([
        'youtube-dl',
        '--no-continue',
        '--format', 'worst',
        '--external-downloader', 'ffmpeg',
        '--external-downloader-args',
        '-s 128x36 -r 10 -pix_fmt bgr24 ./images/frame_%04d.bmp',
        '--output', './video/%(id)s.%(ext)s',
        url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print('\x1b[38;2;0;128;0mReading frames...\x1b[0m')
    frames = []
    for name in sorted(os.listdir('./images')):
        with Image.open(f'./images/{name}', 'r') as f:
            frames.append(list(f.getdata()))

    shutil.rmtree('./images')
    shutil.rmtree('./video')
    return frames


def get_flag(flag: str) -> str:
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '--' + flag or sys.argv[i] == '-' + flag[0]:
            return sys.argv[i + 1]

    return ''


if __name__ == '__main__':
    main()
