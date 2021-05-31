import os
import dropbox

class Transfer_Data:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,folder_from,folder_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(folder_from):
            for file_name in files:
                new_location =os.path.join(root,file_name)
                relative_path=os.path.relpath(new_location,folder_from)
                dropboxpath=os.path.join(folder_to,relative_path)
                f=open(folder_from,'rb')
                dbx.files_upload(f.read(),dropboxpath)

def Main():
    access_token="dLPIWFUTxzwAAAAAAAAAAaIzYbD6han8HnLmY6i2e3CHTqkQ1xAreulMzlREK6hE"
    transfer_data=Transfer_Data(access_token)
    folder_from=input("Which folder do you want to upload: ")
    folder_to=input("Where do you want to upload the folder: ")
    transfer_data.upload_files(folder_from,folder_to)
    print ("Folder has been moved")
Main()




