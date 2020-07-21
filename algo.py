import cv2
import numpy as np
import math
# get lines


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    kernel = 15  # it's important here to have a high value to prevent the light reflection of the road to cause any problem
    blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def make_points(image, line):
    slope, intercept = line
    y1 = int(image.shape[0])  # bottom of the image
    y2 = int(y1*3/5)         # slightly lower than the middle
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]


def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []

    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:  # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    average = [np.average(a, axis=0)
               for a in [left_fit, right_fit] if len(a) >= 1]
    points = [make_points(image, a) for a in average]
    return points


def display_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 20)
    return line_image


def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]
    mask = np.zeros_like(canny)

    polygon = np.array([[
        (0, height),
        (width, height),
        (width, height-200),
        (0, height-200),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

def get_average_slopes(lines):
    if lines is None:
        return None
    avg=0
    for line in lines:
        for x1, y1, x2, y2 in line:
            a = math.atan((y2-y1)/(x2-x1))/(2*math.pi*len(lines))
            avg += a - (a/abs(a))*0.15
    return avg