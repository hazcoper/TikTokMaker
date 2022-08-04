"""
This will be the part that receives the text and generates the speech
"""


# Import the required module for text 
# to speech conversion
from gtts import gTTS
import pyttsx3
import os
from google.cloud import texttospeech
  
# This module is imported so that we can 
# play the converted audio
import os



def generateAudio(myText, name, play=False, select="wavenet"):
    """
    Will generate the audio file for the given text and save it using the given name
    """
    
    if select == "google":
        generateGoogle(myText, name, play)
    elif select == "wavenet":
        generateWaveNEt(myText, name, play)
    else:
        generateSelf(myText, name)


def generateGoogle(myText, name, play=False):

    # Language in which you want to convert
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=myText, lang=language, tld="com", slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"{name}.mp3")
    
    # Playing the converted file
    if play:
        os.system(f"mpg321 {name}.mp3")


def generateSelf(myText, name, play=False):

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    print(voices)

    engine.setProperty("rate", 250)
    engine.say(myText)
    engine.runAndWait()

def generateWaveNEt(myText, name, play=False):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gCloud.json"

    # Instantiates a client

    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=myText)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("female")
    voice = texttospeech.VoiceSelectionParams(
    language_code='en-US',
    name='en-US-Neural2-A',
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(f'{name}.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    # Playing the converted file
    if play:
        os.system(f"mpg321 {name}.mp3")

if __name__ == '__main__':
    generateWaveNEt("THis is a very quick test with a bunch of tea", "output", True)