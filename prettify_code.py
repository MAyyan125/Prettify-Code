from bs4 import BeautifulSoup
import argparse
import sys

parser=argparse.ArgumentParser(description="This Tool have ability to prettify you'r code :)")
parser.add_argument("-f","--file",help="Specify your target file path")
# parser.add_argument("-o","--output",help="Specify the output path")
args=parser.parse_args()

def out(args):
    with open(args.file,"r") as o:
        z=o.read()
        soup=BeautifulSoup(z,"html.parser")
        return soup.prettify()
        
        
sys.stdout.write(str(out(args)))