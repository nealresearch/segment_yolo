import os
import random
import shutil

"""
code to randomly shuffle the image and the label and move it to the folder.
* Note to self: Refactor it into class object. 
"""
#function to move the files
def move_file(src_dir, dst_dir, file_name):
    try:
        src = os.path.join(src_dir, file_name)
        dst = os.path.join(dst_dir, file_name)
        if os.path.exists(src):
            shutil.move(src, dst)
    except FileNotFoundError as err:
        print(f"File is not found: {src}")
        
train = "M:\\yolo_images\\yolo_segment_r\\train\\images\\"
train_label = "M:\\yolo_images\\yolo_segment_r\\train\\labels\\"

valid = "M:\\yolo_images\\yolo_segment_r\\valid\\images\\"
valid_label = "M:\\yolo_images\\yolo_segment_r\\valid\\labels\\"


image = "M:\\yolo_images\\yolo_segment_r\\collect_image\\"
label = "M:\\yolo_images\\yolo_segment_r\\collect_label\\"


length_of_file = len([file for file in os.listdir("M:\\yolo_images\\yolo_segment_r\\collect_image\\")])
number_for_file = [x for x in range(1, length_of_file)]


random.shuffle(number_for_file)

train_percent = int((80 / 100) * (length_of_file + 22))
valid_percent = int((20 / 100) * (length_of_file + 22)) 

 
train_list = number_for_file[:train_percent]
valid_list = number_for_file[train_percent:train_percent + valid_percent]


for i in train_list:
    check_path_image = os.path.join(image, "lidar{}.tif".format(i))
    check_path_label = os.path.join(label, "lidar{}.txt".format(i))
    if os.path.exists(check_path_image) and os.path.exists(check_path_label):
        move_file(image, train, "lidar{}.tif".format(i))
        move_file(label, train_label, "lidar{}.txt".format(i))
    else:
        print("File not found", i)
        
    
for i in valid_list:
    check_path_val = os.path.join(image, "lidar{}.tif".format(i))
    check_path_label_val = os.path.join(label, "lidar{}.txt".format(i))
    if os.path.exists(check_path_val) and os.path.exists(check_path_label_val):
        move_file(image, valid, "lidar{}.tif".format(i))
        move_file(label, valid_label, "lidar{}.txt".format(i))
    else:
        print("file not found", i)
