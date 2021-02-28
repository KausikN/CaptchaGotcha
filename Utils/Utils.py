'''
Util functions for CaptchaGotcha
'''

# Imports
import os

# Main Functions
def FindFiles(path):
    files = []
    for f in os.listdir(path):
        files.append(os.path.join(path, f))
    return files

# Driver Code