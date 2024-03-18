# StarCitizenControllerCfg
A python application that allows a better customization of Star Citizen controller mapping. It has 2 components:
1. An application that loads an image and allows the user to click with the mouse and name each button.
2. Another application that allows mapping each button to a specific action.
   2.1 The mapping should have the same layout as in SC configuration meniu.
   2.2 It should provide posibility to invert some controller's axis right after selecting it for.
   2.3 A nice to have feature has to be to show for each mapping just like SC, what else is mapped to the same controll.
   2.4 We need a way to show the user which controlls can interfere with each other, based on the modes and ground / flight vehicle etc..


To use the listGameControllersWindows.py one must install following dependency:
pip install pywinusb

To use the tabelizer.py one must install following:
pip install matplotlib Pillow numpy

