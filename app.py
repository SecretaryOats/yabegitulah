from flask import Flask, request, jsonify
import cv2
import numpy as np
from sklearn.cluster import KMeans

# ... your color analysis functions from the original code

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_image():
  # Get uploaded image file
  image_file = request.files.get('image')
  if not image_file:
    return jsonify({'error': 'No image uploaded'}), 400

  # Process the image and get color analysis results
  # (implement your logic using cv2, numpy, etc.)
  results = color_analysis(image_file.read())

  # Return the analysis results as JSON
  return jsonify(results)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  # Run the Flask app
