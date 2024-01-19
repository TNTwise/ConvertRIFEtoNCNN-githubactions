import os

ensemble = False


#get RIFE_HDv3.py file as list
try:
    with open('train_log/RIFE_HDv3.py', 'r') as f:
        RIFE_HD_FILE = f.readlines()
except Exception as e:
    print('No train_log/RIFE_HDv3.py file found! did you input the model?')

#get IFNET_HDv3.py file as list
try:

    with open('train_log/IFNet_HDv3.py', 'r') as f:
        IFNet_HD_FILE = f.readlines()
except Exception as e:
    print('No train_log/IFNet_HDv3.py file found! did you input the model?')

def modify_rife_hd():
    modified_RIFE_HD_FILE = []

    for line in RIFE_HD_FILE:
        if 'flow, mask, merged = self.flownet(imgs, timestep, scale_list)' in line:
            line = line.replace('flow, mask, merged = self.flownet(imgs, timestep, scale_list)', '''torch.onnx.export(
    self.flownet,
    (torch.rand(1, 3, 256, 256),torch.rand(1, 3, 256, 256), torch.Tensor([0.5])),
    "rife.onnx",
    verbose=False,
    opset_version=11,
    input_names=["in0", "in1", "in2"],
    output_names=["out0"],)''')
        if 'return merged[3]' in line:
            line = line.replace('return merged[3]','exit()')
        modified_RIFE_HD_FILE.append(line)
        
    try:
        os.mkdir('train_log_export')
    except:
        pass

    with open('train_log_export/RIFE_HDv3.py', 'w') as f:
            f.writelines(modified_RIFE_HD_FILE)


def modify_ifnet_hd():
    modified_IFNet_HD_FILE = []
    # Training = False is now the meaning for if export = True, so if an if statement needs to run on export, it asks if Training = False, and vise versa
    for line in IFNet_HD_FILE:

        if 'def forward(self, x, timestep=0.5, scale_list=[8, 4, 2, 1], training=False, fastmode=True, ensemble=False):' in line:
            
            line = line.replace(f'def forward(self, x, timestep=0.5, scale_list=[8, 4, 2, 1], training=False, fastmode=True, ensemble=False):',
                                f'def forward(self, img0,img1, timestep=0.5, scale_list=[8, 4, 2, 1], training=False, fastmode=True, ensemble={ensemble}):')
            
        
        if 'if training == False:' in line:
            line=line.replace('if training == False:','if training == True:')

        if 'channel = x.shape[1] // 2' in line:
            line = line.replace('channel = x.shape[1] // 2','x=1')

        if 'img0 = x[:, :channel]' in line:
            line = line.replace('img0 = x[:, :channel]','channel=1')

        ### ^^^^ this just removes the redefining of images with the x variable
            
        if 'if not torch.is_tensor(timestep):' in line:
            line = line.replace('if not torch.is_tensor(timestep):','if training == False:')
        
        if 'timestep = (x[:, :1].clone() * 0 + 1) * timestep' in line:
            line = line.replace('timestep = (x[:, :1].clone() * 0 + 1) * timestep', 'timestep = ((torch.cat((img0,img1),1)[:, :1].clone() * 0 + 1) * timestep).float()')
        
        if 'wf0 = warp(f0, flow[:, :2])' in line:
            line = line.replace('wf0 = warp(f0, flow[:, :2])','wf0 = f0**flow[:, 1:2]')
        
        if 'wf1 = warp(f1, flow[:, 2:4])' in line:
            line = line.replace('wf1 = warp(f1, flow[:, 2:4])','wf1 = f1**flow[:, 2:3]')
        
        if 'warped_img0 = warp(img0, flow[:, :2])' in line:
            line = line.replace('warped_img0 = warp(img0, flow[:, :2])','warped_img0 = img0**flow[:,:3]')
        
        if 'warped_img1 = warp(img1, flow[:, 2:4])' in line:
            line = line.replace('warped_img1 = warp(img1, flow[:, 2:4])','warped_img1 = img1**flow[:,1:4]')
        
        if 'return flow_list, mask_list[3], merged' in line:
            line = line.replace('return flow_list, mask_list[3], merged', 'return merged[3]')
        
        modified_IFNet_HD_FILE.append(line)
    with open('train_log_export/IFNet_HDv3.py', 'w') as f:
            f.writelines(modified_IFNet_HD_FILE)
def copy_files():
    try:
        os.system('cp train_log/refine.py train_log_export/refine.py')
    except:
        print("WARN: No refine file")
    try:
        os.system('cp train_log/flownet.pkl train_log_export/flownet.pkl')
    except:
        print("ERROR: No flownet file")
        return 1




modify_rife_hd()
modify_ifnet_hd()
copy_files()
