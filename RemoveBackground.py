import cv2
import numpy as np
from PIL import Image

def remove_background(pil_image):
    image = np.array(pil_image)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    white_bg = np.full(image_bgr.shape, 255, dtype=np.uint8)
    fg = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)
    bg = cv2.bitwise_and(white_bg, white_bg, mask=cv2.bitwise_not(mask))
    result = cv2.add(fg, bg)
    return Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

class RemoveBackground:
    def __call__(self, image):
        return remove_background(image)
