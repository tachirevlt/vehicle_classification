from PIL import Image, ImageEnhance, ImageFilter
import numpy as np  # Nếu cần cho các thao tác ma trận/ảnh nâng cao
import cv2



def sharpen_image(img):
    img_cv = np.array(img)  # PIL → ndarray
    if img_cv.ndim == 2:
        img_cv = np.expand_dims(img_cv, axis=2)
    kernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ])
    # Áp dụng kernel từng kênh
    if img_cv.shape[2] == 3:
        channels = [cv2.filter2D(img_cv[:, :, i], -1, kernel) for i in range(3)]
        sharpened = cv2.merge(channels)
    else:
        sharpened = cv2.filter2D(img_cv, -1, kernel)
    return Image.fromarray(np.clip(sharpened, 0, 255).astype(np.uint8))


class HistogramEnhanceAndSharpen:
    def __init__(self, 
                 dark_pixel_ratio_thresh=0.6, 
                 brightness_factor=1.2, 
                 contrast_factor=1.2,
                 apply_sharpen=True):
        self.dark_pixel_ratio_thresh = dark_pixel_ratio_thresh
        self.brightness_factor = brightness_factor
        self.contrast_factor = contrast_factor
        self.apply_sharpen = apply_sharpen

    def is_dark(self, img):
        gray = img.convert('L')
        hist = gray.histogram()
        total = sum(hist)
        dark_pixels = sum(hist[:50])
        return (dark_pixels / total) > self.dark_pixel_ratio_thresh

    def sharpen(self, img):
        return sharpen_image(img)  # dùng hàm sharpen đã định nghĩa phía trên

    def __call__(self, img):
        if self.is_dark(img):
            img = ImageEnhance.Brightness(img).enhance(self.brightness_factor)
            img = ImageEnhance.Contrast(img).enhance(self.contrast_factor)
        if self.apply_sharpen:
            img = self.sharpen(img)
        return img
