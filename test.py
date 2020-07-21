import cv2
import numpy as np
import algo

frame = cv2.imread('assets/6.jpg')
frame = cv2.resize(frame, (640, 480))
frame_canny = algo.canny(frame)
cropped_canny = algo.region_of_interest(frame_canny)

lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
averaged_lines = algo.average_slope_intercept(cropped_canny, lines)
line_image = algo.display_lines(cropped_canny, averaged_lines)
combo_image = cv2.addWeighted(cropped_canny, 0.8, line_image, 1, 1)

cv2.imshow("result", frame)
cv2.imshow("canny", frame_canny)
cv2.imshow("cropped canny", combo_image)
cv2.waitKey(0)
