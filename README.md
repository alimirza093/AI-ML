# AI & ML Learning Repository

A personal learning repository focused on machine learning, deep learning, data preprocessing, NLP, and applied AI projects. This repository is organized as a structured practice space where I experiment with algorithms, build models, test ideas, and document what I learn while improving my skills.

## Overview

This project is designed for learning and practicing core concepts in artificial intelligence and machine learning. It includes:

- data preprocessing and exploratory workflows
- classical machine learning algorithms
- model evaluation and tuning techniques
- unsupervised learning methods
- natural language processing techniques
- deep learning with ANN, CNN, and RNN/LSTM models
- small end-to-end AI projects and demos

The repository is intentionally practical and educational rather than production-focused. It is meant to serve as a hands-on library of experiments, notebook-based learning, and portfolio-style work.

## Repository Structure

```text
AI-ML/
├── 01-data-preprocessing/
│   ├── 01-data-preprocessing.ipynb
│   └── 02-data-preprocessing.ipynb
├── 02-machine-learning/
│   ├── 01-regression/
│   ├── 02-classification/
│   ├── 03-model-selection/
│   ├── 04-hyperparameter-tuning/
│   ├── 05-ensemble-learning/
│   └── 06-unsupervised-learning/
├── 03-projects/
│   ├── adult-census-income-prediction/
│   ├── emotion-detection-model(NLP)/
│   ├── employee-attrition-prediction/
│   └── heart-disease-prediction/
├── 04-natural-language-processing/
│   ├── 01-text-preprocessing/
│   └── 02-feature-extraction/
├── 05-deep-learning/
│   ├── 01-artificial-neural-network(ANN)/
│   ├── 02-convolutional-neural-network(CNN)/
│   └── 03-recurrence-neural-network(RNN)/
├── data/
│   ├── adult.csv
│   ├── heart.csv
│   ├── insurance.csv
│   ├── Iris.csv
│   ├── Titanic-Dataset.csv
│   └── ...
├── requirements.txt
├── .gitignore
├── README.md
└── venv/
```

## Learning Areas

### 1. Data Preprocessing

This section focuses on:

- handling missing values
- encoding categorical variables
- feature scaling
- data cleaning and transformation
- preparing datasets for modeling

### 2. Machine Learning

Topics covered include:

- linear regression
- logistic regression
- decision trees
- k-nearest neighbors
- support vector machines
- random forests
- Naive Bayes
- cross-validation
- hyperparameter tuning with GridSearchCV and RandomizedSearchCV
- ensemble methods such as bagging, boosting, stacking, and XGBoost
- clustering and dimensionality reduction techniques

### 3. Natural Language Processing (NLP)

This part of the repository includes:

- text preprocessing
- tokenization
- stop-word removal
- feature extraction using BoW and TF-IDF
- NLP-driven project experiments

### 4. Deep Learning

This folder contains experiments with:

- artificial neural networks (ANN)
- convolutional neural networks (CNN)
- recurrent neural networks (RNN)
- LSTM-based sequence modeling

### 5. Real-World AI Projects

The projects section demonstrates practical application of ML and AI concepts on real-world datasets and prediction tasks such as:

- income prediction
- employee attrition prediction
- heart disease prediction
- emotion detection

## Tools and Technologies

This repo uses a modern Python-based ML stack, including:

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- scikit-learn
- TensorFlow / Keras
- Streamlit
- Jupyter Notebook / JupyterLab

## Environment Setup

### Prerequisites

- Python 3.10+
- pip or conda
- Jupyter Notebook support

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# or
venv\Scripts\activate      # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running Notebooks

Open notebooks with Jupyter:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

## Running Streamlit Apps

Some projects include interactive web apps. For example:

```bash
streamlit run 05-deep-learning/03-recurrence-neural-network\(RNN\)/02-lstm-implementation/app.py
```

## Project Philosophy

This repository reflects a hands-on learning approach:

- practice before perfection
- learn by implementing real algorithms
- explore multiple models and datasets
- track progress through notebooks and experiments
- build intuition through repetition and iteration

It is not a production-ready library or a polished product. Instead, it is a growing personal archive of learning and experimentation in AI and ML.

## Goals

The main goals of this repo are to:

- strengthen fundamentals in machine learning and deep learning
- practice with real datasets and public benchmarks
- experiment with different model architectures and evaluation techniques
- build confidence in Python-based AI development
- create a portfolio of learning projects and technical practice

## Notes

This repository is best used as a study and learning log. Each folder and notebook represents a milestone in the learning journey and can be revisited as knowledge grows.

## License

This repository is intended for educational and personal learning use.

## Future Direction

This repository will continue to grow with:

- more ML practice notebooks
- additional NLP and deep learning experiments
- more mini-projects and real-world use cases
- improved documentation and learning notes
- deployment demos and small AI apps

---

Built for continuous learning, experimentation, and skill-building in machine learning and deep learning.
