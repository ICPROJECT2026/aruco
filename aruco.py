import cv2
import numpy as np

# 相机参数
camera_matrix = np.array([
    [1812.3, 0, 960],
    [0, 1810.7, 540],
    [0, 0, 1]
])

dist_coeffs = np.array([
    -0.12,
     0.08,
     0.0007,
    -0.0004,
     0.0
])

# Marker尺寸
marker_size = 0.08

aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_6X6_250
)

detector = cv2.aruco.ArucoDetector(
    aruco_dict
)

cap = cv2.VideoCapture(0)

z0 = None

while True:

    ret, frame = cap.read()

    corners, ids, reject = detector.detectMarkers(frame)

    if ids is not None:

        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners,
            marker_size,
            camera_matrix,
            dist_coeffs
        )

        z_current = tvecs[0][0][2]

        if z0 is None:
            z0 = z_current
            print("零点已记录")

        height = z_current - z0

        cv2.putText(
            frame,
            f"Height: {height*1000:.1f} mm",
            (40,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0,255,0),
            2
        )

        cv2.drawFrameAxes(
            frame,
            camera_matrix,
            dist_coeffs,
            rvecs[0],
            tvecs[0],
            0.05
        )

    cv2.imshow("Height Measure", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()