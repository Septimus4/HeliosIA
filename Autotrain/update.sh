mkdir ./ScriptsIAHelios
cp -r ../PythonScripts/* ./ScriptsIAHelios/
#Tensorflow
git clone https://github.com/tensorflow/models
cp ./CustomTfScripts/model_main.py ./models/research/object_detection/
cd models/research
python3 setup.py sdist
cd slim && python3 setup.py sdist && cd ../../..

#YOLOv3_Python
git clone https://github.com/AntonMu/TrainYourOwnYOLO
mv TrainYourOwnYOLO/2_Training/src/keras_yolo3 PreModels/YoloV3
rm -rf TrainYourOwnYOLO
cd PreModels/YoloV3/keras_yolo3
wget https://pjreddie.com/media/files/yolov3.weights
python3 convert.py yolov3.cfg yolov3.weights yolo.h5
cp model_data/yolo_anchors.txt ../FilesToTrain/
cp yolo.h5 ../FilesToTrain/