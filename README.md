# Synthetic Image Generator

This project creates synthetic images with overlaid text in various fonts and styles, using different backgrounds with bounding boxes that can be labeled.

## Features

- Generates synthetic images with varied text overlaid on diverse backgrounds.
- Customization of the number of images to generate.
- Option to split generated images into training and validation sets.

## Requirements

- Python 3.10.6
- Libraries:
    - Pillow (PIL)
    - scikit-learn (for splitting training and validation sets)

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nepomucenoc/synthetic-images-generator
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the image generator:**

    ```bash
    python execute_generator.py
    ```

4. **Customize parameters in the `execute_generator.py` file** as needed, such as font and background directories, desired number of images, etc.

## Project Structure

- `execute_generator.py`: Main file to run the image generator.
- `synthetic_image_generator.py`: Class responsible for generating synthetic images.
- `fonts/`: Directory containing different fonts for use in the images.
- `backgrounds/`: Directory containing various backgrounds for the generated images.
- `sintetico/`: Directory where the synthetic images are saved.

## Contribution

Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and problems.

## Authors

- [Author Name](https://github.com/nepomucenoc)

## License

This project is licensed. If you want to use, contact me at my email: carolina.nep@gmail.com
