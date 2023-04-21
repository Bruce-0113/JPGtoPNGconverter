import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--target_dir', dest='target_dir', action='store', default='image/', help='the target image directory') 
parser.add_argument('--output_dir', dest='output_dir', action='store', default='output/', help='the output directory') 
parser.add_argument('--verbose', dest='verbose', action='store', default='1', help='whether to print out successful message. 0 : Don\'t print; 1 : Print Successful message.') 
args = parser.parse_args()

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

try :    
    for filename in os.listdir(args.target_dir):
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(f'{args.target_dir}{filename}')
        #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
        img.save(f'{args.output_dir}/{clean_name}.png', 'png')
        if args.verbose == '1' : 
            print('all done!')
except FileNotFoundError :
    print('Please enter correct image directory!')