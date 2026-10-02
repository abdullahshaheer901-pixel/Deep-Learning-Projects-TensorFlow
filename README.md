# 🧠 Deep Learning Projects — TensorFlow & Keras

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15%2B-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-2.15%2B-red?style=for-the-badge&logo=keras&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A curated collection of **Deep Learning** implementations using **TensorFlow & Keras**, covering the four fundamental neural network architectures:

**ANN → CNN → RNN → LSTM**

Each project is self-contained with its own dataset, model architecture, training script, and documentation.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Projects Overview](#-projects-overview)
- [Model Comparison](#-model-comparison)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Learning Path](#-learning-path)
- [Results Summary](#-results-summary)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Connect With Me](#-connect-with-me)
- [Acknowledgements](#-acknowledgements)

---

## 🧠 About the Project

This repository is a **hands-on deep learning portfolio** demonstrating the progression from basic neural networks to advanced sequence models. Every project includes:

- ✅ A complete **training script** (`.py`)
- ✅ A **dataset** (or auto-download)
- ✅ A **dedicated README** explaining the model
- ✅ **Expected results** and evaluation metrics

The goal is to help learners and recruiters see a clear journey through the four pillars of neural networks.

---

## 🎯 Projects Overview

| # | Project | Type | Dataset | Task |
|---|---------|------|---------|------|
| 1 | **ANN — Wine Classification** | Artificial Neural Network | Wine (sklearn) | Multi-class Classification |
| 2 | **CNN — MNIST Digit Recognition** | Convolutional Neural Network | MNIST | Image Classification |
| 3 | **RNN — Sequence Classification** | Recurrent Neural Network | Synthetic Sequence | Binary Classification |
| 4 | **LSTM — Sequence Classification** | Long Short-Term Memory | Synthetic Sequence | Binary Classification |

---

## 📊 Model Comparison

| Model | Data Type | Best For | Key Feature |
|-------|-----------|----------|-------------|
| **ANN** | Tabular | Structured data | Fully connected layers |
| **CNN** | Images | Spatial patterns | Convolution + Pooling |
| **RNN** | Sequences | Short-term dependencies | Recurrent loops |
| **LSTM** | Sequences | Long-term dependencies | Memory gates |

---

## ✨ Features

- ✅ **4 complete deep learning projects** in a single repo
- ✅ **Clean, modular Python code** with comments
- ✅ **TensorFlow 2.x + Keras** implementations
- ✅ **Real datasets** (Wine, MNIST) + synthetic sequences
- ✅ **Detailed documentation** for each project
- ✅ **Easy to run** — just `pip install` and go
- ✅ **Cross-platform** — Windows, Linux, macOS
- ✅ **Beginner-friendly** progression path

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core language |
| **TensorFlow 2.15+** | Deep learning framework |
| **Keras** | High-level neural network API |
| **NumPy** | Numerical computations |
| **Pandas** | Data manipulation |
| **Scikit-learn** | Datasets & preprocessing |
| **Matplotlib** | Visualization |

---

## 📁 Project Structure
Deep-Learning-Projects-TensorFlow/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── 01-ANN-Wine-Classification/
│ ├── ann_implementation.py
│ └── README.md
│
├── 02-CNN-MNIST-Digit-Recognition/
│ ├── cnn_model.py
│ └── README.md
│
├── 03-RNN-Sequence-Classification/
│ ├── rnn_model.py
│ └── README.md
│
└── 04-LSTM-Sequence-Classification/
├── lstm_model.py
└── README.md

text

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-compatible GPU for faster training

### Step 1: Clone the Repository

```bash
git clone https://github.com/abdullahshaheer901-pixel/Deep-Learning-Projects-TensorFlow.git
cd Deep-Learning-Projects-TensorFlow
Step 2: Create Virtual Environment (Recommended)
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
▶️ Usage
Each project is independent — navigate to its folder and run:

1️⃣ ANN — Wine Classification
bash
cd 01-ANN-Wine-Classification
python ann_implementation.py
2️⃣ CNN — MNIST Digit Recognition
bash
cd 02-CNN-MNIST-Digit-Recognition
python cnn_model.py
3️⃣ RNN — Sequence Classification
bash
cd 03-RNN-Sequence-Classification
python rnn_model.py
4️⃣ LSTM — Sequence Classification
bash
cd 04-LSTM-Sequence-Classification
python lstm_model.py
📚 Learning Path
This repository follows a natural progression:

text
1. ANN  →  Learn fundamentals of neural networks
              ↓
2. CNN  →  Add convolution for image processing
              ↓
3. RNN  →  Add recurrence for sequential data
              ↓
4. LSTM →  Add memory gates for long-term patterns
Recommendation: Study them in order — from 01 to 04.

📊 Results Summary
Model	Epochs	Test Accuracy
ANN (Wine)	100	~95%
CNN (MNIST)	3	~98%
RNN (Sequence)	30	~85%
LSTM (Sequence)	20	~90%
Actual values may vary slightly per run. Update with your real results.

🗺 Roadmap
☑ ANN — Wine Classification
☑ CNN — MNIST Digit Recognition
☑ RNN — Sequence Classification
☑ LSTM — Sequence Classification
□ Add Transformer model
□ Add GRU (Gated Recurrent Unit)
□ Add Autoencoders
□ Web interface (Streamlit)
□ Model deployment examples
🤝 Contributing
Contributions, issues, and feature requests are welcome!

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👤 Author
Abdullah Shaheer

🎓 Data Analytics Student | Deep Learning & Computer Vision Enthusiast

🐙 GitHub: @abdullahshaheer901-pixel

💼 LinkedIn: Abdullah Shaheer

📊 Kaggle: @abdullahshaheer260

📧 Email: abdullahshaheer901@gmail.com

🌐 Connect With Me
<p align="left"> <a href="https://www.linkedin.com/in/abdullah-shaheer260" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/> </a> <a href="https://kaggle.com/abdullahshaheer260" target="_blank"> <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle"/> </a> <a href="https://github.com/abdullahshaheer901-pixel" target="_blank"> <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/> </a> <a href="mailto:abdullahshaheer901@gmail.com" target="_blank"> <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/> </a> </p>
🙏 Acknowledgements
TensorFlow — Deep learning framework

Keras — High-level neural network API

Scikit-learn — Datasets & preprocessing

Digi Skills Program — Learning platform

⭐ Show Your Support
If this repository helped you, please give it a ⭐ star!

<p align="center"> Made with ❤️ by <a href="https://github.com/abdullahshaheer901-pixel">Abdullah Shaheer</a> </p> ```
