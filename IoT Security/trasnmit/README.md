Prerequisites
Arduino 1.6.5 (or newer, if you know what you are doing)
git
python 2.7
terminal, console, or command prompt (depending on you OS)
Internet connection
Instructions
Open the console and go to Arduino directory. This can be either your sketchbook directory (usually <Documents>/Arduino), or the directory of Arduino application itself, the choice is up to you.
Clone this repository into hardware/esp8266com/esp8266 directory. Alternatively, clone it elsewhere and create a symlink, if your OS supports them.

cd hardware
mkdir esp8266com
cd esp8266com
git clone https://github.com/esp8266/Arduino.git esp8266
You should end up with the following directory structure:

Arduino
|
--- hardware
    |
    --- esp8266com
        |
        --- esp8266
            |
            --- bootloaders
            --- cores
            --- doc
            --- libraries
            --- package
            --- tests
            --- tools
            --- variants
            --- platform.txt
            --- programmers.txt
            --- README.md
            --- boards.txt
            --- LICENSE
Download binary tools

cd esp8266/tools
python get.py
Restart Arduino
