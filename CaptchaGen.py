'''
Captcha generation tools
'''

# Imports
import os
import captcha
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from tqdm import tqdm

from Utils import Utils

# Main Functions
# Generate Functions
def GenerateAudioCaptcha(text='1234', out_path='audioCAPTCHA.wav', voicedir='Data/Voices/'):
    audio = AudioCaptcha(voicedir=voicedir)
    data = audio.generate(text)
    audio.write(text, out_path)

def GenerateImageCaptcha(text='1234', out_path='imageCAPTCHA.png', font_paths=['Data/Fonts/Calibri.ttf', 'Data/Fonts/Sans.ttf']):
    image = ImageCaptcha(fonts=font_paths)
    data = image.generate(text)
    image.write(text, out_path)

# # Driver Code
# # Params
# fonts_path = 'Data/Fonts/'
# voices_path = 'Data/Voices/'

# fonts = Utils.FindFiles(fonts_path)
# print("Found", len(fonts), "fonts.")

# voices = Utils.FindFiles(voices_path)
# print("Found", len(voices), "voices.")
# # Params

# # Image Generation
# n_gen = 5
# gen_path = 'Data/Generated/'
# text = 'Kausik'

# startIndex = len(Utils.FindFiles(gen_path)) + 1
# for i in tqdm(range(n_gen)):
#     path = os.path.join(gen_path, str(startIndex + i) + ".png")
#     GenerateImageCaptcha(text, path, font_paths=fonts)