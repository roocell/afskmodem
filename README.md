# hunt
recorded a wav file by running tx-demo.py  
repeated message with 15sec gaps in between (15sec is as longer as the message the receiving device speech takes)  
run rx-demo.py as a service to constantly listen to modem audio signals.  
once detected, it will take the decoded messages and use gtts to speak it.  
the receiving device will be in parts that need to be assembled. (battery, raspi, speaker, cords)  


# gTTS
sudo python3 gtts-demo.py

# create out.wav using afskmodem
copy this to /static
```
sudo python3 tx-demo.py
```
# convert to video with lossless (flac) audio
Was going to upload to youtube - but decided on webpage instead
```
ffmpeg -loop 1 -i elf.jpg -i out.wav -c:v libx264 -tune stillimage -c:a flac -b:a 192k -pix_fmt yuv420p -shortest file.mp4
```

# instead just hosted a webpage with a wav player.
run as a service
```
[Unit]
Description=modemrx
After=network-online.target
[Service]
ExecStart=python3 /home/pi/afskmodem/rx-demo.py
WorkingDirectory=/home/pi/afskmodem
Restart=always
RestartSec=0

[Install]
WantedBy=multi-user.target
```
