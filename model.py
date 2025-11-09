# export API key
# Linux/MacOs
# export ELEVENLABS_API_KEY="c409bdb0792a210474b78f593fcfbb90da6ce9ec45b7746c4eb34977432bee7e"
# Windows
# set ELEVENLABS_API_KEY="c409bdb0792a210474b78f593fcfbb90da6ce9ec45b7746c4eb34977432bee7e"

# INSTALL PYTHON PLAYSOUND BEFORE USING WITH THE FOLLOWING COMMAND
# pip install playsound==1.2.2

# ALSO INSTALL ELEVENLABS PACKAGE WITH THE FOLLOWING COMMAND
# pip install elevenlabs
from elevenlabs import ElevenLabs, save
import os
api_key = os.environ.get('ELEVEN_LABS_API_KEY')


client = ElevenLabs(api_key=api_key)
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

voice_name ="Ms. Walker"

audio = client.text_to_speech.convert(
    voice_id=voice_name,
    model_id="eleven_multilingual_v2",
    text=text
)

save(audio, "output.mp3")
print("Audio saved")

import playsound
playsound.playsound("output.mp3")