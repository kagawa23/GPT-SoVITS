# -*- coding:utf-8 -*-

import sys,os,traceback
dir=sys.argv[1]
# opt_name=dir.split("\\")[-1].split("/")[-1]
opt_name=os.path.basename(dir)

import whisper

opt=[]
prompt=''
model = whisper.load_model("small")
for name in os.listdir(dir):
    try:
        audio_path="%s/%s"%(dir,name)
        result = model.transcribe(audio_path,verbose=True,initial_prompt=prompt)
        text = result["text"]
        language = result['language']
        opt.append("%s/%s|%s|%s|%s"%(dir,name,opt_name,language,text))
    except:
        print(traceback.format_exc())

opt_dir="output/asr_opt"
os.makedirs(opt_dir,exist_ok=True)
with open("%s/%s.list"%(opt_dir,opt_name),"w",encoding="utf-8")as f:f.write("\n".join(opt))

