import os
with open (f'flownet.param','r') as f:
    flowparam = f.readlines()
newParamFile = []

for iteration,line in enumerate(flowparam):
    #Fix cropping
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
        
    #Replace OP
    if 'Pow' in line:
        line = line.replace('BinaryOp','rife.Warp').replace('Pow','warp')
    newParamFile.append(line)

with open (f'flownet.param','w') as f:
    for line in newParamFile:
        f.write(line)
    

                    

        
