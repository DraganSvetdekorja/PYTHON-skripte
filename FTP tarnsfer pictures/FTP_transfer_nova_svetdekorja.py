import os
import ftplib
from tqdm import tqdm


def upload_files_ftp(local_path, remote_path, ftp_host, ftp_port, ftp_username, ftp_password):
    with ftplib.FTP() as ftp:
        # Connect to the FTP server
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_username, ftp_password)

        # Change to the desired remote directory
        ftp.cwd(remote_path)

        # Iterate through all subdirectories and files in the local_path
        for root, dirs, files in os.walk(local_path):
            for file in files:
                if file.lower().endswith(".jpg"):
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(remote_path, file)
                    with open(local_file_path, "rb") as f:
                        # Upload the file in binary mode
                        ftp.storbinary(f"STOR {remote_file_path}", f)

                    print(f"Uploaded: {remote_file_path}")

        # Close the FTP connection
        ftp.quit()


# Example usage
local_path = input("Enter the local folder path: ")
remote_path = "/nova.svetdekorja.si/pub/media/slike_svetdekorja/"
ftp_host = "th3.neoserv.si"
ftp_port = 21
ftp_username = "svetdeko"
ftp_password = "sa2sirup"

upload_files_ftp(local_path, remote_path, ftp_host, ftp_port, ftp_username, ftp_password)
