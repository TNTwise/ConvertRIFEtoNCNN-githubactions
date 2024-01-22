import os
with open (f'flownet.param','r') as f:
    flowparam = f.readlines()
newParamFile = []
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
for iteration,line in enumerate(flowparam):
    #Fix cropping
    if onnx:
        if 'Crop' in line:
            
            if 'splitncnn' in line:
                if 'Pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                    if '-23309=1,0 -23310=1,3 -23311=1,0' in line:                    
                        line = (line.replace('-23309=1,0 -23310=1,3 -23311=1,0','-23309=1,0 -23310=1,2 -23311=1,0'))
            if '-23309=1,1 -23310=1,4 -23311=1,0' in line:
                if 'splitncnn' in line:
                    if 'Pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                        line = (line.replace('-23309=1,1 -23310=1,4 -23311=1,0','-23309=1,2 -23310=1,4 -23311=1,0'))
            if '-23309=1,1 -23310=1,2 -23311=1,0' in line:
                if 'splitncnn' in line:
                    if 'Pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                        line =(line.replace('-23309=1,1 -23310=1,2 -23311=1,0','-23309=1,0 -23310=1,2 -23311=1,0'))
            if '-23309=1,2 -23310=1,3 -23311=1,0' in line:
                if 'splitncnn' in line:
                    if 'Pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                        line =(line.replace('-23309=1,2 -23310=1,3 -23311=1,0','-23309=1,2 -23310=1,4 -23311=1,0'))  
    if pnnx:
        if 'Crop' in line:
            if 'splitncnn' in line:
                if 'pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                    line = line.replace('-23310=1,3 -23311=1,0 -23309=1,0','-23310=1,2 -23311=1,0 -23309=1,0')
            if 'splitncnn' in line:
                if 'pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                    line = line.replace('-23310=1,4 -23311=1,0 -23309=1,1','-23310=1,4 -23311=1,0 -23309=1,2')
            if 'splitncnn' in line:
                if 'pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                    line = line.replace('-23310=1,2 -23311=1,0 -23309=1,1','-23310=1,2 -23311=1,0 -23309=1,0')
            if 'splitncnn' in line:
                if 'pow' in flowparam[iteration+1] or 'warp' in flowparam[iteration+1]:
                    line = line.replace('-23310=1,3 -23311=1,0 -23309=1,2','-23310=1,4 -23311=1,0 -23309=1,2')
        
    #Replace OP
    if 'pow' in line.lower():
        line = line.replace('BinaryOp','rife.Warp').replace('Pow','warp').replace('pow','warp')
    newParamFile.append(line)

with open (f'flownet.param','w') as f:
    for line in newParamFile:
        f.write(line)
    

                    

        
