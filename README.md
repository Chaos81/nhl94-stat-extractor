# nhl94-stat-extractor
 
 **NHL94 Save State Stat Extractor version 0.5**

This Python app is designed to extract stats from save states (from RetroArch 1.10+ 64-bit Genesis Plus GX core) and output the data into an XLS file. The XLS file is a spreadsheet that is compatible with MS Excel and other spreadsheet programs.

Instructions:
    - Choose the ROM used to play the game
    - Enter the length of period and number of teams in the ROM
    - Choose the save state to load
    - Click "Extract to XLS..."

    The save state should be one saved at either the Three Stars screen, or the Game End menu. The Length of period is used to calculate the GAA for the goalie. Once complete, it will ask you to choose a location to save the XLS file. If there are any errors, a message will pop up to notify you.

This was written in Python 3.9.6. 

The following modules are needed to run the Python script:
    - PyQt5
    - xlwt
