from flask import Flask, request, jsonify
import cv2
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

def extract_dominant_colors(image_path, num_colors=5):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    return dominant_colors

def classify_color(color):
    r, g, b = color
    if 0 <= r <= 180 and 0 <= g <= 175 and 27 <= b <= 200:
        season_type = "Winter"
    elif 50 <= r <= 255 and 50 <= g <= 255 and 46 <= b <= 235:
        season_type = "Spring"
    elif 10 >= r >= 224 and 10 >= g >= 200 and 0 >= b >= 185:
        season_type = "Autumn"
    elif 0 <= r <= 255 and 0 <= g <= 237 and 0 <= b <= 255:
        season_type = "Summer"
    else:
        season_type = "Neutral"
    
    saturation = (np.max(color) - np.min(color)) / 255.0
    if saturation > 0.5:
        saturation_level = "Saturated"
    else:
        saturation_level = "Desaturated"
    
    if 180 <= r <= 225 and 0 <= g <= 175 and 50 <= b <= 150:
        temperature = "Warm"
    elif 50 <= r <= 184 and 60 <= g <= 250 and 100 <= b <= 120:
        temperature = "Cool"
    else:
        temperature = "Neutral"
    
    return season_type, saturation_level, temperature

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    dominant_colors = extract_dominant_colors(file_path)
    classifications = []
    for color in dominant_colors:
        season_type, saturation_level, temperature = classify_color(color)
        classifications.append({
            'color': color.tolist(),
            'season_type': season_type,
            'saturation_level': saturation_level,
            'temperature': temperature
        })

    return jsonify(classifications)

if __name__ == '__main__':
    app.run(debug=True)
