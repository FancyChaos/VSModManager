#!/usr/bin/env python3

import zipfile
import json
from prompt_toolkit import PromptSession
from pathlib import Path

data_path_default = Path('/var/vintagestory/data')


class Mod:
    def __init__(self, archive: Path):
        self.archive = archive
        self._parse_archive()

    def __getattr__(self, name: str):
        try:
            return self.modinfo[name]
        except Exception:
            return ''

    def _parse_archive(self):
        '''
        Parse a mod archive
        '''
        with zipfile.ZipFile(self.archive, 'r') as archive:
            self._modinfo_string = archive.read('modinfo.json').strip()

            # TODO: Error Handling
            self._modinfo_raw = json.loads(self._modinfo_string)

            # Convert keys to all lowercase for easy access
            self.modinfo = {k.lower(): v for k, v in self._modinfo_raw.items()}

    def print_default(self):
        print('{name} ({modid}) [{version}] - {desc}'.format(
            name=self.name or 'UNKNOWN',
            modid=self.modid or 'ModID unknown',
            version=self.version or 'Version unknown',
            desc=self.description or 'No description'
        ))

    def print_all(self):
        print(f'Mod located at "{self.archive}":')
        print()
        for k, v in self.modinfo.items():
            print(f'{k}: {v}')

    def _check_update(self):
        '''
        Check if updates are available and save available
        versions in sorted list
        '''
        pass

    def remove(self):
        '''
        Remove myself
        '''

    def update(self, version):
        '''
        Update mod to given version
        '''
        pass


class ModManager:
    mods = []

    def __init__(self, data_path=None):
        self.data_path = data_path
        if not self.data_path:
            self.data_path = data_path_default

        self.mods_path = self.data_path / 'Mods'

        self._mods_refresh()

    def _mods_refresh(self):
        '''
        Iterate over all mods in the mods directory and save them
        for further use
        '''
        mod_archives = [
            f for f in self.mods_path.iterdir()
            if zipfile.is_zipfile(f)
        ]

        self.mods = [
            Mod(f) for f in mod_archives
        ]

    def _mods_get(self, modid: str):
        '''
        Get list of mods by modid or name (fallback)
        '''
        modid = modid.lower()

        return [
            mod for mod in self.mods
            if modid in (mod.name.lower(), mod.modid.lower())
        ]

    def mods_lists(self):
        '''
        Pretty print list of installed mods
        '''
        for mod in self.mods:
            mod.print_default()

    def mod_list(self, modid):
        '''
        List all modinfo field of singular mod by modid or general name
        '''
        for mod in self._mods_get(modid):
            mod.print_all()

    def mod_install(self):
        '''
        Install a mod by modid  (Maybe even by name if modid does not match)
        '''
        pass

    def mod_remove(self, modid):
        '''
        Remove by name modid or general name (fallback)
        '''
        pass


helptext = '''VSModManager commands
list [name]
    - list all available mods or information about a single one'''

if __name__ == '__main__':
    session = PromptSession()
    modmanager = ModManager()

    while True:
        try:
            cmd = session.prompt('> ').lower().strip().split()
            if not cmd:
                print(helptext)
                continue
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

        cmd_main = cmd[0]
        if cmd_main == 'list':
            if len(cmd) > 1:
                modmanager.mod_list(' '.join(cmd[1:]))
            else:
                modmanager.mods_lists()
        else:
            print(helptext)

    print('Exiting VSModManager...')
