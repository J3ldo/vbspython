# Vbspython
### Description
Vbspython is a python package that lets you interact with vbscript (visual basic script) in python. This can be helpfull if you're learning the language  
   
Current amount of downloads:  
[![Downloads](https://pepy.tech/badge/vbspython)](https://pepy.tech/project/vbspython)

### Installing
Install it using pip in the console by saying: pip install vbspython   
Vbspython also can be installed under the following names:  
vbscript  
vbs

## What it does
vbspython does a lot of things. Here are some of them: 
* Show a msgbox gui on the screen.
* Show a working input gui on the users screen.
* Do system commands.
* Pressing keys.
* Show the location of special folders like appdata and downloads.
* Creating shortcuts to files.
* Creating hotkeys that open a file.
* Creating folders
* Deleting folders
* Deleting files
* Copy files
* Copy folders
* Mocing files
* Moving folders

## Example code
### Multiple items in one file
```python
import vbspython    
file = vbspython.makefile()

file.msgbox("The next item will be an input box!")
file.input("Give your input here")
output = file.run() #Will be a list
```

### Run instantly
```python
import vbspython

print(vbspython.system("whoami")) #Some attributes from makefile can also be run instantly
> J3ldo

```

### Msgbox
```python
import vbspython

icon = vbspython.itemattributes.msgbox.icons.information()
options = vbspython.itemattributes.msgbox.options.ok_cancel()

vbspython.msgbox(text="Hello!", title="My first message box!", icon=icon, options=options) #will show a message box try it your self

```
#### Getting output
```python
import vbspython

#This is a simple program which says if you said yes or no 
if vbspython.msgbox("Yes or no?", options=vbs.itemattributes.msgbox.options.yes_no) == vbspython.itemattributes.msgbox.returns.no():
    vbspython.msgbox("You said no!", getoutput=False)
else:
    vbspython.msgbox("You said yes!", getoutput=False)
```

### Input
```python
import vbspython

print(vbspython.input("What do you think of this library?")) #will print the input the user gave
```

### Variables
Variables is an easy way to set variables to items in vbscript like output or system. Here is a quick example.  
```python
import vbspython as vbs

file = vbs.makefile()

var = file.Variable("myvariable")  # Declare the variable name.

file.system('whoami', variable=var.apply()) #  Apply the variable to the output of system.
file.msgbox('You are: ', variable=var.reference()) #  Show the output using the reference keyword

file.run() #  Run the file
```

### Pressing keys
```python
import vbspython

file = vbspython.makefile()
file.execute("notepad") #Will open notepad using windows + r
file.sleep(1) #sleep is in seconds. This will sleep the python file and the vbs file but is not needed if run without a file
file.presskeys("Hello world!")
file.presskey("enter") #Will press enter. To get a list of keys leave empty
file.run()
```

### Looping
```python
#Dont run like this
import vbspython as vbs
file = vbs.makefile()
file.msgbox("I am indestructable!")

while True:
    file.run(deletefile=False)
    
file.delete()

#But like this
import vbspython

file = vbspython.makefile()

@file.loop()
def loop_this():
   file.msgbox("I am indestructable!")
   

file.run()
```
### Looping an amount of time
```python
import vbspython

file = vbspython.makefile()

@file.loop(10)
def loop_this():
   file.msgbox("I will be run 10 times!")
   

file.run()
```

### Special folders
```python
import vbspython

path = vbspython.specialfolder("Downloads")
print(path) #Will print the path to downloads could be useful if your downloading things
```
### Text to speech
```python
import vbspython as vbs

file = vbs.makefile()

tts = file.tts()  # Enable the text to speech.

tts.volume(50)  # Set the volume of the text to speech. Cant be higher then 100.  
tts.rate(1)  # Sets the rate of the speaker. Can't be higher then 10 and must be higher then -10.  

tts.voice(vbs.itemattributes.tts.voice_1())  # Sets the voice of the speaker.  

tts.speak("Hello, world.") #Says the text. The same as say.  

file.run()  # Run the file.  

```

### Copying
```python
import vbspython as vbs

vbs.copy("Hello, i am copied.") #Copies: 'Hello, i am copied.' to the clipboard
print(vbs.getcopied()) #Prints the current copied item on the clipboard

```

### Creating shortcuts
```python
import vbspython

shortcut = "picture.png" #If the shortcut is clicked it will open the picture
location = "./" #Current executing directory
icon = 20 #put in an integer for the built in icons. Else put in a string with the location to the .ico
name = "openpicture" #this indicates the name of the shortcut

vbspython.createshortcut(shortcut, location, icon, name)
print("Succesfully made the shortcut!")
```

### Creating hotkeys
```python
import vbspython

#First off the unfunny script.
open = "bananas.png" #Will open bananas.png
hotkey = "Ctrl+Alt+e" #When you press ctrl and alt and e at the same time it will open.
name = "hotkeyname" #optional. can be left blank

vbspython.createhotkey(open, hotkey, name)

#the next one is a funny troll script. It will disable a random key on your keyboard
import string, random

open = "nothing.vbs" #A blank vbs script which does nothing.
hotkey = random.choice(list(string.ascii_lowercase)) #Will get a random ascii character. When pressed the key will look like it wasnt pressed

vbspython.createhotkey(open, hotkey)

```
#### Deleting hotkeys
```python
'''
Deleting hotkeys needs to be done manual. First of go in to file explorer and enable show hidden files. 
Then go to your desktop and search for a file with a standard .exe icon called: vbspythonhotkey_{the id/custom name}.
Now the hotkey has been deleted!

'''
```

### Files
### Creating files
#### Creating a folder
```python
import vbspython

file = vbspython.makefile()

file.createfolder("C:\Users\MyUser\Myepicfolder") #Myepicfolder will be the folder that will be created

file.run()
```
### Deleting files
#### Deleting a file
```python
import vbspython

file = vbspython.makefile()

file.deletefile("TempFile.py") #Deletes the file TempFile.py

file.run()
```
#### Deleting a folder
```python
import vbspython

file = vbspython.makefile()

file.deletefolder("AllTempFiles") #Will delete the whole folder and the contents in it

file.deletefile("TempFile.py")

file.run()
```
### Copying and moving
#### Copy file
```python
import vbspython

file = vbspython.makefile()

file.copyfile("Secretfile.txt", "C:\Users") #copies the file to the Users directory

file.run()
```
#### Copy folder
```python
import vbspython

file = vbspython.makefile()

file.copyfolder("Newuser", "C:\Users") #Copies folder to C:\Users

file.run()
```
#### Move file
```python
import vbspython

file = vbspython.makefile()

file.movefile("TempFile.py", "Tempfiles") #moves a file

file.run()
```
#### Move folder
```python
import vbspython

file = vbspython.makefile()

file.movefolder("TempFiles", "Logs") #moves the file

file.run()
```

## Changelog  
0.0.1 - Made vbspython but it doesnt work  
0.0.2 - Made it work  
0.0.8 - Made a press keys will press any keys of choice. A sleep that will make the .vbs file sleep. And a presskey that will press a special key leave empty for a list of keys.  
0.1.0 - Made a help loop and runfile.  
0.1.1 - Made the getting input system better. Added icons and options in the itemattributes class  
0.1.2 - Added a runas command this will run the file as administrator. And a tts class with: say, rate, volume (see in attributes), speak (same as say)  
0.1.3 - Added a copyfile movefile createfolder movefolder deletefolder deletefile copyfolder and did some bug fixes  
0.1.4 - Added an execute this doesnt stop when opening files like with system
0.1.5 - Added special folders
0.1.6 - Changelog forgotten
0.1.7 - Forgot to do the changelog on 0.1.6 and partialy on 0.1.7. I added creating shortcuts to files and added hotkeys.
0.1.8 - Added the option to get a variable from msgbox. use to see if someone said yes or no using the itemattributes.  
0.1.9 - Added the Variable class (see github docs) that applies to input, msgbox, and system. Also added @staticmethod to itemattributes.  
0.2.0 - Big update! What was added in 0.2.0 was: the amount of looping in @loop, and a variable param to specialfolder, :param for all items in makefile to help ide's read it, and added a copy and getcopied function.  
