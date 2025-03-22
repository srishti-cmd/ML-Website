from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the trained model
model = load_model("handwriting_traits_model.h5")

# Define the classes (Make sure these match your model's output classes)
class_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

# Function to preprocess the uploaded image
def preprocess_image(img_path):
    img = Image.open(img_path)
    img = img.resize((128, 128))  # Resize image to match model input size
    img_array = np.array(img)  # Convert image to numpy array
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Route to home page
@app.route('/')
def index():
    return render_template('index1.html')

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400 
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected', 400
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(f"Attempting to save file at: {file_path}")

    try:
        file.save(file_path)
        print(f"File successfully saved at: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
        return 'Error saving file', 500
   
    try:
        # Open the uploaded image
        img = Image.open(file).convert('RGB')  # Ensure RGB format
        img = img.resize((128, 128))  # Resize to match model input
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict using the model
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        class_names = ['Agreeableness', 'Conscientiousness', 'Extraversion', 'Neuroticism', 'Openness']
        trait = class_names[predicted_class[0]]
        return render_template('index1.html', prediction=trait, image_file=f"images/{filename}")
    
    except Exception as e:
        print("Error during prediction:", e)
        return 'Error processing file', 500

if __name__ == '__main__':
    app.run(debug=True)
