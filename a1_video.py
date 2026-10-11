import cv2

cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    print("error occured while opening video file")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (w, h))

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    count = count + 1
    cv2.rectangle(frame, (50, 80), (300, 250), (0, 250, 0), 3)
    cv2.putText(frame, "Frame " + str(count), (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    out.write(frame)

    small = cv2.resize(frame, (w // 2, h // 2))
    cv2.imshow("video", small)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("done, frames:", count)