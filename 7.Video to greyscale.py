import cv2

video = cv2.VideoCapture("sample.mp4")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Fast Motion Video", frame)

    # Delay of 10 ms for fast motion
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
