# **Cotton Plant Disease Pridiction Deep Learning CNN Model**

## *Introduction* -:
Agriculture is the backbone of many countries in South Asia like Bangladesh, China, and India.Cotton is known as ‘white gold’ in the agricultural industry. Agriculture is the primary source of economic income in Bangladesh and the country’s economy is heavily dependent on agriculture. The soil and water resources of our country are fertile and the climate is moderate. But numerous diseases aﬀect crop production and cause enormous crop losses, endangering the lives of helpless farmers. A previous report showed that about 70–80% of cotton diseases were leaf diseases and 30–20% were pest diseases. Experts typically use bare eyes to ﬁnd and identify such plant diseases and pests which may result from lower accuracy of the identiﬁcation. As a result, early detection of cotton disease using AI-based systems may help to increase the production of cotton by detecting the leaf disease signiﬁcantly.

So we use Deep Techniques for model building and provide a best accuracy of model for Agriculture domain.

## *Python Libraries use in this Project* -:
Python Libraries-

Numpy
Matplotlib
Keras

For Deployment-
Flask
Version - check the versions in 'requirements.txt' file.

## *Data Collection* -:
A data set containing images of fresh and diseased cotton leaf and plants are collected from Kaggle.com as part of a competition. This data set is comprised of four image types: fresh cotton leaf, fresh cotton plant, diseased cotton leaf and diseased cotton plant with unique images. For example, 2 and 3 represent the fresh and aﬀected samples of the dataset.

## *Data Analysis and Preprocessing* -:
The real image of the dataset is not always fresh and hence may contain noise in the data. Before attempting to ﬁt them into the learning module, it is necessary to preprocess them for better accuracy and per-formance of the module. This refers to the process of preparing the data for further use, which may involve integrating, cleaning, normalization, or transforming the data. In our case, we apply the some types of operation - Resize, Rescaling, zooming etc.

## *Model Building With Convolutional neural network (CNN) Model* -:
Train the data using CNN and apply the some tradisional features like resize, rescaling, or build a model with 98% accuracy. Model will give perfect accuracy after increasing the number of epochs. We use maxpooling layers with each or affected position.You can see summary detail of model using model.summary function.The data has droped three times with building model at 0.2, 0.5, and 0.75.

## *Model accuracy, Evaluation, or Test* -:
Model is giving 98% accuracy with the better validation accuracy and
tested confusion Matrix, classification report, precision or recall scores.

There is some parameter chenges for model building.
Learning Rate  - 0.001
Dropout        - 0.2
Optimizer      - Adam
Loss           - SparseCategoricalCrossentropy
etc.
We plotted the Accuracy or Losses at Chart.

## *Deployment of the Project* -:
This is a complete Project of cnn so we Deployed at heroku
we use Flask Python library for backend.

# **Project End**