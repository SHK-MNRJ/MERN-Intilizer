import argparse
import os
import subprocess
import time

def creatFolder(folderName):
    os.mkdir(folderName)

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--project", help = "Project Name")

args = parser.parse_args()
projectTitle=args.project
print(type(args.project),args.project)

subprocess.run(f"mkdir {projectTitle}",shell=True, check=True)

os.chdir(f"{projectTitle}")

os.mkdir("frontend")
os.mkdir("backend")

time.sleep(2)
os.chdir("frontend")

print(f"npm create vite@latest . -- --template react")
subprocess.run(f"npm create vite@latest . -- --template react",shell=True, check=True)
subprocess.run("npm install",shell=True, check=True)

subprocess.run("npm i react-router-dom axios",shell=True, check=True)
print("in frontend")

os.chdir("..")
os.chdir("backend")

print("in backend")

subprocess.run("npm init -y",shell=True, check=True)
subprocess.run("npm i nodemon dotenv http helmet mysql2 cors express body-parser",shell=True, check=True)

'''
[FE]
npm create vite@latest . -- --template react
npm install
npm i react-router-dom axios

[BE]

npm init -y
npm i nodemon dotenv http helmet mysql2 cors express body-parser
'''
