# Stash Plugin for Image Processing

This Stash app plugin allows users to send paused frame images to a specified Flask application (`app.py`) and receive bounding box information in return. The plugin is designed to facilitate image processing tasks, particularly in the context of face detection and recognition.

## Project Structure

```
stash-plugin
├── src
│   ├── main.py          # Entry point of the plugin
│   ├── api
│   │   └── client.py    # API client for communication with app.py
│   └── utils
│       └── __init__.py  # Utility functions and classes
├── requirements.txt      # Project dependencies
├── README.md             # Documentation for the plugin
└── config.json           # Configuration settings for the plugin
```

## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Install Dependencies**
   Navigate to the project directory and install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

3. **Configuration**
   Update the `config.json` file with the necessary API endpoints and settings required for the plugin's operation.

4. **Run the Plugin**
   Start the plugin by executing the `main.py` file:
   ```
   python src/main.py
   ```

## Usage

- The plugin listens for paused frame images and sends them to the Flask application for processing.
- Upon receiving the bounding box data, the plugin can display or utilize this information as needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.