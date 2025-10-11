"""
Captcha cracking tools
"""

# Imports
import captcha_solver
from captcha_solver import CaptchaSolver

# Main Functions
def CrackCaptcha_TwoCaptcha(raw_data, api_key):
    '''
    Crack Captcha - Two Captcha
    '''
    solver = CaptchaSolver("twocaptcha", api_key=api_key)
    cracked_data = solver.solve_captcha(raw_data)

    return cracked_data

def CrackCaptcha_RUCaptcha(raw_data, api_key):
    '''
    Crack Captcha - RU Captcha
    '''
    solver = CaptchaSolver("rucaptcha", api_key=api_key)
    cracked_data = solver.solve_captcha(raw_data)

    return cracked_data

def CrackCaptcha_BrowserCaptcha(raw_data):
    '''
    Crack Captcha - Browser Captcha
    '''
    solver = CaptchaSolver("browser")
    cracked_data = solver.solve_captcha(raw_data)

    return cracked_data

def CrackCaptcha_AntigateCaptcha(raw_data, api_key):
    '''
    Crack Captcha - Antigate Captcha
    '''
    solver = CaptchaSolver("antigate", api_key=api_key)
    cracked_data = solver.solve_captcha(raw_data)

    return cracked_data

# Main Vars
CAPTCHA_CRACKERS = {
    "image": {
        "Two Captcha Cracker": {
            "func": CrackCaptcha_TwoCaptcha,
            "api_key_required": True
        },
        "RU Captcha Cracker": {
            "func": CrackCaptcha_RUCaptcha,
            "api_key_required": True
        },
        "Browser Captcha Cracker": {
            "func": CrackCaptcha_BrowserCaptcha,
            "api_key_required": False
        },
        "Antigate Captcha Cracker": {
            "func": CrackCaptcha_AntigateCaptcha,
            "api_key_required": True
        }
    }
}

# Run Code
# # Params
# path = "Examples/Captcha_1.jpg"
# api_key = ""
# # Params

# # RunCode
# Crack_BrowserCaptcha(open(img_path, "rb").read())