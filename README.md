# xmas hunt 2023
recorded a wav file by running tx-demo.py
repeated message with 15sec gaps in between (15sec is as longer as the message the receiving device speech takes)
run rx-demo.py as a service to constantly listen to modem audio signals.
once detected, it will take the decoded messages and use gtts to speak it.
the receiving device will be in parts that need to be assembled. (battery, raspi, speaker, cords)


# use gTTS for text-to-speech
sudo python3 gtts-demo.py

# create out.wav using afskmodem
# need to modify afskmodem.py transmit path to produce 'output_file'
sudo python3 tx-demo.py

# convert from wav to mp4 to upload to youtube
# use flac for lossless (but it's experimental)
ffmpeg -loop 1 -i elf.jpg -i out.wav -c:v libx264 -tune stillimage -c:a flac -b:a 192k -pix_fmt yuv420p -shortest file.mp4

# instead just hosted a webpage with a wav player.

