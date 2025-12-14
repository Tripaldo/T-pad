# T-pad
my macropad, it has 8 buttons with macros that open apps and sites. every button has one or two led's linked to it so that they light up when the button is pressed. 

# Features
- 3d printed case
- led's linked to keys
- 8 keys
- simple python code with shortcuts to programs and sites

# CAD model
everything is held togheter by just 4 M3 bolts
the printed pieces are 2 and once the switches are soldered the keycaps will fit perfectly without any elevations.
<img width="1919" height="780" alt="Screenshot 2025-12-14 135656" src="https://github.com/user-attachments/assets/872525f6-c5d2-4758-9abc-7e7ef15e413d" />
made in fusion360.

# pcb
my pcb is very simple and made in KiCad.

this is the schematic:
<img width="1061" height="454" alt="Screenshot 2025-12-11 213529" src="https://github.com/user-attachments/assets/71cbbd80-fa30-48eb-85a1-33eb42bdf04a" />

this is the pcb:

<img width="552" height="539" alt="image" src="https://github.com/user-attachments/assets/d01c31dd-00e8-40b8-b53d-6875951e4957" />

# firmware
it uses KMK for a beginner friendly firmware.
- all 8 keys is a macro for apps and sites
- the firmware is easy to change so that everyone can change the macro's to whatever they like
- every button lights up the led near it
changes may be made in the future

# BOM
components needed for the hackpad (T-Pad)
- 8x cherry mx switches
- 8x dsa keycaps
- 4x M3 x 16 mm SHCS
- 12x SK6812 MINI
- 1x XIAO RP2040
- 1x case (only 3d printed parts)
  no need for diodes as it does not use a matrix but single digital pins
# extra
i have no idea what to tell you but it's my first project ever and hope it inspire someone
