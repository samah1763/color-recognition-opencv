import cv2
import numpy as np

image = cv2.imread("colors.jpg")

if image is None:
    print("الصورة غير موجودة")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

colors = {
    "Red": [
        (np.array([0, 100, 100]), np.array([10, 255, 255])),
        (np.array([170, 100, 100]), np.array([180, 255, 255]))
    ],
    "Green": [
        (np.array([35, 70, 70]), np.array([85, 255, 255]))
    ],
    "Blue": [
        (np.array([90, 80, 70]), np.array([130, 255, 255]))
    ]
}

for color_name, ranges in colors.items():
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

    for lower, upper in ranges:
        mask = mask | cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (255, 255, 255),
                3
            )

            cv2.putText(
                image,
                color_name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

cv2.imshow("Color Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()