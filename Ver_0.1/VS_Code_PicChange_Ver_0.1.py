import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json

testpath = "D:\\Learn\\Learning\C_learning\\04_Algorithm\Data_structrue\\3_Vscode_Change_BGPic"
bg_color = "height: 100%;width: 100%;margin: 0;\
padding: 0;\
overflow: hidden;\
font-size: 11px;\
user-select: none;\
pointer-events: auto !important;\
background-size: 100% !important;\
opacity: 0.9 !important;\
background-position: 0 0 !important;\
background-image: url(\"VSCODE_BG_IMAGE\") !important;\
content: \"\";\
position: absolute;\
z-index: 99999;\
width: 100%;\
background-repeat: no-repeat"


class VS_Code_BG:
  def __init__(self):
    self.current_path = os.path.dirname(__file__)
    self.target_file_name = "workbench.desktop.main.css"
    self.vscode_bg_path = "Microsoft VS Code\\resources\\app\\out\\vs\\workbench\\"
    # self.vscode_bg_path = "test\\"
    self.vscode_path = "D:\\"
    # copy image to this path
    self.dest_address = ""
    # vs code css file
    self.target_file =  ""
    # bg_color informations <!!! important !!!>
    self.bg_color = bg_color
    self.data = {
      "vscode_install_path": "D:\\",
    }

  def Initialization(self):
    root = tk.Tk()
    root.withdraw()

    # get vs_code installed path
    while 1:
      self.vscode_path = filedialog.askdirectory(title="Choose your VS Code Installation directory")
      print(self.vscode_path)
      if not self.vscode_path:
        if messagebox.askyesno(message="The following operations cannot be performed without Installation directory!"):
          return 0
        else:
          continue
      else:
        break
    # copy image to this path
    self.dest_address = os.path.join(self.vscode_path, self.vscode_bg_path)
    # vs code css file
    self.target_file =  os.path.join(self.dest_address, self.target_file_name)

    backup_file = os.path.join(self.current_path, self.target_file_name)
    if not os.path.isfile(backup_file):# back up css files
      prompt = input("You have no backup setting file, \
        do you want create one?(Y/N or others):\n")
      if(prompt=='Y' or prompt=='y'):
        shutil.copy(self.target_file,self.current_path)
    return 1;
        

  def ChangeBG(self):
    # instantiation file select windows and get image file path
    root = tk.Tk()
    root.withdraw()

    while 1:
      image_path = filedialog.askopenfilename(title="Choose background picture you prefer")
      if not image_path:
        if messagebox.askyesno(message="Don't you want a nice background picture?"):
          return 0
        else:
          continue
      else:
        break
    
    print('\nfile path is : \n', image_path) # get the bg_image file path
    (image_path_only, image_file) = os.path.split(image_path) # get the bg_image file name
    print(image_file)

    # copy image file to destination path
    shutil.copy(image_path,self.dest_address)
    print("successfully copy %s to %s"%(image_path,self.dest_address))


    # change the image file setting
    self.bg_color = self.bg_color.replace("VSCODE_BG_IMAGE",image_file)

    os.path.join(self.vscode_path, self.vscode_bg_path)
    with open(self.target_file, "r+", encoding = "utf-8") as file:
      txt = file.read()
      addr = txt.index("}body{")
      addr = addr+6
      end_addr = txt[addr:].index("}")
      # print("\n[%s] \nwill be repalced by [%s]\n"%(txt[addr:addr+end_addr], self.bg_color))
      txt = txt[:addr] + self.bg_color + txt[addr+end_addr:]

      file.seek(0)
      file.truncate()
      file.write(txt)
    
    return 1

  def Reset_setting(self):
    backup_file = os.path.join(self.current_path, self.target_file_name)

    if os.path.isfile(backup_file):
      os.remove(self.target_file)
      shutil.copy(backup_file, self.dest_address)
    else:
      print("\nNo backup!!!")


def Process():
  CodeBG = VS_Code_BG()
  if not CodeBG.Initialization():
    return 0
  while True:
    print("You may want to :")
    print("[0]:Change the background.")
    print("[1]:Reset settings.")
    main_prompt = input("Tell me what you need(Y/N or others):")

    if main_prompt=='0':
      CodeBG.ChangeBG()
    elif main_prompt=='1':
      command = input("Are you need to reset the background?(Y/N or others)\n")
      if(command=="Y" or command=="y"):
        CodeBG.Reset_setting()
    else:
      break


if __name__ == "__main__":
  Process()
  
  input("Press any key to exit...")
