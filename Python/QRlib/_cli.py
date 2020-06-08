import sys
import os

def Cline():
    
    if(len(sys.argv)<2):
        print('an argumet is required ("-h" or "--help")')
        sys.exit()
        
        
    if('-h' in sys.argv or '--help' in sys.argv):
        print(os.system("pip show QRlib"))
        print("")
        print("")
        print(help("QRlib"))
        
    elif('-u' in sys.argv or '--update' in sys.argv):
        os.system("python -m pip install --upgrade QRlib")
    
    else:
        print("Got An Unexpected Argument")