#!"C:\Users\ethan\OneDrive\Documents\University\Year 4\Term 2\COSC 310\TherapistJen\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.2','console_scripts','pip'
__requires__ = 'pip==19.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==19.0.2', 'console_scripts', 'pip')()
    )
