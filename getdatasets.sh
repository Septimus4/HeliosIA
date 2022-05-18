mkdir traindatasets && cd traindatasets

### DOWNLOAD
#VisDrone_Vid_train - vd_vidtrain.zip
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1NSNapZQHar22OYzQYuXCugA3QlMndzvw' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1NSNapZQHar22OYzQYuXCugA3QlMndzvw" -O vd_vidtrain.zip && rm -rf /tmp/cookies.txt
#VisDrone_Vid_val - vd_vidval.zip
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1xuG7Z3IhVfGGKMe3Yj6RnrFHqo_d2a1B' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1xuG7Z3IhVfGGKMe3Yj6RnrFHqo_d2a1B" -O vd_vidval.zip && rm -rf /tmp/cookies.txt
#VisDrone_Pic_train - vd_pictrain.zip
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn" -O vd_pictrain.zip && rm -rf /tmp/cookies.txt

### ZIP
sudo apt install unzip
unzip vd_vidtrain.zip && unzip vd_vidval.zip && unzip vd_pictrain.zip

### PREPARE
cd VisDrone2019-DET-train/
mv annotations/* . && mv images/* .
rm -rf annotations/ images/

### CONVERT
cd ../../Ressources
python3 main_toyolov3.py ../traindatasets/VisDrone2019-DET-train/
python3 video_toyolov3.py ../traindatasets/VisDrone2019-VID-train/
python3 tog.py pic_train_data.txt video_train_data.txt output.txt
python3 video_toyolov3.py ../traindatasets/VisDrone2019-VID-val/
python3 tog.py output.txt video_train_data.txt train_data.txt

### EXPORT
cp train_data.txt ../Autotrain/PreModels/YoloV3/FilesToTrain/