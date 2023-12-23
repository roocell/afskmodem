

# use gTTS for text-to-speech
sudo python3 gtts-demo.py

# create out.wav using afskmodem
# need to modify afskmodem.py transmit path to produce 'output_file'
sudo python3 tx-demo.py

# convert from wav to mp4 to upload to youtube
# but this is lossy
ffmpeg -loop 1 -i elf.jpg -i out.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest file.mp4

# here's a lossless version
ffmpeg -loop 1 -i elf.jpg -i out.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest file.mp4

ffmpeg -loop 1 -i elf.jpg -i out.wav -c:v libx264 -tune stillimage -preset veryslow -qp 0 -c:a flac output_lossless.mp4
