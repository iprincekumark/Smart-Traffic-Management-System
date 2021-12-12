import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def findDensity():
    image1 = cv2.imread('lane1.png')
    assert not isinstance(image1, type(None)), 'image not found'
    dict_lane = {'lane-1' :0, 'lane-2' :0, 'lane-3' :0, 'lane-4' :0}

    bbox, label, conf = cv.detect_common_objects(image1)
    outputImage1 = draw_bbox(image1, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-1 in the image is ', total)

    dict_lane['lane-1'] = total

    image2 = cv2.imread('lane2.png')
    assert not isinstance(image2, type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(image2)
    outputImage2 = draw_bbox(image2, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-2 in the image is ', total)

    dict_lane['lane-2'] = total

    image3 = cv2.imread('lane3.png')
    assert not isinstance(image3, type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(image3)
    outputImage3 = draw_bbox(image3, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-3 in the image is ', total)

    dict_lane['lane-3'] = total

    image4 = cv2.imread('lane4.png')
    assert not isinstance(image4, type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(image4)
    outputImage4 = draw_bbox(image4, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-4 in the image is ', total)

    dict_lane['lane-4'] = total
    print(dict_lane)

    sorted_density = sorted(dict_lane.items(), key = lambda x: x[1], reverse = True)
    return sorted_density

def checkDensity():
    sorted_density = findDensity()
    max = 10
    for i in sorted_density:
        lane = i[0]
        if i[1] == 0:
            trafficLight(lane, 11)
        elif i[1]>max:
            trafficLight(lane, 36)
        else:
            trafficLight(lane, 26)

def trafficLight(lane, time):
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

checkDensity()