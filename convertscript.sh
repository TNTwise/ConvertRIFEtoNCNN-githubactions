git clone https://github.com/hzwer/Practical-RIFE
rm -rf Practical-RIFE/requirements.txt
cp -r Practical-RIFE/* .
sudo apt install python3-pip -y
pip install onnxsim onnxconverter_common torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 
pip install onnxsim onnxconverter_common torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 --break-system-packages 
wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/0.png && wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/2.png
pip install -r requirements.txt
pip install -r requirements.txt --break-system-packages
python3 modify_train_log.py
mv train_log/ train_log_backup/
mv train_log_export/ train_log/
python3 inference_img.py  --img 0.png 2.png --exp 1 
mv train_log/ train_log_export/ 
mv train_log_backup/ train_log/
chmod +x ncnnoptimize
chmod +x onnx2ncnn

sudo apt install libprotobuf17 -y

onnxsim rife.onnx rife-sim.onnx
./onnx2ncnn  rife-sim.onnx flownet-sim.param flownet-sim.bin
./ncnnoptimize flownet-sim.param flownet-sim.bin flownet.param flownet.bin 65536 #the 65535 converts it to fp16
python3 fix_param_file.py
