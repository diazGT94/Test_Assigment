import argparse
import numpy as np
import cv2
from functions import *


def parse_args():
    desc = 'Application that can extract hole information from and image and from .stl model'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-Image_function', '--Image_function', dest='Image_function', action='store_true',
                        help='Specify this flag for using the image function')
    parser.add_argument('-Model_function', '--Model_function', dest='Model_function', action='store_true',
                        help='Specify this flag for using the image function')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    x=[]
    y=[]
    centroids=[]
    radiuses=[]
    if args.Image_function:
        # Call the function from Holes
        image_path = './files/model_top_view.png'
        x,y = Holes_from_Image(image_path)

    if args.Model_function:
        # Call the function from STL
        model_path = './files/model.stl'
        centroids, radiuses = Holes_from_3DModel(model_path)
        for i in range(len(radiuses)):
            print('Hole#: ' + str(i + 1) + ' Centroid: ' + str(centroids[i]) + ' Radius: ' + str(radiuses[i]))

    if args.Image_function and args.Model_function and len(centroids)>0 and len(x)>0:
        cM =[[790,0,395],[0,622,311],[0,0,1]]
        cM = np.array(cM)
        iP = np.column_stack((x, y))
        iP = np.array(iP).astype('float32')
        oP=np.array(centroids).astype('float64')

        ret,rvecs,tvecs = cv2.solvePnP(oP,iP,cM,distCoeffs=None,flags=cv2.SOLVEPNP_SQPNP)
        print('\n' + 'Rotation Vector: \n'+ str(rvecs) + '\n'+ 'Translation Vector: \n' + str(tvecs))




if __name__ == '__main__':
    main()
