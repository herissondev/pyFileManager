# Simple Python File Manager

This repository contains a Python script that lets you relocate files automatically.

## How to use ?
### Clone the repository:
Enter your desired folder and execute this command: <br>
`git clone https://github.com/aime-risson/pyFileManager.git`

### Set up the manager:
In the same directory create a new fille called `manager.py`
<br>
After that we will need to import our fileManager handler: `MyHandler`
```python
from fileManager import MyHandler

handler = MyHandler()
```
Once imported we will need to create new events.<br>
Events are used to listen to a specific folder and to relocate new files to a folder if their extensions match the desired ones.<br>
For example:<br>
```python
listeningFolder = "Path/to/watched/folder" 
relocateFolder = "Path/to/desired/folder" 
extensionsToInclude = (".yourExtensionInLowerCase", ".jpg", ".png") #Tuple of strings !!!

handler.newEvent(listeningFolder, relocateFolder, extensionsToInclude)

```
