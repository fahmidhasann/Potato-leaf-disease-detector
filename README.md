
# 🥔 Potato Leaf Disease Detector

A machine learning-powered web application for detecting diseases in potato leaves using computer vision. This project uses a fine-tuned ResNet18 model to classify potato leaf images into three categories: Early Blight, Healthy, and Late Blight.

## 🌟 Live Demo

**🔗 [Try the app live on Hugging Face Spaces!](https://huggingface.co/spaces/fahmidhasan/Potato-Leaf-Disease-Detector)**

## 🚀 Features

- **Real-time Disease Detection**: Upload an image of a potato leaf and get instant disease classification
- **Three Disease Categories**: 
  - Early Blight
  - Healthy
  - Late Blight
- **User-friendly Interface**: Built with Gradio for easy interaction
- **High Accuracy**: Trained using FastAI with data augmentation techniques

## 🛠️ Tech Stack

- **Deep Learning Framework**: FastAI
- **Model Architecture**: ResNet18 (pre-trained and fine-tuned)
- **Web Interface**: Gradio
- **Backend**: PyTorch
- **Development Environment**: Jupyter Notebook

## 📋 Prerequisites

- Python 3.7+
- pip package manager

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fahmidhasann/Potato-leaf-disease-detector.git
   cd Potato-leaf-disease-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the trained model**
   - The application expects a `model.pkl` file in the root directory
   - Train your own model using the provided Jupyter notebook, or
   - Download a pre-trained model (if available)

## 🚀 Usage

### Running the Web Application

```bash
python app.py
```

The application will launch a Gradio interface where you can:
1. Upload an image of a potato leaf
2. Get instant disease classification with confidence scores
3. View results for Early Blight, Healthy, and Late Blight categories

### Training Your Own Model

1. **Open the Jupyter notebook**
   ```bash
   jupyter notebook Potato_Disease_Detector.ipynb
   ```

2. **Prepare your dataset**
   - Organize images in folders by disease category
   - Update the data path in the notebook

3. **Run the notebook cells** to:
   - Load and verify images
   - Create data loaders with augmentation
   - Fine-tune the ResNet18 model
   - Export the trained model as `model.pkl`

## 📊 Model Details

- **Architecture**: ResNet18 (transfer learning)
- **Training Technique**: Fine-tuning with FastAI
- **Data Augmentation**: Rotations up to 180 degrees
- **Validation Split**: 80/20 train-validation split
- **Evaluation Metrics**: Error rate and confusion matrix

## 🗂️ Project Structure

```
Potato-leaf-disease-detector/
├── app.py                          # Gradio web application
├── Potato_Disease_Detector.ipynb   # Model training notebook
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # Apache 2.0 License
└── model.pkl                       # Trained model (generated after training)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍🎓 Author

**Fahmid Hasan Taohid**  
*B.Sc.Ag(Hons), Bangladesh Agricultural University, Mymensingh*  
📧 Email: taohid.2102010@bau.edu.bd

## 🙏 Acknowledgments

- FastAI team for the excellent deep learning framework
- Gradio team for the intuitive web interface library
- The open-source community for the tools and libraries used

## ⚠️ Disclaimer

This tool is for educational and research purposes. For critical agricultural decisions, please consult with agricultural experts and use professional diagnostic methods.
