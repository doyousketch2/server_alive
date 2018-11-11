
[![OpenSource](https://img.shields.io/badge/Open-Source-orange.svg)](https://github.com/doyousketch2)  [![PythonVersions](https://img.shields.io/badge/Python-2.7-blue.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPL--v3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)  [![Git.io](https://img.shields.io/badge/Git.io-fptgb-233139.svg)](https://git.io/fptgb)  

# server_alive.py  
get a popup once your ping gets through  

**Requirements:**  
- [x] Python 2.7  ~~  comes with Linux  
      win users will have to install:  
      https://www.python.org/download/releases/2.7  

- [x] fping ~~  it's easy enough to install in Linux.  
      `sudo apt-get install fping`  
      Win users can find a link to download a compiled binary for windows here:  
      https://universallp.wordpress.com/2017/02/22/fping-on-windows  
      
- [x] gtk+  ~~  again, easy to install in Linux.  
      `sudo apt-get install libgtk-3-dev`  
       win users might have to jump through a couple hoops:  
       https://www.gtk.org/download/windows.php  
       https://pygobject.readthedocs.io/en/latest  

![image](https://raw.githubusercontent.com/doyousketch2/server_alive/master/Screenshot.png)  

the server and time between pings is hardcoded in the script,  
because I wrote it to serve a single purpose.  

if you wish to change these, just modify these two lines in the script:  
`server  = 'hometownserver.com'`  
`minutes_between_ping  = 30`  
