from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os 

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1xV_tRXPbjRurN9Tn1a_14eiUTN7zhRAG'

# file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
# file1.SetContentString('Hello world!, this is my second file')
# file1.Upload()

directory = "C:/Users/sarve/OneDrive/Pictures/Camera Roll"
for f in os.listdir(directory):
    filepath = os.path.join(directory,f)
    # print(filepath)
    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
    gfile.SetContentFile(filepath)
    gfile.Upload()