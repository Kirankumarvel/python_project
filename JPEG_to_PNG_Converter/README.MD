# CONVERT_JPEG_to_PNG

This project contains a simple Python script to change file extensions from `.jpeg` to `.png`.

## Requirements

To run this project, you need the following Python module:

- **Pillow**

You can install it using pip:
```bash
pip install pillow
```

## Methods

I accomplished this task in two ways:

### 1. Using Terminal

1. Add the image in JPEG format with the name `input` in this folder.
2. Run the `converter_terminal.py` script:
    ```bash
    python3 converter_terminal.py
    ```
3. The output image will be generated in this folder.

### 2. Using GUI

1. Run the `converter_GUI.py` script:
    ```bash
    python3 converter_GUI.py
    ```
2. Pick any JPEG image from any location.
3. Press the 'Convert Jpeg to Png' button.

## Additional Notes

- Ensure that your input image is in JPEG format and named correctly when using the terminal method.
- The GUI method provides a user-friendly interface for selecting images from anywhere on your system.
