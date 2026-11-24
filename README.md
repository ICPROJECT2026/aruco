# aruco
Step1 calibrate the camera: Get the position of camera in matrix.

camera_matrix

dist_coeffs


Step2 generate aruco: After printing, stick ChArUco Board onto the platform.

Assuming the aruco side length is 100mm, so marker_size = 0.1, unit: m.


Step3 real-time detection and measurement of height

Many people use "height = tvec[2]" directly, but installation errors often occur on industrial sites. This is due to the camera is not completely vertical. Here the code uploaded establish a world coordinate system.
