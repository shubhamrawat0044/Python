import subprocess #for running the process/opening them
import os # for checking if the location of the paths are availbale and right or not
import time # using for opening the programs  with a little interval 

#function for opening the programs
def launch_programs(program):
    try:
        subprocess.Popen(program)
        print(f"Program is starting: {program}")
    except:
        print(f"Program not found:{program}")

#programs path stores that i want to open when executing the script its a dict(so that we can use args too)instead of a simple list sys
programs = {
    "chrome":r"C:\Path***************\chrome.exe",
    "vmware": r"C:\Path**************\vmware.exe"
}

#checking for for the program to run through exe file if not it will tell you that the program file path is not correct
def check_program(program):
   if os.path.exists(program):
       return True
   else:
       return False
   
#this part checks for the programs file, if it is there ok launch the program if not thenprint the program name with program not found 
def main():
    for program in programs:
        if check_program(program):
            launch_programs(program)
            time.sleep(3)
        else:
            print(f"Could not start {program}") 

if __name__ == "__main__":
    main()