import os

folder = os.path.join(os.getcwd(),'backend/output')
filelist = [f for f in os.listdir(folder)if f.endswith(".pptx")]

for f in filelist:
    os.remove(os.path.join(folder,f))
