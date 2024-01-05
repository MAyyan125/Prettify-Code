from bs4 import BeautifulSoup
import argparse
try:
 parser=argparse.ArgumentParser(description=f"This Tool have ability to prettify you'r code :)")
 parser.add_argument("-f","--file",help="Specify your target file path")
# parser.add_argument("-o","--output",help="Specify the output path")
 args=parser.parse_args()

 def out(args):
    with open(args.file,"r") as o:
        z=o.read()
        soup=BeautifulSoup(z,"html.parser")
        return soup.prettify()
 print(str(out(args)))  
except TypeError:
    print("Specify file path using -o or use -h for help")
