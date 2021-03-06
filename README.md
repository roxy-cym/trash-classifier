# Trash-classifier
 <div align=center>                                                                                                       
<img width="350" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/top.jpg">                                          
<img width="350" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/right.jpg"> 
</div>

# Introduction
Garbage classification plays an important role in our environment. It contributes to further resource utilization and converts garbage into public resources. It is a long-term and systematic project. It seems that it is difficult to see obvious results in the short term. But in the long run, garbage classification is of great significance to people in improving and protecting their living environment.

Last term, I made a bin that can automatically open-close. This term, I continued this theme and made a device that can classify five types of garbage: glass, metal, plastic, paper, and cardboard. In this project, I used Edge impulse and Lobe to train a machine learning model. Then I loaded the model onto a Raspberry pi to make it usable, as well as applied a webcam and LEDs to visualize the results of the model prediction. 
<div align=center><img width="350" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/img1.png"/></div>

#  Research question
Using model learning model to identify five types of garbage ( glass, metal, plastic, paper, cardboard ).
# Application overview
There are two essential building blocks of this project, which are software and hardware. The main task of the software block is to train a model that can classify the garbage types correctly. The hardware task is to capture photos using a webcam and turn on the corresponding LED according to the output of the ML model prediction.

I used Edge impulse to train my ML model. The accuracy of the model at the beginning is relatively low, about 6%. In order to improve the accuracy, I did some experiments, which included changing models and parameter settings. The accuracy increased from 6% to 78.9%. After finishing model training, I converted the model files into TensorFlow lite format and uploaded the lite files onto the raspberry pi. I created a python script to call the Ml model, let the webcam take pictures, and turn on the LED. Example pictures for camera vision are shown below:
<div align=center>                                                                                                       
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/image1.jpg">                                         
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/image2 .jpg"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/image3 .jpg">
</div>
The workflow of the hardware part is that when I charge the raspberry pi and run the python script in the terminal. It will load the model and call the webcam. When the webcam is ready to capture an image, the light at the left top of the device (red LED) will turn on. Once the cam has taken an image, it will be put in ML model and output a result. The output determines which light will turn on: yellow (glass), blue (cardboard), green (metal), white(paper), or red ( plastic). After the LED turns off, the status light starts pulsing again, and the webcam retakes the photo.


In order to protect raspberry pi, hold the camera and place the LEDs, I referred to pi cases online [1] and made some changes to satisfy my requirements. 
<div align="center"><img width="350" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/case.jpg"></div>

# Data
The initial data I used is the Garbage Classification Dataset on Kaggle[2]. The dataset consisted of 2340 images and five classifications: cardboard (393), glass (491), metal (400), paper(584), and plastic (472)[2]. Example pictures for each category are shown below:
 <div align=center>                                                                                                       
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/cardboard1.jpg">                                         <img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/glass1.jpg"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/metal1.jpg">
</div>
<div align=center>
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/paper1.jpg"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/plastic1.jpg"> 
</div>                                                                                                             
The 2340 images were split into training and testing data according to the 80% and 20% proportions, which is 1820 images of training data and 468 images of testing data.

Most of the experiments in this project are carried out on the basis of Kaggle data. In order to test the impact of the amount of data on the accuracy of the model. I added my own data. The data consisted of cardboard (100), glass (100), metal (100), paper(100), and plastic (100). The majority of the data was collected using a mobile phone, taking photos of items(5 types) at my home. Example pictures for each category are shown below:
<div align=center>                                                                                                       
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/cardboard.jpeg">                                           <img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/glass.JPG"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/metal.jpeg">
</div>
<div align=center>
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/paper.JPG"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/plastic.JPG"> 
</div>  

The first processing of the picture is resizing the pictures. There are two kinds of picture pixels on edge impulse, 96x96 and 160x160, respectively. The accuracy of the model is higher at 160x160 pixels, so in this project, I set picture pixels as 160x160. Another parameter which is colour depth, was set to RGB. All objects in the dataset have their own colour. So, colour is also one of the significant factors for garbage classification.

# Model
- Transfer learning  
Under transfer learning, there are many different models in the Edge impulse. As can be seen in Table below .
The MobileNet focus on lightweight CNN networks in mobile or embedded devices. Compared with the traditional convolutional neural network, the model parameters and the amount of computation are greatly reduced on the premise that the accuracy rate is slightly reduced[3]. In the MobileNet v2 network, compared with the MobileNet V1 network, the accuracy rate is higher, and the model is smaller.
<div align=center><img width="600" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table1.png"/></div>  

- CNN  
In the field of pattern recognition and classifications, convolution neural networks (CNN) also show excellent success. For CNN, the dataset need to do more preprocessing, but with transfer learning, little processing of the dataset need to be done, like resizing to 96 x 96 or 160 x160 according to selected Pre-trained Models (MobileNetV1&MobileNetV2). This saves much time for preprocessing data. Pretrained Models provides much greater accuracy for completely new dataset such as image dataset. As I use transfer learning for this project gives higher accuracy. In comparison, CNN gives lesser accuracy than transfer learning.  
- Difference  
**Advantages of Transfer Learning**
	1. Transfer learning is useful for insufficient data and imbalanced class problems. So that we can limit training data and training time, it can give nearly a hundred percent of accuracy for less amount of data.
	2. Transfer learning gives a good combination of features even for the very complex task within a short time frame.
	
   **Disadvantages of CNN**
  	1. Training a convolutional neural network takes a long time, especially with massive datasets.

# Experiments
I conducted some experiments on several parameters, as shown in below table 2.
<div align=center><img width="600" height="400" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table2.png"/></div>

The table below shows the result of all the experiments that I did. The accuracy is the accuracy of testing data. The experiments were divided into six groups. I marked the changed parameters in red and added a grey background colour to the data with the highest accuracy, and the next group of experiments will be performed on this data. For example, the changed parameters of the first group were model, resolution and width multiplier. Row 4 has the highest accuracy, which is 77.9%. And next experiments, except for the changes of the neurons, the rest of the parameter settings will keep the same with Row 4 until a higher value appears.
<div align=center><img width="700" height="400" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table3.png"/></div>
<div align=center><img width="700" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table4.png"/></div>

- Model selection
As can be seen in these two tables, the selection of the model has the most significant impact on the model accuracy. Although we can change various parameter settings, it can only slightly improve the accuracy. According to the model testing, the accuracy under the NN model is around 50%, but the accuracy under the transfer learning is over 70%, so I choose to use transfer learning.
- Parameter settings
It can be seen from the experimental result that the larger the value of the resolution and width multiplier of the model, the higher the accuracy. The number of neurons and epochs is not as good as possible with the number increasing. Toggled on the auto-balance dataset and data argumentation didn't achieve a better result.
- Adding more images
At first, I thought that as long as the amount of data increased, the accuracy could be increased, so I didn't pay attention to any details, and randomly took photos of items belonging to these five categories. But when I experimented, the accuracy decreased, which led me to think why. Then I realized that the images that I captured have lots of noise, which affects the recognition correctness of the model to a large extent. For example, a item has many material, many items in a image, the background is not pure and so on. All of these conditions will affect the accuracy of the model prediction. Only pure data can improve accuracy.
<div align=center>
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/multi-material.png"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/multi-objects.png">
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/not pure background.png"> 
</div> 

- Relabeling the images
For those testing data, they have the wrong prediction. I relabeled them based on my cognition. Here I used the Lobe platform, which can relabel pictures very quickly.

 # Results
According to the experiment, the choice of the model has the greatest impact on the accuracy. Therefore, in the experiment, we must first select a suitable model and then change the settings of other parameters to obtain a model with high accuracy. However, it should also be noted that the value of the parameter is not as large as possible, and more experiments are required to find the optimal value.
<div align=center><img width="400" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/result.png"/></div>

Sometimes the device will output a wrong prediction. Errors are mainly concentrated in misjudgment of glass and plastic. Because they have lots of similarities. For instance, if there is a transparent glass, the output might be plastic; if there is a transparent plastic bottle, the output might be glass. In the future I will try to increase the amount of data in these two categories to improve the accuracy of the model
<div align=center><img width="400" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/error.png"/></div>

Due to platform limitations, the settings of some parameters cannot be tested, and the job always fails. If there is enough time, I will use Colab to assist the experiments.

# Reference
 1. N.d. URL https://cdn.thingiverse.com/assets/54/c8/f3/cd/5a/Raspberry_Pi_Case_2.stl (accessed 4.25.22b).
 2. cchangcs, n.d. Garbage Classification [WWW Document]. Kaggle. URL https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification (accessed 4.25.22).
 3. Pujara, A., 2020. MobileNet Convolutional neural network .Machine Learning Algorithms. Analytics Vidhya. 
 4. Shalash, W.M., 2019. Driver Fatigue Detection with Single EEG Channel Using Transfer Learning, in: 2019 IEEE International Conference on Imaging Systems and Techniques (IST). IEEE.
 5. Tiyajamorn, P., Lorprasertkul, P., Assabumrungrat, R., Poomarin, W., Chancharoen, R., 2019. Automatic Trash Classification using Convolutional Neural Network Machine Learning, in: 2019 IEEE International Conference on Cybernetics and Intelligent Systems (CIS) and IEEE Conference on Robotics, Automation and Mechatronics (RAM). IEEE.
 6. Gao, L., Liu, Z., Shen, L., Shi, S., Lv, Y., 2021. A Research on Intelligent Classification of Urban Trash Bins Based on Machine Learning. Proceedings of International Conference on Artificial Life and Robotics 26, 712???715. https://doi.org/10.5954/icarob.2021.os12-16

# Resources
video link https://youtu.be/brmlQnhjAQU  
Edge Impulse page : https://studio.edgeimpulse.com/studio/85812/validation
