# export API key
# Linux/MacOs
# export ELEVENLABS_API_KEY="c409bdb0792a210474b78f593fcfbb90da6ce9ec45b7746c4eb34977432bee7e"
# Windows
# set ELEVENLABS_API_KEY="c409bdb0792a210474b78f593fcfbb90da6ce9ec45b7746c4eb34977432bee7e"

# INSTALL PYTHON PLAYSOUND BEFORE USING WITH THE FOLLOWING COMMAND
# pip install playsound==1.2.2

# ALSO INSTALL ELEVENLABS PACKAGE WITH THE FOLLOWING COMMANDS
# pip install elevenlabs
# npm install @elevenlabs/elevenlabs-js
from elevenlabs import ElevenLabs, save #set_api_key, generate 
from pathlib import Path
import os
os.environ["ELEVENLABS_API_KEY"] = "c409bdb0792a210474b78f593fcfbb90da6ce9ec45b7746c4eb34977432bee7e"



def getVoice(filename):

    client = ElevenLabs()

    file_content = Path(filename).read_text()
    # with open("test.txt", "r", encoding="utf-8") as f:
    #     text = f.read()

    audio = client.text_to_speech.convert(
        voice_id="DLsHlh26Ugcm6ELvS0qi",
        output_format="mp3_44100_128",
        model_id="eleven_multilingual_v2",
        text=file_content
    )

    save(audio, "output.mp3")
    print("Audio saved")

    import playsound
    playsound.playsound("output.mp3")

getVoice("test.txt")