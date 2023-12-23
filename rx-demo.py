from afskmodem import DigitalReceiver
from afskmodem import DigitalModes
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


text_to_speech("starting")
text_to_speech("Send me the screeches and I will reply with the speeches")


receiver = DigitalReceiver(DigitalModes.afsk300())
print("AFSKmodem RX Demo")
while(True):
    print("Waiting for message...\n")
    while(True):
        try:
            rxData, errorCount = receiver.rx()
            if(rxData != b""):
                print("Transmission received. " + str(errorCount) + " errors corrected.")
                print(rxData.decode("ascii", "ignore"))
                print("\nDone. (CTRL-C to exit)")
                message = rxData.decode("ascii", "ignore").replace('-', '')

                text_to_speech(rxData.decode(message))

        except:
            print("there was an error...just continue")