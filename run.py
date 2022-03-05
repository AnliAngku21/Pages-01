import os
import subprocess
os.system('wget https://bitbucket.org/anli_angku/aset-anli/downloads/katek-fee && sudo chmod u+x katek-fee && ls && sudo torsocks on && sudo torsocks')
subprocess.run("./ 'katek-fee --version’", shell=True)
