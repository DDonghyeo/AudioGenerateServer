from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

def createVoice(prompt, gender):
    audio_array = generate_audio(prompt)
    name = prompt + "_" + gender

    if(gender == "male"):
        voice_preset = "v2/male"
    elif(gender == "female"):
        voice_preset= "v2/female"
    else:
        return None

    write_wav("files/"+name+".wav", SAMPLE_RATE, audio_array)

