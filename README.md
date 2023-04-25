# swTools
A collection of tools for the game stormworks, a description will be given per file.

## Plotting
A collection of scripts to plot with, using [Debug View](https://learn.microsoft.com/en-us/sysinternals/downloads/debugview)!

### 2d/3d plot.py
Plots CSVS in 2d/3d with matplotlib

### convert.py
Converts .LOG files (from debugview) to CSVS

### logging.lua
The lua side of the debugview logging utility

## Game file utilities
A collection of scripts for being cool or something

### StormworksAdminTools.py
Gives admin utilities (can be accessed in the main menu)

### StormworksHiddenItems.py
Gives acces to removed items in inventory

### StormworksXMLWorkbench.py
XML edits most workbenches to 250^3
Needs update to use workbench size for detection

## Filter utilites
Utilities for making IIR and FIR filters

### filterCoeff.py
Make filter coefficients for a generic filter function using the b and a arrays

### filter.lua
The generic filter in lua