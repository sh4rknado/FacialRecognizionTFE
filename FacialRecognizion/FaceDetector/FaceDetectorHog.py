import cv2
import dlib


class FaceDetectorHoG:
    def __init__(self):
        # DLIB HoG
        self._hogFaceDetector = dlib.get_frontal_face_detector()

    def detectFaceDlibHog(self, frame, inHeight=300, inWidth=0):

        frameDlibHog = frame.copy()
        frameHeight = frameDlibHog.shape[0]
        frameWidth = frameDlibHog.shape[1]
        if not inWidth:
            inWidth = int((frameWidth / frameHeight) * inHeight)

        scaleHeight = frameHeight / inHeight
        scaleWidth = frameWidth / inWidth

        frameDlibHogSmall = cv2.resize(frameDlibHog, (inWidth, inHeight))

        frameDlibHogSmall = cv2.cvtColor(frameDlibHogSmall, cv2.COLOR_BGR2RGB)
        faceRects = self._hogFaceDetector(frameDlibHogSmall, 0)
        print(frameWidth, frameHeight, inWidth, inHeight)
        bboxes = []
        cv2.putText(frameDlibHog, "OpenCV HoG", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, cv2.LINE_AA)
        for faceRect in faceRects:
            cvRect = [int(faceRect.left() * scaleWidth), int(faceRect.top() * scaleHeight),
                      int(faceRect.right() * scaleWidth), int(faceRect.bottom() * scaleHeight)]
            bboxes.append(cvRect)
            cv2.rectangle(frameDlibHog, (cvRect[0], cvRect[1]), (cvRect[2], cvRect[3]), (0, 255, 0),
                          int(round(frameHeight / 150)), 4)
        return frameDlibHog
