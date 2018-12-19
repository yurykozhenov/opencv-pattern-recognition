import cv2


def lab15(video_path):
    scale_factor = 1.2
    min_neighbors = 5
    flags = 0
    min_size = (50, 50)

    cascade_file_path = "./haarcascade_frontalface_alt.xml"

    cascade = cv2.CascadeClassifier(cascade_file_path)
    video = cv2.VideoCapture(video_path)

    while True:
        ret, img = video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        rects = cascade.detectMultiScale(
            gray, scale_factor, min_neighbors, flags, min_size)

        if len(rects) >= 0:
            for (x, y, w, h) in rects:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('Face Detection on Video', img)

            key = cv2.waitKey(1)

            if key == 27:
                break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab15("assets/face_detection_video.mp4")
