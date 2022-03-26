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
            try:
                for f in os.listdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files'):
                    os.remove(os.path.join(f'{str(Path( __file__ ).absolute())[:-11]}\\files', f)) #clears the directory

                with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{filename2}.vbs', 'x') as f: #re-creates the file
                    pass
            except:
                os.mkdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files')
                with open(f'{str(Path( __file__ ).absolute())[:-11]}\\var.txt', "x"):
                    pass

                with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{filename2}.vbs', 'x') as f:  # re-creates the file
                    pass




    def msgbox(self, text=None, title=None): #make a msgbox
        if text == None: text = "" #if the text, title is None
        if title == None: title = ""
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f: #writes it into the .vbs file
            f.write(f'msgbox \"{text}\",,\"{title}\"\n')

    def system(self, cmd, showprompt=False, getouput=False):
        if not showprompt: sprompt = ", 0, True"
        if showprompt: sprompt = ""
        if getouput: self.inputvar = True
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if getouput:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                    f"Set out = oShell.Exec(\"cmd.exe /C {cmd}\")\n"
                    f"all = out.StdOut.ReadAll\n"
                    'a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - '
                    'Len(wscript.scriptname) - 6)\n'
                    'Set fleobj = CreateObject(\"Scripting.FileSystemObject\")'
                    '.OpenTextFile(a & \"var.txt\",2)\n'
                    f'fleobj.WriteLine(all)\n'
                    f'fleobj.close\n'
                    f'Set fleobj = Nothing\n'
                        )
            else:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                        f"oShell.Run \"cmd.exe /C {cmd}\" {sprompt}\n")


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


    def presskeys(self, keys):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"set oShell = Createobject(\"wscript.shell\")\n"
                f"oShell.sendkeys(\"{keys}\")\n"
            )

    def sleep(self, amount):
        amount *= 1000
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"set oShell = Createobject(\"wscript.shell\")\n"
                f"wscript.sleep {amount}\n"
            )

    def presskey(self, key=None):
        if key == None:
            print(
                  "List of keys:\n"
                  """
Key	            Code
Backspace:	    BACKSPACE, BKSP or: BS
Break:	        BREAK
Caps Lock:  	CAPSLOCK
Delete	        DELETE or: DEL
Down Arrow:	    DOWN
End:	        END
Enter:          ENTER or ~
Escape:      	ESC
Help:	        HELP
Home:	        HOME
Insert:	        INSERT or INS
Left Arrow:	    LEFT
Num Lock:	    NUMLOCK
Page Down:	    PGDN
Page Up:	    PGUP
Print Screen:	PRTSC
Right Arrow:	RIGHT
Scroll Lock:    SCROLLLOCK
Tab:	        TAB
Up Arrow:       UP
F1: 	        F1
F2: 	        F2
F3: 	        F3
F4: 	        F4
F5: 	        F5
F6: 	        F6
F7:  	        F7
F8:       	    F8
F9: 	        F9
F10:            F10
F11:            F11
F12:            F12
F13:            F13
F14:            F14
F15:            F15
F16:            F16
                  """
            )
            return

        key_to_send1 = "{"
        key_to_send2 = "}"

        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"set oShell = Createobject(\"wscript.shell\")\n"
                f"oShell.sendkeys(\"{key_to_send1}{key}{key_to_send2}\")\n"
            )

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
                self.inpvar = r.read()
            return self.inpvar #returns the inpvar given
        return

    def delete(self, file='file', allfiles=False):
        if allfiles:
            for i in os.listdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files'):
                os.remove(os.path.join(f'{str(Path( __file__ ).absolute())[:-11]}\\files', i))

        if not allfiles:
            os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{file}.vbs')
