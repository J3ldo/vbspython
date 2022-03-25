'''

--Base Process--

import subprocess, os
with open('test.vbs', 'x') as f:
    f.write('msgbox \"Hello\"')

CREATE_NO_WINDOW = 0x08000000
DETACHED_PROCESS = 0x00000008
subprocess.run('cscript test.vbs', creationflags=CREATE_NO_WINDOW)
print('True')
os.remove('test.vbs')


You can go a step farther by forcing the child to have no console at all:

DETACHED_PROCESS = 0x00000008
subprocess.call('taskkill /F /IM exename.exe', creationflags=DETACHED_PROCESS)

--Base Process--

'''


import subprocess as sub
import os
from pathlib import Path

class makefile:
    def __init__(self, filename=None):
        self.inputvar = False
        filename2 = filename
        if filename == None: filename2 = 'file'
        self.filename = filename2



        try: #if the file not exists
            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{filename2}.vbs', 'x') as f:
                pass   #makes the file
        except: #if the file already exists
            for f in os.listdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files'):
                os.remove(os.path.join(f'{str(Path( __file__ ).absolute())[:-11]}\\files', f)) #clears the directory

            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{filename2}.vbs', 'x') as f: #re-creates the file
                pass



    def msgbox(self, text=None, title=None): #make a msgbox
        if text == None: text = "" #if the text, title is None
        if title == None: title = ""
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f: #writes it into the .vbs file
            f.write(f'msgbox \"{text}\",,\"{title}\"\n')


    def input(self, text=None, title=None, getvar=False): #pretty much the same as msgbox
        if text == None: text = ""
        if title == None: title = ""
        self.inputvar = getvar
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if not getvar:
                f.write(f'Inputbox \"{text}\",\"{title}\"\n')
            elif getvar:
                f.write(f'txt=Inputbox(\"{text}\",\"{title}\")\n'
                        'a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - '
                        'Len(wscript.scriptname) - 6)\n'
                        'Set fleobj = CreateObject(\"Scripting.FileSystemObject\")'
                        '.OpenTextFile(a & \"var.txt\",2)\n'
                        f'fleobj.WriteLine(txt)\n'
                        f'fleobj.close\n'
                        f'Set fleobj = Nothing\n')






    def run(self, deletefile=True, showprompt=False): #runs the file
        if showprompt:
            sub.run(f'cscript {str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')
            if deletefile:
                os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')

        elif not showprompt:
            sub.run(f'cscript {str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', creationflags=0x08000000) #turns off the prompt
            if deletefile:
                os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')
        else:
            print('something went wrong')

        if self.inputvar:
            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\var.txt', 'r') as r:
                self.inpvar = r.readline()
            return self.inpvar #returns the inpvar given
        return

    def delete(self, file='file', allfiles=False):
        if allfiles:
            for i in os.listdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files'):
                os.remove(os.path.join(f'{str(Path( __file__ ).absolute())[:-11]}\\files', i))

        if not allfiles:
            os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{file}.vbs')
