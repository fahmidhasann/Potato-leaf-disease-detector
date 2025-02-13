import gradio as gr
import torch
from fastai.vision.all import *

# Load the model
learn = load_learner("model.pkl")

# Define classes
labels = ["Early Blight", "Healthy", "Late Blight"]

# Prediction function
def predict(img):
    img = PILImage.create(img)
    pred, _, probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

# Gradio UI
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(),
    title="Potato Leaf Disease Detector",
    description="Upload an image of a potato leaf to detect disease.",
)

if __name__ == "__main__":
    interface.launch()
