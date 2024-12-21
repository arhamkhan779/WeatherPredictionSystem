# 🌤️ Weather Prediction System

## 📌 Overview
The **Weather Prediction System** is an end-to-end machine learning project designed to predict whether the weather will be sunny or rainy. This project incorporates modular programming, industrial CI/CD pipelines, and deployment strategies, making it scalable and production-ready.

---

## 🎯 Features
- **Weather Prediction**: Classifies weather as "Sunny" or "Rainy."
- **Interactive Web Interface**: Simple and intuitive HTML-based interface.
- **CI/CD Pipeline**: Ensures continuous integration and deployment.
- **Scalable Architecture**: Modular design for easy updates and enhancements.

---

## 🏗️ Project Structure
The project uses a well-organized directory structure:

```
WeatherPredictionSystem/
│
├── .github/workflows/.gitkeep
├── src/WeatherPredictionSystem/
│   ├── __init__.py
│   ├── components/__init__.py
│   ├── utils/__init__.py
│   ├── config/__init__.py
│   ├── config/configuration.py
│   ├── pipeline/__init__.py
│   ├── entity/__init__.py
│   ├── constants/__init__.py
│
├── config/config.yaml
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── setup.py
├── research/trials.ipynb
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── sunny.html
│   ├── rainy.html
```

---

## 🚀 Workflow
The project is divided into the following stages:

1. **Data Ingestion**
   - Downloads the dataset from Google Drive.
   - Saves the data locally for preprocessing.

2. **Data Preprocessing**
   - Applies `StandardScaler` for input data transformation.
   - Saves processors as `input_processor.pkl` and `target_processor.pkl`.

3. **Model Training**
   - Trains the machine learning model.
   - Saves:
     - Model results as a CSV file.
     - Confusion matrix as a PNG.
     - Final model as `model.pkl`.

All processes are executed by running `main.py`, ensuring seamless CI/CD integration.

---

## 🌐 Web Interface
The web interface consists of the following pages:

- **Home Page (`home.html`)**: Welcome page with a "Get Started" button.
- **Input Form (`index.html`)**: A form to input weather parameters for prediction.
- **Sunny Page (`sunny.html`)**: Displays when the prediction is "Sunny."
- **Rainy Page (`rainy.html`)**: Displays when the prediction is "Rainy."

---

## 📂 Dataset
The dataset used for this project is sourced from Kaggle:  
[Weather Prediction Dataset](https://www.kaggle.com/datasets/ananthr1/weather-predictionhttps://www.kaggle.com/datasets/ananthr1/weather-prediction)

---

## 📜 Key Files
- **`config/config.yaml`**: Configuration settings for the project.
- **`params.yaml`**: Parameters for preprocessing and training.
- **`main.py`**: Entry point to execute the entire pipeline.
- **`setup.py`**: Script to package the project as a Python library.

---

## 🛠️ Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<username>/WeatherPredictionSystem.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd WeatherPredictionSystem
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## 🌟 Highlights
- Implements **logging** and robust **exception handling**.
- Common utility functions for reusability in `common.py`.
- CI/CD pipeline ensures smooth development and deployment.

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👨‍💻 Author
**Arham Khan**  
*Data Scientist | Machine Learning Developer | Deep Learning Enthusiast*  

---

## 🙌 Acknowledgements
- **Dataset Provider**: Kaggle
- **Inspirations**: Community contributions and industrial best practices.

Feel free to fork, star ⭐, and contribute to this project!