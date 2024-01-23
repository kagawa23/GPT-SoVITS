# -*- coding:utf-8 -*-

import sys,os,traceback
dir=sys.argv[1]
# opt_name=dir.split("\\")[-1].split("/")[-1]
opt_name=os.path.basename(dir)

import whisper

opt=[]
prompt='以下是普通话的句子'
model = whisper.load_model("small")
for name in os.listdir(dir):
    try:
        audio_path="%s/%s"%(dir,name)
        result = model.transcribe(audio_path, language='zh',verbose=True,initial_prompt=prompt)
        text = result["text"]
        opt.append("%s/%s|%s|ZH|%s"%(dir,name,opt_name,text))
    except:
        print(traceback.format_exc())

opt_dir="output/asr_opt"
os.makedirs(opt_dir,exist_ok=True)
with open("%s/%s.list"%(opt_dir,opt_name),"w",encoding="utf-8")as f:f.write("\n".join(opt))

