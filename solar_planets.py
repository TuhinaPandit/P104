import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (120,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (220,310), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (320,110), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (420,100), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (520,110), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (800,310), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (950,110), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1100,310), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,255))

cv2.imshow("output", img)
cv2.waitKey(0)