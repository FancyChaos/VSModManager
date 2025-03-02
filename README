# VSModManager

An extremely simple [Vintage Story](https://www.vintagestory.at/) mod manager following the KISS prinicple. Written for all Linux distributions.

## Features

1.  Single python file wihout ANY dependencies to external or third-party libraries. If you have python installed, you can use this mod manager.
2. Install a mod by their *modid* (Should generally be the name of the mod)
3. Update all installed mods or a single one by their modid/modname
4. Remove installed mod by their modid/modname
5. List all installed mods or specific information about a single one
6. Backup the /Mods/ folder

## Usage

This mod manager can be used as an interactive CLI application or non-interactively by passing the required arguments and action directly to it.

First mark the python file as an executable

	chmod +x vsmodmanager

Make the user who uses this mod manager has the permission to see/edit the vintage story data folder.

### Interactive mode

	./vsmodmanager

### Non-interactive mode

	./vsmodmanager -d <data_path> -v <game_version> <action> [mod]

#### Caveats

The Non-interactive mode does not require any further input from the user. Due to that fact only sane decisions are made to gurantee stability.  A mod for example will ONLY be installed/updated if the target game version of it matches the given game version exactly.

Use the interactive mode if you want to install/update a mod that is not made for your specific game version. 

### Examples

Following examples for the Non-interactive mode. The interactive mode should hopefully be self-explanatory

1. List all installed mods
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -l`
2. List information about one specific mod
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -l knapster`
3. Install a mod
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -i morepiles`
4. Update a single mod
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -u morepiles`
5. Update all installed mods
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -u`
6. Remove a mod
`./vsmodmanager -d /var/vintagestory/data/ -v 1.20.3 -r morepiles`

For more see the help text
`./vsmodmanager -h`

## Planned

1. Minor code cleanup
2. Easier to read/understand output
3. Colorful output

