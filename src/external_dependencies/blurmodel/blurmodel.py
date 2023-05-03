from .blurmodelabc import BlurModelABC
import cv2
import numpy as np
import base64

from loguru import logger


class BlurModel(BlurModelABC):


    def __init__(self
                 ,cascade_file_path: str):
        self.face_casecade = cv2.CascadeClassifier(cascade_file_path)

    def blur_frame(self, frame) -> bytes:
        img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_casecade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            img[y:y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], 35)
        return cv2.imencode('.jpg', img)[1].tobytes()


    def blur(self, img_content: bytes) -> bytes:
        nparr = np.frombuffer(img_content, np.uint8)
        logger.debug(nparr.shape)
        return self.blur_frame(nparr)
    


    def _image_to_base64(self, img: np.ndarray) -> bytes:
        # using opencv 2, there are others ways
        img_buffer = cv2.imencode('.jpg', img)[1]
        return base64.b64encode(img_buffer).decode('utf-8')
    
    def get_image(self, volume, index: int):
        image = volume[:, :, index]
        return self._image_to_base64(image)

