# RoboBuddy
Robo companion using RP2040 and other modules.
The plan is to have a robot that is able to change states/faces by reading the accelerometer data. It will have a variety of faces and sounds.
I am first testing the idea on a Raspberry Pi Pico with external modules. Once I finish the prototype I will make the design smaller by making my own PCB with the RP2040.
The software I am using is Thonny for the micropython code and KiCad for the PCB and schematic design.
8/15/2024: I have finished testing it on the pico and have been working on a schematic for the past weeks. I just finished the pcb design and generated the gerber files. I will hopefully begin production soon and see if my pcb works. I will be using JLCPCB.com to make the pcb board.
8/27/2024: Turns out there is an issue with my PCB's Flash memory (it is able to load as an external USB but doesn't load any UF2 files I put in it). I will downscale the project to just be a shield that will connect to a pico. The latest file should be uploaded in the "RoboBuddy Folder" and files named "RoboBuddy.kicad_..."
![image](https://github.com/BensBeens/RoboBuddy/blob/main/Schematic%20v.2.png)
![image](https://github.com/BensBeens/RoboBuddy/blob/main/Front3DView_PCB.png)
![image](https://github.com/BensBeens/RoboBuddy/blob/main/RoboBuddy_public/Front_PCBSchematic_new.png)
