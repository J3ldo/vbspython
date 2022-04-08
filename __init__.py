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
import ast
import time

#print(os.path.abspath("main.py"))
#print(os.path.abspath("main.py").split("\\")[-1])
fileids = 0


class dontusethispls:
    def __init__(self, outer):
        self.outer = outer
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                "Set tts = CreateObject(\"SAPI.SpVoice\")\n"
            )

    def rate(self, rate=0):
        if int(rate) > 10 or int(rate) < -10:
            raise Exception("You can't have the rate above 10 or under -10")
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Rate = {rate}\n"
            )

    def say(self, text):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Speak \"{text}\"\n"
            )

    def speak(self, text):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Speak \"{text}\"\n"
            )

    def voice(self, speaker):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"Set tts.Voice = tts.GetVoices.Item({speaker})\n"
            )

    def volume(self, volume):
        if int(volume) > 100 or int(volume) < 0:
            raise Exception("Volume can't be higher then 100 or lower then 0")

        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Volume = {volume}\n"
            )




class makefile:
    def __init__(self, filename=None):
        self.inputvar = False
        self.runasadmin = False
        filename2 = filename
        global fileids
        if filename == None: filename2 = 'file' if fileids == 0 else f'file{fileids}'
        self.filename = filename2
        fileids += 1


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
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f: #writes it into the .vbs file
            f.write(f'all_vars = \"[\"\n')

    def tts(self):
        return dontusethispls(self)


    def msgbox(self, text=None, title=None, icon=None, options=None): #make a msgbox
        if text == None: text = "" #if the text, title is None
        if title == None: title = ""

        opts = ""
        if options == None and icon != None:
            opts += icon
        if icon == None and options != None:
            opts += options
        if icon != None and options != None:
            opts += options + "+" + icon

        if icon == None: icon = ""
        if options == None: options = ""

        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f: #writes it into the .vbs file
            f.write(f'msgbox \"{text}\",{opts},\"{title}\"\n')

    def system(self, cmd, showprompt=False, getouput=False):
        if not showprompt: sprompt = ", 0, True"
        if showprompt: sprompt = ""
        if getouput: self.inputvar = True
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if getouput:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                    f"Set out = oShell.Exec(\"cmd.exe /C {cmd}\")\n"
                    f"all = out.StdOut.ReadAll\n"
                    f"all_vars = all_vars + \"\"\"\"\"\"\"\" & all & \"\"\"\"\"\"\"\" & \",\"\n"
                        )
            else:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                        f"oShell.Run \"cmd.exe /C {cmd}\" {sprompt}\n")


    def execute(self, item):
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                    f"oShell.Run \"{item}\"\n"
                    )

    def input(self, text=None, title=None, getvar=True): #pretty much the same as msgbox
        if text == None: text = ""
        if title == None: title = ""
        self.inputvar = getvar
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if not getvar:
                f.write(f'Inputbox \"{text}\",\"{title}\"\n')
            elif getvar:
                f.write(f'txt=Inputbox(\"{text}\",\"{title}\")\n'
                        f'all_vars = all_vars + \"\"\"\" & txt & \"\"\"\" & \",\"\n')


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

    def loop(self, func):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"do\n"
            )
        func()
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"loop\n"
            )

    def runas(self):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                "Sub RunAsAdmin()\n"
                "If WScript.Arguments.Named.Exists(\"RunAsAdmin\") Then Exit Sub\n"
                "CreateObject(\"Shell.Application\").ShellExecute _\n"
                "\"WScript.exe\", \"\"\"\" & WScript.ScriptFullName & \"\"\" /RunAsAdmin\",\"\",\"runas\", 1\n"
                "WScript.Quit()\n"
                "End Sub\n"
                "RunAsAdmin()\n")

            self.runasadmin = True


    def copyfile(self, oldpath, newpath):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.CopyFile \"{os.path.abspath(oldpath)}\" , \"{os.path.abspath(newpath)}\\\"\n"
            )


    def copyfolder(self, oldpath, newpath):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.CopyFolder \"{os.path.abspath(oldpath)}\", \"{os.path.abspath(newpath)}\\\"\n"
            )


    def movefile(self, oldpath, newpath):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.MoveFile \"{os.path.abspath(oldpath)}\" , \"{os.path.abspath(newpath)}\\\"\n"
            )


    def movefolder(self, oldpath, newpath):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.MoveFolder \"{os.path.abspath(oldpath)}\", \"{os.path.abspath(newpath)}\\\"\n"
            )


    def createfolder(self, path):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.CreateFolder \"{path}\"\n"
            )

    def deletefolder(self, path):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.DeleteFolder \"{os.path.abspath(path)}\"\n"
            )

    def deletefile(self, path):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.DeleteFile \"{os.path.abspath(path)}\"\n"
            )

    def filelocation(self):
        return f"{str(Path(__file__).absolute())[:-11]}files\\{self.filename}.vbs"

    def filecontent(self):
        with open(f"{str(Path(__file__).absolute())[:-11]}files\\{self.filename}.vbs") as f:
            return f.read()

    def code(self):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'r') as f:
            return f.read()


    def run(self, deletefile=True, showprompt=False): #runs the file
        if self.inputvar:
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:  # writes it into the .vbs file
                f.write(
                    'all_vars = all_vars + \"]\"\n'
                    'a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - '
                    'Len(wscript.scriptname) - 6)\n'
                    'Set fleobj = CreateObject(\"Scripting.FileSystemObject\")'
                    '.OpenTextFile(a & \"var.txt\",2)\n'
                    'fleobj.WriteLine(all_vars)\n'
                    'fleobj.close\n'
                    f'Set fleobj = Nothing\n')

        if self.runasadmin:
            sub.run(f'cscript {str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', creationflags=0x08000000)
            if deletefile:
                time.sleep(0.2)
                os.remove(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs')
            return


        if showprompt:
            sub.run(f'cscript {str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')
            if deletefile:
                os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')

        elif not showprompt:
            sub.run(f'cscript {str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', creationflags=0x08000000) #turns off the prompt
            if deletefile:
                os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs')
        else:
            print('Something went wrong')

        if self.inputvar:
            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\var.txt', 'r') as r:
                self.inpvar = r.read()
            return ast.literal_eval(self.inpvar) #returns the inpvar given
        return

    def delete(self, file=None, allfiles=False):
        if file == None:
            file = self.filename
        if allfiles:
            for i in os.listdir(f'{str(Path( __file__ ).absolute())[:-11]}\\files'):
                os.remove(os.path.join(f'{str(Path( __file__ ).absolute())[:-11]}\\files', i))

        if not allfiles:
            os.remove(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{file}.vbs')

class help:
    def __init__(self):
        pass

    class makefile:
        def __init__(self):
            pass

        def help(self):
            print("Makes the file.\n\n"
                "Fields: \n"
                "filename (Indicates the filename)\n\n"
                  "Example: \n"
                  "file = vbspython.makefile()\n"
                  "file.run() (runs the file)")

        def msgbox(self):
            print("Will show a message box/prompt\n\n"
                  "Fields: \n"
                  "title (Shows the title of the message box)\n"
                  "text (The text displayed in the box)\n\n"
                  "Example: \n"
                  "file = vbspython.makefile()\n"
                  "file.msgbox(title=\"Im the title!\", text=\"Im the text\")")

        def system(self):
            print("Runs a command via the command prompt\n\n"
                  "Fields: \n"
                  "cmd (the command that you want to execute)\n"
                  "getoutput (If you want to get output from to commmand)\n\n"
                  "Example:"
                  "file = vbspython.makefile()\n"
                  "file.system(cmd=\"whoami\", getoutput=True)\n"
                  "output = file.run()\n"
                  "print(output)")

        def input(self):
            print(
                "Get an input from a user\n\n"
                "Fields: \n"
                "text (text of the input box)\n"
                "title (the title of the input box)\n"
                "getvar (gets the variable from the input)\n\n"
                "Example: \n"
                "file = vbspython.makefile()\n"
                "file.input(title=\"Title!\", text=\"Text\", getvar=True)"
                "varfrominput = file.run()\n"
                "print(varfrominput)"
            )

        def presskeys(self):
            print(
                "Simulates key presses.\n\n"
                "Fields: \n"
                "keys (The keys you want to press)\n\n"
                "Example: \n"
                "file = vbspython.makefile()\n"
                "file.presskeys(\"Hello!\")\n"
                "file.run()"
            )

        def presskey(self):
            print(
                "Presses a special key like enter or backspace. Leave empty for a list of them\n\n"
                "Fields: \n"
                "key (The key you want to press)\n\n"
                "Example:"
                "file = vbspython.makefile()\n"
                "file.presskey(\"enter\")\n"
                "file.run()"
            )

        def sleep(self):
            print(
                "Makes the program sleep ONLY THE VBS FILE\n\n"
                "Fields: \n"
                "amount (How long you want to let it sleep in seconds)\n\n"
                "Example: \n"
                "file = vbspython.makefile()\n"
                "file.sleep(10)"
                "file.run()"
            )

        def loop(self):
            print(
                "Makes a part of the file loop\n\n"
                "Fields: \n"
                "none\n\n"
                "Example: \n"
                "file = vbspython.makefile()\n"
                "@file.loop\n"
                "def itemtoloop():"
                "\tfile.sendkeys(\"Hello!\")\n"
                "file.run()"
            )

        def run(self):
            print(
                  "Runs the file\n\n"
                  "Fields: \n"
                  "deletefile (if you want to delete the file after running)\n"
                  "showprompt (shows everything that you normallyy couldnt see)\n\n"
                  "Example:\n"
                  "file = vbspython.makefile()\n"
                  "file.run()"
            )

        def delete(self):
            print(
                "Deletes a file of choice\n\n"
                "Fields: \n"
                "file (The file you want to delete. If left empty will delete the current file your using.)\n"
                "allfiles (Will delete all files in the files directory)\n\n"
                "Example:\n"
                "file = vbspython.makefile(filename=\"filename\")\n"
                "file.run(deletefile=False)\n"
                "file.run(deletefile=False)\n"
                "file.delete(file=\"filename\", allfiles=True)"
            )

    def runfile(self):
        print("Runs a file without the need for a makefile\n\n"
              "Fields:\n"
              "file (The file you want to run (Say file if you dont know the file name)\n"
              "showprompt (If you want to show the prompt)\n\n"
              "Example:\n"
              "file = vbspython.makefile(filename=\"myfile\")\n"
              "vbspython.runfile(file=\"myfile\", showprompt=True)"
              "")

def runfile(file:str, showprompt:bool=False):
    if file.endswith(".vbs"):
        pass
    else:
        file += ".vbs"
    if showprompt:
        sub.run(f'cscript {str(Path(__file__).absolute())[:-11]}\\files\\{file}')

    elif not showprompt:
        sub.run(f'cscript {str(Path(__file__).absolute())[:-11]}\\files\\{file}',
                creationflags=0x08000000)  # turns off the prompt


'''
Here will the instant use items go.
'''

def presskey(key=None):
    file = makefile()
    if key == None:
        file.presskey()
        return
    file.presskey(key)
    file.run()

def msgbox(text=None, title=None, icon=None, options=None):
    file = makefile()
    file.msgbox(text=text, title=title, icon=icon, options=options)
    file.run()

def input(text=None, title=None):
    file = makefile()
    if text == None:
        text = ""
    if title == None:
        title = ""

    file.input(text=text, title=title, getvar=True)
    output = file.run()
    return output[0]

def system(cmd, showprompt=False):
    file = makefile()
    if showprompt:
        file.system(cmd, showprompt=True, getouput=True)
    if not showprompt:
        file.system(cmd, getouput=True)

    output = file.run()
    return output[0]

def presskeys(keys):
    file = makefile()

    file.presskeys(keys)

    file.run()

def sleep(amount:int):
    file = makefile()

    file.sleep(amount)

    file.run()





class itemattributes:
    class tts:
        def voice_1(self):
            return "0"

        def voice_2(self):
            return "1"
    class msgbox:
        class returns:
            def ok(self):
                return "1"

            def cancel(self):
                return "2"

            def abort(self):
                return "3"

            def retry(self):
                return "4"

            def ignore(self):
                return "5"

            def yes(self):
                return "6"

            def no(self):
                return "6"

        class options:
            def ok(self):
                return "0"

            def ok_cancel(self):
                return "1"

            def retry_abort_ignore(self):
                return "2"

            def yes_no_cancel(self):
                return "3"

            def yes_no(self):
                return "4"

            def retry_cancel(self):
                return "5"


        class icons():
            def critical(self):
                return "16"

            def questionmark(self):
                return "32"

            def exclamation(self):
                return "48"

            def information(self):
                return "64"
