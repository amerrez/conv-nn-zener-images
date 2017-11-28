Contributors :

Amer Rez            
Kunal Deshmukh      
Thinh Nguyen        

Pre Req:
Pytohn2.7 with numpy and Pillow
Tensorflow

Example command to run the code:
python zener_generator.py data 1000
python conv_train.py cross lenet_5 0.001 100 S model_name data

conv_train arguments description:
<mode> <network_description> <epsilon> <max_updates> <class_letter> <model_file_name> <data_folder>

This file produces a graph for Question 1 among other statistics like Training
Cost,Validation cost as well as training and validation statistics.

Possible modes are :
cross,cross-l1,cross-l2,test. test mode is can be used to test a already
developed model using test data.
If test mode is used epsilon, max_updates will be required.
