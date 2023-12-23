import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 44100
CHUNK_FRAMES = 1024
RECORD_SECONDS = 5
OUTPUT_FILE = "output.wav"

# Check available audio devices and their indices
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device {i}: {info['name']}")

# Use the desired input device index (replace with your specific index)
desired_input_device_index = 2

# Open an input stream with PortAudio
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=SAMPLE_RATE,
    input=True,
    input_device_index=desired_input_device_index,
    frames_per_buffer=CHUNK_FRAMES
)

# Open a WAV file for writing
wf = wave.open(OUTPUT_FILE, 'wb+')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)

# Record audio and write to the WAV file
print("Recording...")
for _ in range(int(SAMPLE_RATE / CHUNK_FRAMES * RECORD_SECONDS)):
    data = stream.read(CHUNK_FRAMES)
    wf.writeframes(data)

print("Recording complete.")

# Close the input stream and the WAV file
stream.stop_stream()
stream.close()
wf.close()

# Terminate PyAudio
p.terminate()

# # Read and process audio data from the stream (add your processing logic)
# while True:
#     data = stream.read(CHUNK_FRAMES)
#     # Process the audio data as needed
#     print('data')