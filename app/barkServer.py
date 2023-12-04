from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from transformers import AutoProcessor, BarkModel
import os

# download and load all models
preload_models()

def createVoice(prompt, gender):
    fileName = prompt + "_" + gender
    if check_file_existence("./files/" + fileName + ".wav"):
        print("파일이 이미 존재합니다.")
        return False
    else:
        processor = AutoProcessor.from_pretrained("suno/bark")
        model = BarkModel.from_pretrained("suno/bark")

        if(gender == "male"):
            voice_preset = "v2/ko_speaker_4"
        elif(gender == "female"):
            voice_preset= "v2/ko_speaker_0"
        else:
            return None

        inputs = processor(prompt, voice_preset=voice_preset)

        audio_array = model.generate(**inputs)
        audio_array = audio_array.cpu().numpy().squeeze()    
        

        write_wav("files/" + fileName + ".wav", SAMPLE_RATE, audio_array)

        return True

def check_file_existence(file_name):
    file_path = os.path.join(file_name)
    return os.path.exists(file_path)