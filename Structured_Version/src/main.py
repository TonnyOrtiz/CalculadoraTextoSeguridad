import os
import sys
from controller.controller import Controller

# Set working directory to the directory where the main script is located
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

def main():
    controller = Controller()
    controller.run()

if __name__ == "__main__":
    main()