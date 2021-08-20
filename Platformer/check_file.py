from pathlib2 import Path

if Path('assets/platform_level_01.tmx').is_file():
    print("File exists")
else:
    print("File does not exist")