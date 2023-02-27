# Import the required module for text
# to speech conversion
from gtts import gTTS
from moviepy.editor import *

# The text that you want to convert to audio
mytext = 'Welcome to my awesome youtube channel please subscribe and follow and hit the bell notification button !'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Load the audio file
audio = AudioFileClip("welcome.mp3")

# Create the image clip object
image = ImageClip("image.jpg")

# Specify the duration of the new clip to be the duration of the audio clip
duration = audio.duration

# Create a video clip with the image
video = image.set_duration(duration)

# Use set_audio method from image clip to combine the audio with the image
video = video.set_audio(audio)

# Set the FPS to 60
video.fps = 60

# Write the resuling video clip
video.write_videofile("output.mp4")
