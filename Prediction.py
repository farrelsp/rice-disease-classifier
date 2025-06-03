import streamlit as st
import time
from PIL import Image
import torch
from torchvision import transforms, models
import torch.nn as nn

st.set_page_config(
    page_title="Rice Disease Classifier",  # <- This is the browser tab title
    page_icon="🌾",                        # <- Optional: tab icon (emoji or URL)
)

# Set default language on first load
if "language" not in st.session_state:
  st.session_state.language = "English"
    
language = st.sidebar.selectbox(
  "🌐 Language / Bahasa",
  options=["English", "Bahasa Indonesia"],
  index=0 if st.session_state.language == "English" else 1
)

# Store selection
st.session_state.language = language

# CLASS LABELS
class_names = {
  "English": ["Bacterial leaf blight", "Brown spot", "Healthy", "Leaf smut"],
  "Bahasa Indonesia": ["Hawar Daun Bakteri", "Bintik Cokelat", "Sehat", "Api Daun"]
}

# LANGUAGE DICT
texts = {
  "title": {
    "English": "🌾 Rice Leaf Disease Classifier",
    "Bahasa Indonesia": "🌾 Klasifikasi Penyakit Daun Padi"
  },
  "description": {
    "English": "Upload an image of a rice leaf and let the model classify it.",
    "Bahasa Indonesia": "Unggah gambar daun padi dan biarkan model mengklasifikasikannya."
  },
  "tab1": {
    "English": "📂 Upload Image",
    "Bahasa Indonesia": "📂 Unggah gambar"
  },
  "tab2": {
    "English": "📸 Webcam",
    "Bahasa Indonesia": "📸 Webcam"
  },
  "tab1-instructions": {
    "English": "Upload a leaf image",
    "Bahasa Indonesia": "Unggah gambar daun padi"
  },
  "tab2-instructions": {
    "English": "Take a photo of the rice leaf",
    "Bahasa Indonesia": "Ambil gambar daun padi"
  },
  "result": {
    "English": "🧠 Prediction:",
    "Bahasa Indonesia": "🧠 Hasil Prediksi:"
  }
}

# MODEL LOADING
@st.cache_resource
def load_model():
  model = models.resnet18(pretrained=False)
  model.fc = nn.Linear(model.fc.in_features, 4)
  model.load_state_dict(torch.load("resnet18_best.pth", map_location="cpu"))
  model.eval()
  return model

def predict(image):
  input_tensor = transform(image).unsqueeze(0)
  with torch.no_grad():
    outputs = model(input_tensor)
    probs = torch.softmax(outputs, dim=1)
    confidence, predicted = torch.max(probs, 1)
    return confidence, predicted

model = load_model()

# IMAGE TRANSFORM
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# STREAMLIT UI
# Sidebar: Team Info
st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 RusselbinMitchel Team")
st.sidebar.markdown("""
- Farrel Satya Putra Mahendra
- Made Arbi Parameswara
- Muhammad Fahmy Nadhif 
- Adi Wahyu Candra 
- Fahmi Sajid
""")

# Main page
current_lang = st.session_state.language

st.title(texts["title"][current_lang])
st.write(texts["description"][current_lang])

# Choice selector
tab1, tab2 = st.tabs(["📂 Upload", "📸 Webcam"])

image = None

with tab1:
  uploaded_file = st.file_uploader(texts["tab1-instructions"][current_lang], type=["jpg", "jpeg", "png"])
  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    confidence, predicted = predict(image)
    st.success(f"{texts['result'][current_lang]} **{class_names[current_lang][predicted.item()]}**")
    st.info(f"Confidence: **{confidence.item():.2%}**")
    
with tab2:
  captured_img = st.camera_input(texts["tab2-instructions"][current_lang])
  if captured_img is not None:
    image  = Image.open(captured_img)
    st.image(image, use_container_width=True)
    confidence, predicted = predict(image)
    st.success(f"{texts['result'][current_lang]} **{class_names[current_lang][predicted.item()]}**")
    st.info(f"Confidence: **{confidence.item():.2%}**")

# Footer 
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        © 2025 RusselbinMitchel | Built with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)