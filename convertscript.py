import os
from readConfig import returnValue
if 'onnx' in returnValue('conversion_method'):
    onnx=True
    pnnx=False
if 'pnnx' in returnValue('conversion_method'):
    pnnx=True
    onnx=False
if 'True' in returnValue('fp16'):
    fp16=1
else:
    fp16=0
os.system('git clone https://github.com/hzwer/Practical-RIFE')
os.system('rm -rf Practical-RIFE/requirements.txt')
os.system('cp -r Practical-RIFE/* .')
os.system('sudo apt install python3-pip -y')

try:
    os.system('pip install onnxsim onnxconverter_common torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1')
except:
    os.system('pip install onnxsim onnxconverter_common torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1')
os.system('wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/0.png && wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/2.png')

try:
    os.system('pip install -r requirements.txt')
except:
    os.system('pip install -r requirements.txt')
os.system('python3 modify_train_log.py')
os.system('mv train_log/ train_log_backup/')
os.system('mv train_log_export/ train_log/')
try:
    os.system('python3 inference_img.py  --img 0.png 2.png --exp 1')
except:
    pass
os.system('mv train_log/ train_log_export/') 
os.system('mv train_log_backup/ train_log/')
os.system('chmod +x ncnnoptimize')
os.system('chmod +x onnx2ncnn')
os.system('chmod +x pnnx')
os.system('sudo apt install libprotobuf17 -y')
if onnx:
    os.system('onnxsim rife.onnx rife-sim.onnx')
    os.system('./onnx2ncnn  rife-sim.onnx flownet-sim.param flownet-sim.bin')
    if fp16 == 1:
        os.system('./ncnnoptimize flownet-sim.param flownet-sim.bin flownet.param flownet.bin 65536 ')#the 65536 converts it to fp16
    else:
        os.system('./ncnnoptimize flownet-sim.param flownet-sim.bin flownet.param flownet.bin ')
    

if pnnx:
    
    os.system(f'./pnnx rife.pt inputshape=[1,3,256,256],[1,3,256,256],[1] fp16={fp16} optlevel=2 ncnnparam=flownet.param ncnnbin=flownet.bin')
    
os.system('python3 fix_param_file.py')
