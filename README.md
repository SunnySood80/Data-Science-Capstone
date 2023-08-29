A crop scanning project to detect and segment diseases and interface with a mobile frontend.

Team 8: Sunny Sood, Rahul Tumula

This project aims to develop an innovative solution for detecting diseases on crops. By leveraging LIDAR technology and a segmentation model, we intend to scan, detect, segment, and then relay the findings to a mobile iOS app for straightforward observation.

In the initial phase, our focus will be on scanning a single plant, segmenting the 3D model to identify diseases. This will be accomplished using the iPhone's built-in LIDAR scanner. Notably, all iPhones from the iPhone 11 onwards are equipped with LIDAR scanning capabilities.

Given the current scarcity of 3D plant disease data, our model will primarily be a 2D segmentation model. After obtaining a 3D scan of a plant, we will identify the most optimal 2D slice within the 3D scan. This slice will then be fed into our model following some preprocessing.

We are currently considering a potential data source listed below. It is among the most extensive and diverse datasets, featuring labeled plant data that encompasses various plants and diseases:

https://www.kaggle.com/datasets/alinedobrovsky/plant-disease-classification-merged-dataset
