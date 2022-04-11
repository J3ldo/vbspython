# Vbspython
### Information
Vbspython is a python package that lets you interact with vbscript (visual basic script) in python. This can be helpfull if you're learning the language  

### Installing
Install it using the console by saying: pip install vbspython  
Vbspython also can be installed under the following names:  
vbscript  
vbs

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

icon = vbspython.itemattributes().msgbox().icons().information()
options = vbspython.itemattributes().msgbox().options().ok_cancel()

vbspython.msgbox(text="Hello!", title="My first message box!", icon=icon, options=options) #will show a message box try it your self

```

### Input
```python
import vbspython

print(vbspython.input("What do you think of this library?")) #will print the input the user gave
```

### Pressing keys
```python
import vbspython

file = vbspython.makefile()
file.execute("notepad") #Will open notepad using windows + r
#file.sleep(1) #sleep is in seconds. This will sleep the python file and the vbs file but is not needed for this
file.presskeys("Hello world!")
file.presskey("enter") #Will press enter. To get a list of keys leave empty
file.run()
```

### Looping
```python
import vbspython

file = vbspython.makefile()

@file.loop
def loop_this():
   file.msgbox("I am indestructable!")

file.run()
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
