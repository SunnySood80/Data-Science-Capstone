# Data-Science-Capstone
A crop scanning project to detect and segment a disease and push to a mobile front end

Team 8: Sunny Sood, Rahul Tumula

This project will find a innovative solution to detecting a disease on a crop using LIDAR technology and a segmentation model to scan, detect, and segment then push to a mobile IOS app for easy observation.

For the beginning process of this project, we will focus on scanning only on one plant for now segmenting the 3D model for disease, and doing so using the iphone's built in LIDAR scanner. All iphones above the iphone 11 have LIDAR scanning capabilities.

As of now, the model will consist of a 2D segmentation model of which we will use since not many instances of 3D plant disease data is available. We will a 3D scan of a plant and select the most optimal 2D slice within the 3D scan, then feed it into our model after some preprocessing.

Here is a potential data source we are looking at, it is one of the largest most diverse datasets of available labeld plant data with different plants and different diseases:

https://www.kaggle.com/datasets/alinedobrovsky/plant-disease-classification-merged-dataset
