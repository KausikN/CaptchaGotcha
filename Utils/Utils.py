"""
Util functions for CaptchaGotcha
"""

# Imports
import os

# Main Functions
def FindFiles(path):
    '''
    Find Files
    '''
    files = []
    for f in os.listdir(path):
        files.append(os.path.join(path, f))
    return files

def GetFileNames(paths):
    '''
    Get File Names
    '''
    filenames = []
    for p in paths:
        filenames.append(os.path.splitext(os.path.basename(p))[0])
    return filenames

# Run Code