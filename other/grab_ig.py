#!/usr/bin/env python3

import os
import sys 
import instaloader
from tqdm import tqdm

DIR = '.'
os.chdir(DIR)

name = sys.argv[1]
L = instaloader.Instaloader(quiet = True, post_metadata_txt_pattern = '', save_metadata = False)

if name != '1':
    p = instaloader.Profile.from_username(L.context, name)
    L = instaloader.Instaloader(post_metadata_txt_pattern = '', save_metadata = False)
    for iterator in p.get_posts():
        L.download_post(iterator, p.username)
else:
    for name in os.listdir():
            if name[:-2] != 'py':
                p = instaloader.Profile.from_username(L.context, name)
                L = instaloader.Instaloader(post_metadata_txt_pattern = '', save_metadata = False)
                for iterator in p.get_posts():
                    L.download_post(iterator, p.username)
