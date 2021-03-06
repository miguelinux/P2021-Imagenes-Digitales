import numpy as np
import cv2 as cv


camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    gray = cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
    corners= cv.goodFeaturesToTrack(gray,25,0.01,10)
    color = cv.cvtColor(gray,cv.COLOR_GRAY2RGB)

    if corners is not None:
        corners = np.int0(corners)

        for i in corners:
            x,y = i.ravel()
            cv.circle(color,(x,y),3,(0,0,255),-1)

    cv.imshow("Camara", color)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()