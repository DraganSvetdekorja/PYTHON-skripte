# python  script to copy from folder subfolders selected with explorer to ftp folder all pictures with jpg extension
# show transfer progress

# ftp hostname: ftp.svetdekorja.si
# port: 21
# username: svetdeko
# password: INTERCONTsvet_112!
# remote folder to upload pictures: /public_html/slike_svetdekorja


import os
import ftplib

def upload_file(ftp, local_path, remote_path):
    with open(local_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_path}', file)

def upload_folder(ftp, local_folder, remote_folder):
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                local_path = os.path.join(root, file)
                remote_path = os.path.join(remote_folder, os.path.relpath(local_path, local_folder))
                remote_path =  remote_folder				
                upload_file(ftp, local_path, remote_path)
                print(f'Uploaded: {local_path}')

def main():
    # FTP server credentials
    hostname = 'ftp.svetdekorja.si'
    port = 21
    username = 'svetdeko'
    password = 'INTERCONTsvet_112!'
    remote_folder = '/public_html/slike_svetdekorja'

    # Local folder path to copy pictures from
    local_folder = input('Enter the path of the folder to copy from: ')

    # Connect to the FTP server
    ftp = ftplib.FTP()
    ftp.connect(hostname, port)
    ftp.login(username, password)

    # Set binary mode for file transfer
    ftp.sendcmd('TYPE i')

    # Upload pictures
    upload_folder(ftp, local_folder, remote_folder)

    # Disconnect from the FTP server
    ftp.quit()

if __name__ == '__main__':
    main()


