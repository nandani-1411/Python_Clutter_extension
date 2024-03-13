import os

def clutter(exten):
    i=0
    mainpath="filesfolder"
    filelist =os.listdir("filesfolder")
    for file in filelist:
        i=i+1
        # print(file)
        # root,extenstion=os.path.splitext(file)
        oldpath=os.path.join(mainpath,file)
        newname=f"{i}.{exten}"
        newpath=os.path.join(mainpath,newname)

        os.rename(oldpath,newpath)
    

exten =input("Enter The Extension What you wanted in Your file")

clutter(exten)
print(f"YOur Extentsion is {exten} Converted Successfully")