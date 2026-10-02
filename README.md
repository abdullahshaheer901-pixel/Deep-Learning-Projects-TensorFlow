# Deep Learning Projects with TensorFlow & Keras

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15%2B-orange?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-2.15%2B-red?style=flat-square&logo=keras&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

A hands-on collection of deep learning implementations built with **TensorFlow** and **Keras**, covering four fundamental neural network architectures:

**ANN → CNN → RNN → LSTM**

Each project lives in its own folder with a training script and a dedicated README describing the model, data, and evaluation.

---

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Model Comparison](#model-comparison)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Learning Path](#learning-path)
- [Results](#results)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

---

## Overview

This repository documents a progression from basic feed-forward networks to sequence models. Every project includes:

- A complete, commented **training script** (`.py`)
- Data that is **loaded automatically** (scikit-learn / Keras datasets) or generated synthetically
- A **project README** explaining the architecture and approach
- **Evaluation metrics** on a held-out test set

It is intended both as a learning resource and as a portfolio of core deep learning concepts.

---

## Projects

| # | Project | Architecture | Dataset | Task |
|---|---------|--------------|---------|------|
| 1 | [ANN: Wine Classification](01-ANN-Wine-Classification) | Artificial Neural Network | Wine (scikit-learn) | Multi-class classification |
| 2 | [CNN: MNIST Digit Recognition](02-CNN-MNIST-Digit-Recognition) | Convolutional Neural Network | MNIST | Image classification |
| 3 | [RNN: Sequence Classification](03-RNN-Sequence-Classification) | Recurrent Neural Network | Synthetic sequences | Binary classification |
| 4 | [LSTM: Sequence Classification](04-LSTM-Sequence-Classification) | Long Short-Term Memory | Synthetic sequences | Binary classification |

---

## Model Comparison

| Model | Data Type | Best For | Key Idea |
|-------|-----------|----------|----------|
| **ANN** | Tabular | Structured data | Fully connected layers |
| **CNN** | Images | Spatial patterns | Convolution and pooling |
| **RNN** | Sequences | Short-term dependencies | Recurrent connections |
| **LSTM** | Sequences | Long-term dependencies | Gated memory cells |

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core language |
| TensorFlow 2.15+ | Deep learning framework |
| Keras | High-level neural network API |
| NumPy | Numerical computation |
| Pandas | Data manipulation |
| scikit-learn | Datasets and preprocessing |
| Matplotlib | Visualization |

---

## Project Structure

```text
Deep-Learning-Projects-TensorFlow/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── 01-ANN-Wine-Classification/
│   ├── ann_implementation.py
│   └── README.md
│
├── 02-CNN-MNIST-Digit-Recognition/
│   ├── cnn_model.py
│   └── README.md
│
├── 03-RNN-Sequence-Classification/
│   ├── rnn_model.py
│   └── README.md
│
└── 04-LSTM-Sequence-Classification/
    ├── lstm_model.py
    └── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip`
- *(Optional)* A CUDA-compatible GPU for faster training

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/abdullahshaheer901-pixel/Deep-Learning-Projects-TensorFlow.git
cd Deep-Learning-Projects-TensorFlow
```

**2. Create a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

Each project is independent. Navigate to its folder and run the script:

```bash
# 1. ANN: Wine Classification
cd 01-ANN-Wine-Classification
python ann_implementation.py

# 2. CNN: MNIST Digit Recognition
cd 02-CNN-MNIST-Digit-Recognition
python cnn_model.py

# 3. RNN: Sequence Classification
cd 03-RNN-Sequence-Classification
python rnn_model.py

# 4. LSTM: Sequence Classification
cd 04-LSTM-Sequence-Classification
python lstm_model.py
```

*(Run `cd ..` between projects to return to the repository root.)*

---

## Learning Path

The projects are designed to be studied in order:

```text
1. ANN   Fundamentals of neural networks
   ↓
2. CNN   Convolution for image data
   ↓
3. RNN   Recurrence for sequential data
   ↓
4. LSTM  Gated memory for long-term patterns
```

---

## Results

| Model | Epochs | Approx. Test Accuracy |
|-------|--------|-----------------------|
| ANN (Wine) | 100 | ~95% |
| CNN (MNIST) | 3 | ~98% |
| RNN (Sequence) | 30 | ~85% |
| LSTM (Sequence) | 20 | ~90% |

> Results vary slightly between runs due to random initialization.

---

## Roadmap

- [x] ANN: Wine Classification
- [x] CNN: MNIST Digit Recognition
- [x] RNN: Sequence Classification
- [x] LSTM: Sequence Classification
- [ ] GRU (Gated Recurrent Unit)
- [ ] Autoencoders
- [ ] Transformer model
- [ ] Streamlit web interface
- [ ] Model deployment examples

---

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Abdullah Shaheer**
Data Analytics Student | Deep Learning & Computer Vision Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullah-shaheer260)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/abdullahshaheer260)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/abdullahshaheer901-pixel)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:abdullahshaheer901@gmail.com)

---

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/): deep learning framework
- [Keras](https://keras.io/): high-level neural network API
- [scikit-learn](https://scikit-learn.org/): datasets and preprocessing
- Digi Skills Program: learning platform

---

If this repository helped you, consider giving it a ⭐.
