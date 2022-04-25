# Trash-classifier
# Introduction
Garbage classification plays an important role in our environment. It contributes to further resource utilization and converts garbage into public resources. It is a long-term and systematic project. It seems that it is difficult to see obvious results in the short term. But in the long run, garbage classification is of great significance to people in improving and protecting their living environment.

Last term, I made a bin that can automatically open-close. This term I continued this theme and made a device that can classify the garbage types according to the real-time images.
<div align=center><img width="350" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/img1.png"/></div>

This project uses a machine learning model trained in Edge impulse and Lobe to identify five types of garbage, which are glass, metal, plastic, paper, cardboard, respectively. The model is then loaded onto a Raspberry pi to make it usable wherever there are rubbish bins. 


#  Research question
Using model learning model to identify five types of garbage ( glass, metal, plastic, paper, cardboard ).
# Application overview
There are two essential building blocks of this project, which are software and hardware. The main task of the software block is to train a model that can classify the garbage types correctly. The hardware task is to capture photos using a webcam and turn on the corresponding LED according to the output of the ML model.

I used Edge impulse to train my ML model. The accuracy of the model at the beginning is relatively low, about 6%. In order to improve the accuracy, I did some experiments, which included changing models and parameter settings. The accuracy increased from 6% to 78.9%. After finishing model training, I converted the model files into TensorFlow lite format and uploaded the lite files onto the raspberry pi. I created a python script to control all the hardware components and combine the software and hardware functions. 

The workflow of the hardware part is that when I charge the raspberry pi and run the python script in the terminal. It will load the TensorFlow library and the Lobe ML model. When the program is ready to capture an image, the status light at the left top of the device (red LED) will pulse. Once the cam has taken an image, the program will put the image to the Lobe ML model and output the resulting prediction. The output determines which light will turn on: yellow (glass), blue (cardboard), green (metal), white(paper), or red ( plastic). After the LED turns off, the status light starts pulsing again, and the webcam retakes the photo.

In order to protect raspberry pi, hold the camera and place the LEDs, I referred to pi cases online [1] and made some changes to satisfy my requirements. 

# Data
The initial data I used is the Garbage Classification Dataset on Kaggle[2]. The dataset consisted of 2340 images and five classifications: cardboard (393), glass (491), metal (400), paper(584), and plastic (472). Example pictures for each category are shown below:
 <div align=center>                                                                                                       
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/cardboard1.jpg">                                           <img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/glass1.jpg"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/metal1.jpg">
</div>
<div align=center>
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/paper1.jpg"> 
<img width="250" height="250" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/plastic1.jpg"> 
</div>                                                                                                             
The 2340 images were split into training and testing data according to the 80% and 20% proportions, which is 1820 images of training data and 468 images of testing data.

Most of the experiments in this project are carried out on the basis of Kaggle data. In order to test the impact of the amount of data on the accuracy of the model. I added my own data. The data consisted of cardboard (100), glass (100), metal (100), paper(100), and plastic (100). The majority of the data was collected using a mobile phone, taking photos of items at my home, and the remaining data were collected on the Internet. In the following experiments, the training data consisted of 2220 images, and the testing data consisted of 568 images.

The first processing of the picture is resizing the pictures. There are two kinds of picture pixels on edge impulse, 96x96 and 160x160, respectively. The accuracy of the model is higher at 160x160 pixels, so in this project, I set picture pixels as 160x160. Another parameter which is colour depth, was set to RGB. All objects in the dataset have their own colour. So, colour is also one of the significant factors for garbage classification.

# Model
- Transfer learning  
Under transfer learning, there are many different models in the Edge impulse. As can be seen in Table 1 .
The MobileNet focus on lightweight CNN networks in mobile or embedded devices. Compared with the traditional convolutional neural network, the model parameters and the amount of computation are greatly reduced on the premise that the accuracy rate is slightly reduced. In the MobileNet v2 network, compared with the MobileNet V1 network, the accuracy rate is higher, and the model is smaller.
<div align=center><img width="600" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table1.png"/></div>  

- CNN  
In the field of pattern recognition and classifications, convolution neural networks (CNN) also show excellent success. For CNN, you need to do more preprocessing of the dataset, but with transfer learning, you only need to do little processing of the dataset, like resizing to 96 x 96 or 160 x160 according to selected Pre-trained Models (MobileNetV1&MobileNetV2). This saves much time for preprocessing data. Pretrained Models provides much greater accuracy for completely new dataset such as image dataset. As I use transfer learning for this project gives higher accuracy. In comparison, CNN gives lesser accuracy than transfer learning.  
- Difference  
**Advantages of Transfer Learning**
	1. Transfer learning is useful for insufficient data and imbalanced class problems. So that we can limit training data and training time, it can give nearly a hundred percent of accuracy for less amount of data.
	2. Transfer learning gives a good combination of features even for the very complex task within a short time frame.
	
   **Disadvantages of CNN**
  	1. Training a convolutional neural network takes a long time, especially with massive datasets.

# Experiments
I conducted some experiments on several parameters, as shown in below table 2.
<div align=center><img width="600" height="400" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table2.png"/></div>

The table below shows the result of all the experiments that I did. The accuracy is the accuracy of testing data. The experiments were divided into six groups. I marked the changed parameters in red and added a grey background colour to the data with the highest accuracy, and the next group of experiments will be performed on this data. For example, the changed parameters of the first group were model, resolution and width multiplier. Row 4 has the highest accuracy, which is 77.9%. and next experiments will be carried out on this data until a higher value was appeared.
<div align=center><img width="700" height="400" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table3.png"/></div>
<div align=center><img width="700" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/table4.png"/></div>

- Model selection
As can be seen in these two tables, the selection of the model has the most significant impact on the model accuracy. Although we can change various parameter settings, it can only slightly improve the accuracy. According to the model testing, the accuracy under the NN model is around 50%, but the accuracy under the transfer learning is over 70%, so I choose to use transfer learning.
- Parameter settings
- Adding more images
I thought adding more images would increase the model accuracy. On the contrary, the accuracy decreased. Then I realized that the images that I captured have lots of noise, which affects the recognition correctness of the model to a large extent. For example, many items in a image, the background has a colour and so on. So only pure data can improve accuracy.

- Relabeling the images
For those testing data, they have the wrong prediction. I relabeled them based on my cognition. Here I used the Lobe platform, which can relabel pictures very quickly.

 # results
According to the experiment, the choice of the model has the greatest impact on the accuracy. Therefore, in the experiment, we must first select a suitable model and then change the settings of other parameters to obtain a model with high accuracy. However, it should also be noted that the value of the parameter is not as large as possible, and more experiments are required to find the optimal value.
<div align=center><img width="400" height="200" src="https://github.com/roxy-cym/trash-classifier/blob/main/imgs/result.png"/></div>

Sometimes the device will output a wrong prediction. Errors are mainly concentrated in misjudgment of metal, paper and plastic. Because most of the objects have their own colour, which will increase the difficulty of classification. and the model can easily give out worry predictions. For instance, if there is a transparent glass, the output might be plastic; if there is a transparent plastic bottle, the output might be glass, and if the glass or plastic has colour, the output might be metal.

Due to platform limitations, the settings of some parameters cannot be tested, and the job always fails. If there is enough time, I will use Colab to assist the experiments.

# Reference
 1. N.d. URL https://cdn.thingiverse.com/assets/54/c8/f3/cd/5a/Raspberry_Pi_Case_2.stl (accessed 4.25.22b).
 2. cchangcs, n.d. Garbage Classification [WWW Document]. Kaggle. URL https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification (accessed 4.25.22).
 3. Shalash, W.M., 2019. Driver Fatigue Detection with Single EEG Channel Using Transfer Learning, in: 2019 IEEE International Conference on Imaging Systems and Techniques (IST). IEEE.

# Resources
video link https://youtu.be/brmlQnhjAQU
