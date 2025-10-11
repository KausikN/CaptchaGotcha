"""
Captcha generation tools
"""

# Imports
import os
import captcha
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

from Utils.Utils import *

# Main Functions
# Generate Functions
def GenerateCaptcha_Image(text, out_path, font_paths=["Data/Fonts/Sans.ttf"]):
    '''
    Generate Captcha - Image
    '''
    image = ImageCaptcha(fonts=font_paths)
    # data = image.generate(text)
    image.write(text, out_path)

def GenerateCaptcha_Audio(text, out_path, voicedir=None):
    '''
    Generate Captcha - Audio
    '''
    audio = AudioCaptcha(voicedir=voicedir)
    # data = audio.generate(text)
    audio.write(text, out_path)

# Main Vars
CAPTCHA_GENERATORS = {
    "image": {
        "Python Captcha": {
            "func": GenerateCaptcha_Image
        }
    },
    "audio": {
        "Python Captcha": {
            "func": GenerateCaptcha_Audio
        }
    }
}

# Run Code