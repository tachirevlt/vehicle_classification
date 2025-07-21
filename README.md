#  Vehicle Classification with CNN

This project implements a deep learning model using Convolutional Neural Networks (CNNs) to classify images of vehicles into four categories: **Car**, **Bus**, **Truck**, and **Motorcycle**.

---

##  Dataset

The dataset contains labeled images of four vehicle types:
- **Car**
- **Bus**
- **Truck**
- **Motorcycle**


---

##  Model Architecture

We use a custom **CNN architecture** built with PyTorch:

- 3 Convolutional layers with ReLU + MaxPooling
- Fully Connected layer with Dropout
- Softmax output for classification

---

##  Installation

1. Clone the repo:
```bash
git clone https://github.com/tachirevlt/vehicle_classification.git
```

## Evaluation

|             | precision |   recall | f1-score |
|-------------|-----------|----------|----------|
|        Bus  |   0.5556  |  0.2941  |  0.3846  |
|        Car  |   0.6000  |  0.4615  |  0.5217  |
| motorcycle  |   0.2500  |  0.8571  |  0.3871  |
|      Truck  |   0.9412  |  0.6957  |  0.8000  |

- The model performs well on the Truck class (F1-score: 0.8000), suggesting it learns the features of large vehicles effectively.

- Motorcycle has a high recall (0.8571) but low precision (0.2500), indicating the model often predicts motorcycle, even when incorrect.

- Bus and Car classes show moderate performance, suggesting room for improvement in capturing their distinguishing features.

---

## Future Improvements

1. Expand the Dataset
- Collect more images across different angles, lighting, occlusions, and backgrounds.

- Focus on underrepresented or confusing classes like Bus and Motorcycle.

2. Upgrade the Model
- Replace the simple CNN with modern architectures such as:
ResNet18, MobileNetV2, EfficientNet

- Apply Transfer Learning for better feature extraction and faster convergence.

3. Filter Out Noisy / Occluded Data
- Implement preprocessing techniques to detect and remove:

- Heavily blurred images

- Objects obscured by other elements (e.g., trees, poles, people)

4.  Focused Cropping
- Use semantic segmentation or object detection (YOLO, Mask R-CNN) to:

- Crop and center the main vehicle region

- This helps the model focus on shape and structure rather than surrounding context.

---

## Author

[![GitHub](https://img.shields.io/badge/GitHub-tachirevlt-blue?logo=github)](https://github.com/tachirevlt)
