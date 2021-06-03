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

def GetFileNames(paths):
    filenames = []
    for p in paths:
        filenames.append(os.path.splitext(os.path.basename(p))[0])
    return filenames

# Driver Code