import os
orig_input_dataset = "TrainTest"

# initialize the base path to the new directory that will contain
# our images after computing the training and testing split
base_path = "TrainTest"

# derive the training, validation, and testing directories
train_path = os.path.sep.join([base_path, "training"])
val_path = os.path.sep.join([base_path, "validation"])

# define the amount of data that will be used for training
train_split = 0.8
 
# the amount of validation data will be a percentage of the
# training data
val_split = 0.2