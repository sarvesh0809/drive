from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
folder = '1xV_tRXPbjRurN9Tn1a_14eiUTN7zhRAG'
file1 = drive.CreateFile({'title': '11AA1113',
                          'mimeType': "application/vnd.google-apps.folder",
                          'parents': [{"kind": "drive#fileLink", "id": folder}]})
file1.Upload()
folder_id = file1['id']
file2 = drive.CreateFile({'title': 'filename.jpg',
                          'mimeType': 'image/jpeg',
                          'parents': [{"kind": "drive#fileLink", "id": folder_id}]})
file2.SetContentFile('721078.jpg')
file2.Upload()
permission=file2.InsertPermission({
                            'type': 'anyone',
                            'value': 'anyone',
                            'role': 'reader'})

link=file2['alternateLink']
link=link.split('?')[0]
link=link.split('/')[-2]
link='https://drive.google.com/file/d/'+link+'/view?usp=sharing'
print(link)