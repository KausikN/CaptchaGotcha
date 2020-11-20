'''
Captcha generation tools
'''

# Imports
import captcha
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

# Main Functions
def GenerateAudioCaptcha(text='1234', out_path='audioCAPTCHA.wav', voicedir='Data/Voices/'):
    audio = AudioCaptcha(voicedir=voicedir)
    data = audio.generate(text)
    audio.write(text, out_path)

def GenerateImageCaptcha(text='1234', out_path='imageCAPTCHA.png', font_paths=['Data/Fonts/Calibri.ttf', 'Data/Fonts/Sans.ttf']):
    image = ImageCaptcha(fonts=font_paths)
    data = image.generate(text)
    image.write(text, out_path)

# Driver Code
