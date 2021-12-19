"""
import in python is similar to #include header_file in C/C++. 
Python modules (module is a file containing Python definitions 
and statements) can get access to code from another module by 
importing the file/function using import.
"""
import cv2
import cvlib as cv
"""
OpenCV-Python is a library of Python bindings designed to solve 
computer vision problems.
"""
"""
To count the images one has to make use of computer vision libraries.
Use of the cvlib library which is very simple, easy, and a high-level 
library in Python.
cvlib is a simple, high level, easy-to-use open source Computer Vision 
library for Python. It was developed with a focus on enabling easy and 
fast experimentation. 
Below are the python packages are installed, cvlib is completely pip 
installable.
=>OpenCV
=>Tensorflow
pip install opencv-python tensorflow
pip install cvlib
"""
"""
Object detection
Detecting common objects in the scene is enabled through a 
single function call detect_common_objects(). 
It will return the bounding box co-ordinates, corrensponding 
labels and confidence scores for the detected objects in the image.
"""

def find_density():
    image1 = cv2.imread('lane1.jpg') 
    """
    cv2.imread() method loads an image from the specified file. If 
    the image cannot be read (because of missing file, improper 
    permissions, unsupported or invalid format) then this method 
    returns an empty matrix.
    To read an image using OpenCV
    Now the variable image1 will be a matrix of pixel values. 
    We can print it and see the RGB values.
    """
    #print(image1)

    out = 'image not found'
    assert not isinstance(image1, type(None)), out
    """
    The isinstance() function returns True if the specified object 
    is of the specified type, otherwise False. If the type parameter 
    is a tuple, this function will return True if the object is one 
    of the types in the tuple.
    Syntax => isinstance(object, type)
    The None keyword is used to define a null value, or no value at 
    all. None is not the same as 0, False, or an empty string.
    Asertion - I have written a code that should not execute at all 
    costs because according to you logic it should not happen
    def get_age(age):
    print "Your Age is: ", age
    get_age(18)
    get_age(-1)
    """
    dict_lane = {'lane-1': 0, 'lane-2': 0, 'lane-3': 0, 'lane-4': 0}

    bbox, label, conf = cv.detect_common_objects(image1)
    total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
    # print('Number of vehicles in cam-1 in the image is ', total)

    dict_lane['lane-1'] = total

    image2 = cv2.imread('lane2.jpg')
    
    assert not isinstance(image2, type(None)), out

    bbox, label, conf = cv.detect_common_objects(image2)
    total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
    # print('Number of vehicles in cam-2 in the image is ', total)

    dict_lane['lane-2'] = total

    image3 = cv2.imread('lane3.jpg')
    assert not isinstance(image3, type(None)), out

    bbox, label, conf = cv.detect_common_objects(image3)
    total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
    # print('Number of vehicles in cam-3 in the image is ', total)

    dict_lane['lane-3'] = total

    image4 = cv2.imread('lane4.jpg')
    assert not isinstance(image4, type(None)), out

    bbox, label, conf = cv.detect_common_objects(image4)
    total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
    # print('Number of vehicles in cam-4 in the image is ', total)

    dict_lane['lane-4'] = total
    print(dict_lane)

    sorted_density = sorted(dict_lane.items(), key=lambda x: x[1], reverse=True)
    return sorted_density


def check_density():
    sorted_density = find_density()
    maxx = 10
    for i in sorted_density:
        lane = i[0]
        if i[1] == 0:
            traffic_light(lane, 11)
        elif i[1] > maxx:
            traffic_light(lane, 36)
        else:
            traffic_light(lane, 26)


def traffic_light(lane, time):
    print("Traffic => Light Status")
    if lane == 'lane-1':
        print(f"""
            Lane-1
                /````````````````````/
                Yellow for 3 sec.
                Green for {time} sec.
                Yellow for 3 sec.
                Back to RED.
                /````````````````````/

            Lane-2
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-3
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-4
                /````````````````````/
                Remains RED.
                /````````````````````/
              """)

    elif lane == 'lane-2':
        print(f"""
            Lane-1
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-2
                /````````````````````/
                Yellow for 3 sec.
                Green for {time} sec.
                Yellow for 3 sec.
                Back to RED.
                /````````````````````/

            Lane-3
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-4
                /````````````````````/
                Remains RED.
                /````````````````````/
              """)

    elif lane == 'lane-3':
        print(f"""
            Lane-1
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-2
                /````````````````````/
                Remains RED.
                /````````````````````/

            Lane-3
                /````````````````````/
                Yellow for 3 sec.
                Green for {time} sec.
                Yellow for 3 sec.
                Back to RED.
                /````````````````````/

            Lane-4
                /````````````````````/
                Remains RED.
                /````````````````````/
                """)
    else:
        print(f"""
            Lane-1
                /````````````````````/
                Remains RED.
                /````````````````````/
            Lane-2
                /````````````````````/
                Remains RED.
                /````````````````````/
            Lane-3
                /````````````````````/
                Remains RED.
                /````````````````````/
            Lane-4
                /````````````````````/
                Yellow for 3 sec.
                Green for {time} sec.
                Yellow for 3 sec.
                Back to RED.
                /````````````````````/
                """)

check_density()