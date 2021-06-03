"""
Stream lit GUI for hosting CaptchaGotcha
"""

# Imports
import streamlit as st
import json

import CaptchaGen

# Main Vars
config = json.load(open('./StreamLitGUI/UIConfig.json', 'r'))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
        tuple(
            [config['PROJECT_NAME']] + 
            config['PROJECT_MODES']
        )
    )
    
    if selected_box == config['PROJECT_NAME']:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(' ', '_').lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config['PROJECT_NAME'])
    st.markdown('Github Repo: ' + "[" + config['PROJECT_LINK'] + "](" + config['PROJECT_LINK'] + ")")
    st.markdown(config['PROJECT_DESC'])

    # st.write(open(config['PROJECT_README'], 'r').read())

#############################################################################################################################
# Repo Based Vars
SAVEPATH_DEFAULT_IMAGE = 'captcha.png'
SAVEPATH_DEFAULT_AUDIO = 'captcha.wav'
FONTS_PATH = 'Data/Fonts/'
VOICES_PATH = 'Data/Voices/'

FONT_NAMES = CaptchaGen.Utils.GetFileNames(CaptchaGen.Utils.FindFiles(FONTS_PATH))

# Util Functions


# Repo Based Functions
def generate_image_captcha():
    # Title
    st.header("Generate Image Captcha")

    # Load Inputs
    USERINPUT_text = st.text_area("Enter Captcha Text", "Hello World!")
    USERINPUT_fonts = st.multiselect("Select Font", FONT_NAMES, default=FONT_NAMES)

    # Process Inputs
    if st.button("Regenerate"):
        pass
    font_paths = []
    for f in USERINPUT_fonts:
        font_paths.append(FONTS_PATH + f + ".ttf")
    CaptchaGen.GenerateImageCaptcha(text=USERINPUT_text, out_path=SAVEPATH_DEFAULT_IMAGE, font_paths=font_paths)

    # Display Outputs
    st.markdown("Generated Image Captcha")
    st.image(SAVEPATH_DEFAULT_IMAGE, use_column_width=True, clamp=True)

def generate_audio_captcha():
    # Title
    st.header("Generate Audio Captcha")

    # Load Inputs
    USERINPUT_text = st.text_area("Enter Captcha Text", "Hello World!")

    # Process Inputs
    if st.button("Regenerate"):
        pass
    CaptchaGen.GenerateAudioCaptcha(text=USERINPUT_text, out_path=SAVEPATH_DEFAULT_AUDIO)#, voicedir=VOICES_PATH)

    # Display Outputs
    st.markdown("Generated Audio Captcha")
    st.audio(SAVEPATH_DEFAULT_AUDIO)
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()