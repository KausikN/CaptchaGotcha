'''
Captcha generation tools
'''

# Imports
import os
import captcha
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from tqdm import tqdm

from Utils.Utils import *

# Main Functions
# Generate Functions
def GenerateAudioCaptcha(text, out_path, voicedir=None):
    audio = AudioCaptcha(voicedir=voicedir)
    # data = audio.generate(text)
    audio.write(text, out_path)

def GenerateImageCaptcha(text, out_path, font_paths=["Data/Fonts/Sans.ttf"]):
    image = ImageCaptcha(fonts=font_paths)
    # data = image.generate(text)
    image.write(text, out_path)

# Driver Code