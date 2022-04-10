'''
Captcha cracking tools
'''

# Imports
import captcha_solver
from captcha_solver import CaptchaSolver

# Main Functions
def Crack_TwoCaptcha(api_key, img_path='captcha.png'):
    solver = CaptchaSolver('twocaptcha', api_key=api_key)
    raw_data = open(img_path, 'rb').read()
    print(solver.solve_captcha(raw_data))

def Crack_RUCaptcha(api_key, img_path='captcha.png'):
    solver = CaptchaSolver('rucaptcha', api_key=api_key)
    raw_data = open(img_path, 'rb').read()
    print(solver.solve_captcha(raw_data))

def Crack_BrowserCaptcha(img_path='captcha.png'):
    solver = CaptchaSolver('browser')
    raw_data = open(img_path, 'rb').read()
    print(solver.solve_captcha(raw_data))

def Crack_AntigateCaptcha(api_key, img_path='captcha.png'):
    solver = CaptchaSolver('antigate', api_key=api_key)
    raw_data = open(img_path, 'rb').read()
    print(solver.solve_captcha(raw_data))

# Driver Code
# # Params
# path = "Examples/Captcha_1.jpg"
# api_key = ""
# # Params

# # RunCode
# Crack_BrowserCaptcha(img_path=path)