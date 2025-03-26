# Human Traits Recognition Using Handwriting Samples using Machine Learning

## Overview
This project aims to predict human personality traits based on handwriting samples using machine learning techniques. By analyzing various features of handwriting, such as letter shapes, spacing, and slant, the system can determine key personality traits like openness, conscientiousness, extraversion, agreeableness, and neuroticism.

## Features
- Upload handwriting samples as images.
- Extract handwriting features using image processing techniques.
- Train a machine learning model to predict personality traits.
- Display predicted personality traits with descriptions.
- Interactive and user-friendly UI.

## Technologies Used
- Python
- OpenCV (for image processing)
- Scikit-learn (for machine learning models)
- TensorFlow/Keras (for deep learning models, if applicable)
- Flask/Django (for backend API)
- HTML, CSS, JavaScript (for frontend UI)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/human-traits-recognition.git
   ```
2. Navigate to the project directory:
   ```bash
   cd human-traits-recognition
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open the browser and go to `http://127.0.0.1:5000/` to use the application.

## How It Works
1. The user uploads an image containing handwriting.
2. The system processes the image to extract handwriting features.
3. The extracted features are fed into a trained machine learning model.
4. The model predicts the dominant personality trait based on handwriting characteristics.
5. The results are displayed with an explanation.

## Sample Output
![Sample Output](https://github.com/srishti-cmd/ML-Website/blob/master/output.png)

## Future Enhancements
- Improve accuracy with advanced deep learning models.
- Support additional personality trait models.
- Provide detailed analysis of multiple traits per handwriting sample.

## Contributors
- Srishti Agarwal
- Stuti Jain
- Subhanshi Agarwal

