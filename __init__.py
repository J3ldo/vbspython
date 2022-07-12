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
currentid = 0


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
        global currentid
        if filename == None: filename2 = 'file' if currentid == 0 else f'file{currentid}'
        self.filename = filename2
        self.save_copied = False
        filename = self.filename
        currentid += 1

        if not os.path.exists(str(Path( __file__ ).absolute())[:-11]+"\\copied.txt"):
            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\copied.txt', 'w') as f:
                f.write('temp')


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


    def msgbox(self, text=None, title=None, icon="0", options="0", getoutput=True, variable=None): #make a msgbox
        '''
        :param text: The text in the msgbox
        :param title: The title of the msgbox
        :param icon: The icon. Can be gotten from itemattributes
        :param options: The options the user has. Can be gotten from itemattributes
        :param getoutput: If you want to get output from the msgbox.
        :param variable: The variable from the Variable class
        :return:
        '''

        if getoutput is True: self.inputvar = True
        if text == None: text = "" #if the text, title is None
        if title == None: title = ""

        opts = ""
        if options == None and icon != None:
            opts += icon
        if icon == None and options != None:
            opts += options

        if icon != None and options != None:
            opts += options + "+" + icon

        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f: #writes it into the .vbs file
            if variable is not None:
                fstrstart = "\" & "
                fstrend = " & \""
                f.write(f"{variable[0] if not variable[1] else 'unused = '}msgbox(\"{text+fstrstart+variable[0]+fstrend if variable[1] else text}\",{opts},\"{title}\")\n")

            elif getoutput:
                f.write(f"txt = msgbox(\"{text}\",{opts},\"{title}\")\n"
                        f"all_vars = all_vars + \"\"\"\" & txt & \"\"\"\" & \",\"\n")
            else:
                f.write(f"msgbox(\"{text}\",{opts},\"{title}\")\n")

    def system(self, cmd, showprompt=False, getouput=True, variable=None):
        '''
        :param cmd: The command to execute.
        :param showprompt: If the command prompt should be shown.
        :param getouput: If you want to get the output from the command.
        :param variable: A variable from the Variable class. To set or user
        '''


        sprompt = ", 0, True" if not showprompt else ""
        if getouput: self.inputvar = True
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if variable is not None:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                        f"Set {variable[0] if not variable[1] else 'unused = '}oShell.Exec(\"cmd.exe /C {variable[0] if variable[1] else cmd}\")\n"
                        f"Do While {variable[0][:-3] if not variable[1] else 'unused'}.Status <> 1\n"
                        "WScript.Sleep 100\n"
                        "Loop\n"
                        f"{variable[0] if not variable[1] else 'unused = '}{variable[0][:-3] if not variable[1] else 'unused'}.StdOut.Readall()\n")

            elif getouput:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                    f"Set out = oShell.Exec(\"cmd.exe /C {cmd}\")\n"
                    f"all = out.StdOut.ReadAll\n"
                    f"all_vars = all_vars + \"\"\"\"\"\"\"\" & all & \"\"\"\"\"\"\"\" & \",\"\n"
                        )


            else:
                f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                        f"oShell.Run \"cmd.exe /C {cmd}\" {sprompt}\n")


    def execute(self, item):
        '''
        :param item: Item to execute.
        :returns Same as system. But for opening things.
        '''

        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write("Set oShell = CreateObject (\"WScript.Shell\")\n"
                    f"oShell.Run \"{item}\"\n"
                    )

    class Variable:
        def __init__(self, name):
            self.name = name

        def reference(self):
            return self.name, True #True is for checking if its an refrence or if you want to apply it.

        def apply(self):
            return self.name + " = ", False

        def set(self, item):
            '''
            :param item: Item to set the variable to. Must be string or int.
            '''
            if not isinstance(item, int) or not isinstance(item, str):
                raise TypeError("Item must be int or string")
            else:
                global filename
                high_comma = "\""
                with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{filename}.vbs', 'a') as f:
                    f.write(
                        f"{self.name} = {high_comma+item+high_comma if isinstance(item, str) else item}"
                            )

    def createshortcut(self, filepath, lnkpath, icon, shrtname="shortcut"):
        '''
        :param filepath: The filepath of the item for the shortcut.
        :param lnkpath: Path the shortcut will be made in
        :param icon: The icon of the shortcut needs to be int or a .ico
        :param shrtname: Name of the shortcut.
        '''
        if isinstance(icon, int):
            icon = "%SystemRoot%\System32\SHELL32.dll," + str(icon)
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
                f.write("Set obj = createObject(\"wscript.shell\")\n"
                        f"Set shrt = obj.CreateShortcut(\"{os.path.abspath(lnkpath+ shrtname + '.lnk')}\")\n"
                        f"shrt.TargetPath = \"{os.path.abspath(filepath)}\"\n"
                        f"shrt.IconLocation = \"{icon}\"\n"
                        "shrt.Save\n"
                )

            with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
                f.write("Set obj = createObject(\"wscript.shell\")\n"
                f"Set shrt = obj.CreateShortcut(\"{os.path.abspath(lnkpath)}\")\n"
                f"shrt.TargetPath = {filepath}\n"
                f"shrt.IconLocation = \"{os.path.abspath(icon)}\"\n"
                "shrt.Save\n"
                    )


    def input(self, text="", title="", getoutput=True, variable=None): #pretty much the same as msgbox
        '''
        :param text: The text to appear in the input box.
        :param title: The title of the input box.
        :param getoutput: If you want to get output from the answer from the input box.
        :param variable: To set or use a variable from the Variable class
        '''
        if getoutput is True: self.inputvar = True
        with open(f'{str(Path( __file__ ).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if variable is not None:
                fstrstart = "\" & "
                fstrend = " & \""
                f.write(f"{variable[0] if not variable[1] else 'unused = '}Inputbox(\"{text+fstrstart+variable[0]+fstrend if variable[1] else text}\",\"{title}\")\n")

            elif not getoutput:
                f.write(f'Inputbox \"{text}\",\"{title}\"\n')
            elif getoutput:
                f.write(f'txt=Inputbox(\"{text}\",\"{title}\")\n'
                        f'all_vars = all_vars + \"\"\"\" & txt & \"\"\"\" & \",\"\n')


    def presskeys(self, keys):
        '''

        :param keys: Keys to press
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"set oShell = Createobject(\"wscript.shell\")\n"
                f"oShell.sendkeys(\"{keys}\")\n"
            )

    def sleep(self, amount):
        '''
        :param amount: Time to sleep in ms
        '''
        amount *= 1000
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"set oShell = Createobject(\"wscript.shell\")\n"
                f"wscript.sleep {amount}\n"
            )

    def presskey(self, key=None):
        '''
        :param key: The special key to press
        '''
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

    def loop(self, *args):
        '''
        :param *args: The amount of times to loop.
        '''
        def inner(func):
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
                if len(args) >= 1:
                    f.write(
                        "ffffffffffffggg = 1\n"
                        f"do While ffffffffffffggg < {int(args[0])}\n"
                        "ffffffffffffggg = ffffffffffffggg + 1\n"
                    )
                else:
                    f.write("do\n")
            func()
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
                f.write(
                    f"loop\n"
                )
        return inner

    def runas(self, file=None):
        '''
        :param file: The file to run must be a python file.
        '''
        if not file.endswith('.py'):
            raise Exception("You can at the minute only use .py files.")

        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if file is None:
                f.write(
                    "Sub RunAsAdmin()\n"
                    "If WScript.Arguments.Named.Exists(\"RunAsAdmin\") Then Exit Sub\n"
                    "CreateObject(\"Shell.Application\").ShellExecute _\n"
                    "\"WScript.exe\", \"\"\"\" & WScript.ScriptFullName & \"\"\" /RunAsAdmin\",\"\",\"runas\", 1\n"
                    "WScript.Quit()\n"
                    "End Sub\n"
                    "RunAsAdmin()\n")
                return
            else:
                f.write(
                "Set shell = CreateObject(\"Shell.Application\")"
                f"shell.ShellExecute \"python.exe\", \"{os.path.abspath(file)}\",,\"runas\", 1"
                )

            self.runasadmin = True


    def copyfile(self, oldpath, newpath):
        '''
        :param oldpath: The path of the copied file
        :param newpath: The new path of the copied file
        '''
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
        '''
        :param oldpath: The path of the file
        :param newpath: The new path of the moved file.
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.MoveFile \"{os.path.abspath(oldpath)}\" , \"{os.path.abspath(newpath)}\\\"\n"
            )


    def movefolder(self, oldpath, newpath):
        '''

        :param oldpath: Path of the folder to move.
        :param newpath: The new path of the moved folder
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.MoveFolder \"{os.path.abspath(oldpath)}\", \"{os.path.abspath(newpath)}\\\"\n"
            )


    def createfolder(self, path):
        '''
        :param path: Path of the folder to create.
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.CreateFolder \"{path}\"\n"
            )

    def deletefolder(self, path):
        '''
        :param path: Path of the folder to delete.
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
                f"fso.DeleteFolder \"{os.path.abspath(path)}\"\n"
            )

    def copy(self, item):
        '''
        :param item: Item to copy to clipboard.
        '''

        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                "Set shell = CreateObject(\"wscript.shell\")\n"
                "Set clip = shell.Exec(\"clip\")\n"
                f"clip.Stdin.Write \"{item}\"\n"
                "clip.Stdin.Close()\n"
            )

    def getcopied(self, getouput=True, variable=None):
        '''

        :param getouput: If you want to see output when you run it yes or no.
        :param variable: For the variable in the Variable class
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if variable is not None:
                f.write(
                    "Set html = CreateObject(\"htmlfile\")\n"
                    f"{variable[0] if not variable[1] else 'unused = '} = html.ParentWindow.ClipboardData.GetData(\"Text\")\n"
                )

            elif getouput:
                self.save_copied = True
                f.write(

                    "Set html = CreateObject(\"htmlfile\")\n"
                    "copied = html.ParentWindow.ClipboardData.GetData(\"Text\")\n"
                )
            else:
                f.write(
                    "Set html = CreateObject(\"htmlfile\")\n"
                    "html.ParentWindow.ClipboardData.GetData \"Text\" \n")


    def createhotkey(self, execute, hotkey, custom_name=currentid):
        '''
        :param execute: The path of the item of the file to run
        :param hotkey: The hotkey to press to execute the item.
        :param custom_name: The custom name of the hotkey. Used for multiple hotkeys.
        '''
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            f.write(
                f"""
set obj = WScript.CreateObject(\"WScript.Shell\")
Desktop = obj.specialfolders(\"Desktop\")
    
set shortcut = obj.CreateShortcut(Desktop & \"\\vbspythonhotkey_{custom_name}.lnk\")
shortcut.TargetPath = \"{os.path.abspath(execute)}\"
shortcut.Hotkey = \"{hotkey}\"
shortcut.IconLocation = "notepad.exe, 0"
shortcut.WorkingDirectory = \"C:\\\"
shortcut.Save
    
Set fso = CreateObject(\"Scripting.FileSystemObject\")

fso.GetFile(Desktop & \"\\vbspythonhotkey_{custom_name}.lnk\").Attributes = 34
                """
            )

    def specialfolder(self, folder=None, getoutput=True, variable=None):
        '''

        :param folder: The special folder.
        :param getoutput: If you want to get output from the function.
        :param variable: The variable for the Variable class.
        '''
        if folder == None:
            print(
                """
All special folders are:
This function will give their location on this pc.
    AllUsersDesktop
    AllUsersStartMenu
    AllUsersPrograms
    AllUsersStartup
    Desktop
    Favorites
    Fonts
    MyDocuments
    NetHood
    PrintHood
    Programs
    Recent
    SendTo
    StartMenu
    Startup
    Templates
                """
            )
            return


        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:
            if variable is not None:
                f.write("Set obj = createObject(\"wscript.shell\")\n"
                        f"{variable[0] if not variable[1] else 'unused = '}obj.specialfolders(\"{variable[0] if variable[1] else folder}\")\n")
                return

            f.write(
               "Set obj = createObject(\"wscript.shell\")\n"
               f"txt = obj.specialfolders(\"{folder}\")\n"
            )
            if getoutput:
                f.write(
                    f'all_vars = all_vars + \"\"\"\" & txt & \"\"\"\" & \",\"\n'
                )
                self.inputvar = True


    def deletefile(self, path):
        '''
        :param path: Path to the file to delete.
        '''
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

        if self.save_copied:
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.filename}.vbs', 'a') as f:  # writes it into the .vbs file
                f.write(
                    'a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - '
                    'Len(wscript.scriptname) - 6)\n'
                    'Set fleobj = CreateObject(\"Scripting.FileSystemObject\")'
                    '.OpenTextFile(a & \"copied.txt\",2)\n'
                    'fleobj.WriteLine(copied)\n'
                    'fleobj.close\n'
                )

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

            if self.save_copied:
                with open(f'{str(Path(__file__).absolute())[:-11]}\\copied.txt', 'r') as r:
                    copied = r.read()

            try:
                out = ast.literal_eval(self.inpvar)
                out.append(copied)

                return out #returns the inpvar given
            except:
                self.inpvar = self.inpvar.replace('\\', "/")

                out = ast.literal_eval(self.inpvar)
                out.append(copied)
                return out # returns the inpvar given

        elif self.save_copied:
            with open(f'{str(Path(__file__).absolute())[:-11]}\\copied.txt', 'r') as r:
                copied = r.read()

            return [copied]

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
        sub.getoutput("explorer https://github.com/J3ldo/vbspython/blob/main/README.md#example-code")

    '''class makefile:
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
                "getoutput (gets the output from the input)\n\n"
                "Example: \n"
                "file = vbspython.makefile()\n"
                "file.input(title=\"Title!\", text=\"Text\", getoutput=True)"
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
              "")'''

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

def msgbox(text=None, title=None, icon=None, options=None, getoutput=True):
    file = makefile()
    file.msgbox(text=text, title=title, icon=icon, options=options, getoutput=getoutput)

    if getoutput:
        return file.run()[0]

    file.run()

def input(text=None, title=None, getoutput=True):
    file = makefile()
    if text == None:
        text = ""
    if title == None:
        title = ""

    file.input(text=text, title=title, getoutput=getoutput)

    if getoutput:
        return file.run()[0]
    file.run()

def system(cmd, showprompt=False):
    file = makefile()
    if showprompt:
        file.system(cmd, showprompt=True, getouput=True)
    if not showprompt:
        file.system(cmd, getouput=True)

    return file.run()[0]

def presskeys(keys):
    file = makefile()

    file.presskeys(keys)

    file.run()

def sleep(amount:int):
    file = makefile()

    file.sleep(amount)

    file.run()


def createfolder(path):
    file = makefile()

    file.createfolder(path)

    file.run()

def copyfolder(oldpath, newpath):
    file = makefile()

    file.copyfolder(oldpath, newpath)

    file.run()

def copyfile(oldpath, newpath):
    file = makefile()

    file.copyfile(oldpath, newpath)

    file.run()

def movefolder(oldpath, newpath):
    file = makefile()

    file.movefolder(oldpath, newpath)

    file.run()

def movefile(oldpath, newpath):
    file = makefile()

    file.movefile(oldpath, newpath)

    file.run()

def deletefolder(path):
    file = makefile()

    file.deletefolder(path)

    file.run()

def deletefile(path):
    file = makefile()

    file.deletefile(path)

    file.run()

def execute(item):
    file = makefile()

    file.execute(item)

    file.run()

def speak(text):
    file = makefile()

    file.tts().speak(text)

    file.run()

def say(text):
    file = makefile()

    file.tts().say(text)

    file.run()

def copy(item):
    file = makefile()

    file.copy(item)

    file.run()


def getcopied():
    file = makefile()

    file.getcopied()

    return file.run()[0]


def specialfolder(folder=None, getoutput=True):
    file = makefile()

    file.specialfolder(folder, getoutput)

    if getoutput:
        if folder != None:
            return file.run()[0]
    file.run()


def createshortcut(filepath, lnkpath, icon, shrtname="shortcut"):
    file = makefile()

    file.createshortcut(filepath, lnkpath, icon, shrtname)

    file.run(deletefile=False)

def createhotkey(execute, hotkey, custom_name=currentid + 1):
    file = makefile()

    file.createhotkey(execute, hotkey, custom_name)

    file.run()

def docs():
    sub.getoutput("explorer \"https://github.com/J3ldo/vbspython/blob/main/README.md\"")

class itemattributes:
    class tts:
        @staticmethod
        def voice_1():
            return "0"

        @staticmethod
        def voice_2():
            return "1"
    class msgbox:
        class returns:

            @staticmethod
            def ok():
                return "1"

            @staticmethod
            def cancel():
                return "2"

            @staticmethod
            def abort():
                return "3"

            @staticmethod
            def retry():
                return "4"

            @staticmethod
            def ignore():
                return "5"

            @staticmethod
            def yes():
                return "6"

            @staticmethod
            def no():
                return "7"

        class options:
            @staticmethod
            def ok():
                return "0"

            @staticmethod
            def ok_cancel():
                return "1"

            @staticmethod
            def retry_abort_ignore():
                return "2"

            @staticmethod
            def yes_no_cancel():
                return "3"

            @staticmethod
            def yes_no():
                return "4"

            @staticmethod
            def retry_cancel():
                return "5"


        class icons:
            @staticmethod
            def critical():
                return "16"

            @staticmethod
            def questionmark():
                return "32"

            @staticmethod
            def exclamation():
                return "48"

            @staticmethod
            def information():
                return "64"
