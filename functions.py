import numpy as np
import cv2
import matplotlib.pyplot as plt
import open3d as o3d
import os


def Hough_Circles(image, minDist, p1, p2):
    xVec = []
    yVec = []
    rVec = []
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, minDist, param1=p1, param2=p2)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            xVec.append(x)
            yVec.append(y)
            rVec.append(r)
    return xVec, yVec, rVec


def Holes_from_Image(image_path):
    try:
        image = cv2.imread(image_path)
        output_image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to Grayscale
        x, y, r = Hough_Circles(image, 30, 50, 30)
        if len(x) > 0:
            for i in range(len(x)):
                cv2.circle(output_image, (x[i], y[i]), r[i], (0, 255, 0), 1)
                cv2.rectangle(output_image, (x[i] - 3, y[i] - 3), (x[i] + 3, y[i] + 3), (0, 128, 255), -1)
            cv2.imwrite('output.jpg', output_image)
            return x,y
    except Exception as e:
        print('Something went wrong, pleas try again. ')
        print(e)


def Holes_from_3DModel(model_path):
    try:
        mesh = o3d.io.read_triangle_mesh(model_path)
        centroids = []
        radiuses = []
        vis = o3d.visualization.Visualizer()
        vis.create_window(visible=False)
        vis.add_geometry(mesh)
        vis.update_geometry(mesh)
        vis.poll_events()
        vis.update_renderer()
        image = vis.capture_depth_float_buffer(do_render=True)
        image_asarray = np.asarray(image)
        plt.imsave("tmp.png",
                   image_asarray, dpi=1)
        img = cv2.imread('tmp.png', 0)
        img = cv2.medianBlur(img,3)
        x, y, r = Hough_Circles(img, 20, 20 ,25)

        if len(x)>0:
            for i in range(len(x)):
                z = int(image_asarray[y[i],x[i]])
                centroids.append([y[i], x[i], z])
                radiuses.append(r[i])
        os.remove('tmp.png')
        return centroids, radiuses
    except Exception as e:
        print('Something went wrong, pleas try again. ')
        print(e)

