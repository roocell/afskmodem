from gtts import gTTS
import os

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('mpg123 ' + speech_file)

message = """
------
This should be a breeze.
But it does not come for free.
Something that freshens the air.
But, on the inside, it’s contents are nowhere.
------"""

message = message.replace('-', '')

text_to_speech(message)