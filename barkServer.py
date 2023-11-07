from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

def createVoice(prompt):
    audio_array = generate_audio(prompt)
    name = generateName("input")
    write_wav("files/"+name+".wav", SAMPLE_RATE, audio_array)



def generateName(input):
    return "test2"