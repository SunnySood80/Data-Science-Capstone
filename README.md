A crop scanning project to detect and segment diseases and interface with a mobile frontend.


This project aims to develop an innovative solution for detecting diseases on crops. By leveraging LIDAR technology and a segmentation model, we intend to scan, detect, segment, and then relay the findings to a mobile iOS app for straightforward observation.

In the initial phase, our focus will be on scanning a single plant, and using a segmentation model to segmenent the 3D model and to identify the diseases. This will be accomplished using the iPhone's built-in LIDAR scanner. Notably, all Pro iPhone models from the iPhone 12 Pro onwards are equipped with LIDAR scanning capabilities.

Given the current scarcity of 3D plant disease data, our model will primarily be a 2D segmentation model. After obtaining a 3D scan of a plant, we will identify the most optimal 2D slice within the 3D scan. This slice will then be fed into our model following some preprocessing. Afterwards the 2D slice will be projected back onto the 3D model

Once we have established our small scale Iphone crop scanning app, we will increase the scale of the project and possibly add a drone as well as an actual LIDAR camera to scan numerous crops to check for crop disease and push to our mobile app for an interactive model of the crop field with the classified crops.

This plan is subject to change in regarding to our available technology and materials.

We are currently considering a potential data source listed below. It is among the most extensive and diverse datasets, featuring labeled plant data that encompasses various plants and diseases:

https://www.kaggle.com/datasets/alinedobrovsky/plant-disease-classification-merged-dataset
