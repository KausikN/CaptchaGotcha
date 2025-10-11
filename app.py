"""
Stream lit GUI for hosting CaptchaGotcha
"""

# Imports
import json
import streamlit as st

from Utils import Utils

import CaptchaGen
import CaptchaCrack

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
PATHS = {
    "fonts": "Data/Fonts/",
    "voices": "Data/Voices/",
    "defaults": {
        "save_image": "Data/GeneratedVisualisations/captcha.png",
        "save_audio": "Data/GeneratedVisualisations/captcha.wav",
        "captcha_image": "Data/GeneratedVisualisations/CTest.png"
    }
}
FONT_NAMES = Utils.GetFileNames(Utils.FindFiles(PATHS["fonts"]))

# Util Functions


# UI Functions
def UI_LoadCracker(datatype="image"):
    '''
    UI - Load Cracker
    '''
    USERINPUT_CrackerName = st.selectbox("Select Captcha Cracker", CaptchaCrack.CAPTCHA_CRACKERS[datatype])
    USERINPUT_Cracker = CaptchaCrack.CAPTCHA_CRACKERS[datatype][USERINPUT_CrackerName]

    USERINPUT_Cracker["params"] = {}
    if USERINPUT_Cracker["api_key_required"]:
        USERINPUT_Cracker["params"]["api_key"] = st.text_input(f"Enter API Key for {USERINPUT_CrackerName}")
    
    return USERINPUT_Cracker

# Repo Based Functions
def generate_image_captcha():
    # Title
    st.header("Generate Image Captcha")

    # Load Inputs
    USERINPUT_GeneratorName = st.selectbox("Select Captcha Generator", CaptchaGen.CAPTCHA_GENERATORS["image"])
    USERINPUT_text = st.text_area("Enter Captcha Text", "Hello World!")
    USERINPUT_fonts = st.multiselect("Select Font", FONT_NAMES, default=FONT_NAMES)

    # Process Inputs
    if not st.button("Generate"): return
    USERINPUT_Generator = CaptchaGen.CAPTCHA_GENERATORS["image"][USERINPUT_GeneratorName]
    FONT_PATHS = [PATHS["fonts"] + f + ".ttf" for f in USERINPUT_fonts]
    USERINPUT_Generator["func"](text=USERINPUT_text, out_path=PATHS["defaults"]["save_image"], font_paths=FONT_PATHS)

    # Display Outputs
    st.markdown("Generated Image Captcha")
    st.image(PATHS["defaults"]["save_image"], use_container_width=True, clamp=True)

def generate_audio_captcha():
    # Title
    st.header("Generate Audio Captcha")

    # Load Inputs
    USERINPUT_GeneratorName = st.selectbox("Select Captcha Generator", CaptchaGen.CAPTCHA_GENERATORS["audio"])
    USERINPUT_text = st.text_area("Enter Captcha Text", "Hello World!")

    # Process Inputs
    if not st.button("Generate"): return
    USERINPUT_Generator = CaptchaGen.CAPTCHA_GENERATORS["audio"][USERINPUT_GeneratorName]
    USERINPUT_Generator["func"](text=USERINPUT_text, out_path=PATHS["defaults"]["save_audio"])#, voicedir=PATHS["voices"])

    # Display Outputs
    st.markdown("Generated Audio Captcha")
    st.audio(PATHS["defaults"]["save_audio"])
    
def crack_image_captcha():
    # Title
    st.header("Crack Image Captcha")

    # Load Inputs
    USERINPUT_Cracker = UI_LoadCracker("image")
    USERINPUT_ImageData = st.file_uploader("Upload Captcha Image", type=["jpg", "jpeg", "png"])
    if USERINPUT_ImageData is None: USERINPUT_ImageData = open(PATHS["defaults"]["captcha_image"], "rb").read()
    else: USERINPUT_ImageData = USERINPUT_ImageData.read()
    st.image(USERINPUT_ImageData)

    # Process Inputs
    if not st.button("Crack"): return
    CrackedData = USERINPUT_Cracker["func"](USERINPUT_ImageData, **USERINPUT_Cracker["params"])

    # Display Outputs
    st.markdown("Cracked Data")
    st.write(CrackedData)

#############################################################################################################################
# Run Code
if __name__ == "__main__":
    main()