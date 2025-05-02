# 🖼️ OCR Text Extractor

This Python script automates the extraction of text from images using Tesseract OCR. It processes all images in the `test_images/` folder and saves the extracted text as `.txt` files in the `extracted_texts/` directory, maintaining the original image filenames.

---

## 📁 Project Structure

```

OCR-Text-Extractor/
├── OCR.py
├── test_images/
│   └── image1.jpg
│   └── image2.png
├── extracted_texts/
│   └── image1.txt
│   └── image2.txt
└── README.md
```



---

## ⚙️ Features

* Batch processes `.jpg`, `.jpeg`, and `.png` images.
* Supports multiple languages (default: English and Hindi).
* Automatically creates the `extracted_texts/` folder if it doesn't exist.
* Provides informative logging for each processed file.([GitHub][2])

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Mrigank005/OCR
cd OCR
```



### 2. Install Dependencies

Ensure you have Python 3 installed. Then, install the required Python libraries:

```bash
pip install pillow pytesseract
```



### 3. Install Tesseract OCR Engine

* **Windows**: Download and install from [Tesseract OCR Windows Installer](https://github.com/tesseract-ocr/tesseract/wiki).
* **macOS**: Use Homebrew:([GitHub][1])

  ```bash
  brew install tesseract
  ```



* **Linux (Debian/Ubuntu)**:

  ```bash
  sudo apt-get install tesseract-ocr
  ```



Ensure Tesseract is added to your system's PATH.

### 4. Add Images

Place the images you want to process into the `test_images/` directory.

### 5. Run the Script

```bash
python OCR.py
```



The extracted text files will be saved in the `extracted_texts/` directory.

---

## 📝 Customization

* **Language Support**: The script defaults to English and Hindi. To modify the languages, edit the `langs` parameter in the `extract_text_and_save` function within `OCR.py`:

  ```python
  def extract_text_and_save(image_path, langs=["eng", "hin"]):
  ```



Refer to [Tesseract OCR Language Data](https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#languages) for available language codes.([GitHub][1])

* **Tesseract Path**: If Tesseract isn't in your system's PATH, specify its location in `OCR.py`:

  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
  ```



---

## 🧪 Sample Output

For an image named `page1.jpg` in `test_images/`, the script will generate `page1.txt` in `extracted_texts/` containing the recognized text.

---

## 🙌 Acknowledgements

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [pytesseract](https://pypi.org/project/pytesseract/)
* [Pillow](https://pypi.org/project/Pillow/)

---
