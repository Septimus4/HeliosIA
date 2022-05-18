from google_drive_downloader import GoogleDriveDownloader as gdd

#Train set
gdd.download_file_from_google_drive(file_id='1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn',
	dest_path='./train.zip')

#Test set
gdd.download_file_from_google_drive(file_id='1bxK5zgLn0_L8x276eKkuYA_FzwCIjb59',
	dest_path='./val.zip')
