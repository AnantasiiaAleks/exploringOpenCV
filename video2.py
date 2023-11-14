import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #0 - использование вебкамеры, или ссылка на файл

while True:
    #success, frame = cap.read() #success - булева переменная, удалось ли получить кадр
    _, frame = cap.read() # frame - получили кадр, а сакцесс необязателен
    cv2.imshow('camera', frame)

    if cv2.waitKey(1) & 0xff == ord('q'): # обновление кадра через 1 мс + выход из цикла принажатии на q
        break