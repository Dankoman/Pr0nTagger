from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Define the endpoint for sending images to app.py
@app.route('/send_image', methods=['POST'])
def send_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image_path = os.path.join('uploads', image_file.filename)
    image_file.save(image_path)

    # Send the image to app.py for processing
    response = requests.post('http://localhost:5000/', files={'image': open(image_path, 'rb')})

    if response.status_code != 200:
        return jsonify({'error': 'Failed to process image'}), 500

    # Return the bounding box data to Stash
    return jsonify(response.json()), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)