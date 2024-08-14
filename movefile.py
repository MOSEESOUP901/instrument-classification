import os 

path = r"D:\dataset\audio"
files = os.listdir(path)
labels = {}

for file in files:
    label = file.split('_')[0]
    if label not in labels:
        labels[label] = 1
    elif label in labels:
        labels[label] += 1
    else:
        raise Exception("The file {} is okashii".format(file))

print("labels:", labels)

label2num = dict(zip(labels.keys(),[i for i in range(10)]))
print("labels with indices:", label2num)

import numpy as np

clf_files = [[] for i in range(10)]
for file in files:
    label = file.split('_')[0]
    clf_files[label2num[label]].append(file)

chosen_files = []
for ins_files in clf_files:
    choices = np.random.choice(ins_files,size=140,replace=False)
    chosen_files.append(choices)
chosen_files = np.array(chosen_files)

print("chosen files:", chosen_files.shape)

training_files = chosen_files[:,:120]
testing_files = chosen_files[:,120:]
print("training files:", training_files.shape)
print("testing files:", testing_files.shape)

training_files = np.reshape(training_files,(1200,))
testing_files = np.reshape(testing_files, (200,))
print("training files:", training_files.shape)
print("testing files:", testing_files.shape)

dataset_path = r"D:\nsynth1400"
training_path = dataset_path + '\\training'
testing_path = dataset_path + '\\testing'

if not os.path.isdir(training_path):
    os.mkdir(training_path)
if not os.path.isdir(testing_path):
    os.mkdir(testing_path)

import shutil
for traing_file in training_files:
    file_path = os.path.join(path, traing_file)
    shutil.copy(file_path, training_path)

for testing_file in testing_files:
    file_path = os.path.join(path, testing_file)
    shutil.copy(file_path, testing_path)









    
