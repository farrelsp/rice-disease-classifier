import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Rice Disease Information",  # <- This is the browser tab title
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

# Sidebar: Team Info
st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 RusselbinMitchel Team")
st.sidebar.markdown("""
- Farrel Satya Putra
- Made Arbi Parameswara
- Muhammad Fahmy Nadhif 
- Adi Wahyu Candra 
- Fahmi Sajid
""")

texts = {
  "title": {
    "English": "🌾 Rice Leaf Disease Information",
    "Bahasa Indonesia": "🌾 Informasi Penyakit Daun Padi"
  },
  "description": {
    "English": "Learn more about the diseases and how to prevent or control them.",
    "Bahasa Indonesia": "Pelajari lebih lanjut tentang penyakit dan cara mencegah atau mengendalikannya."
  },
  "prevention": {
    "English": "Prevention & Control Measures:",
    "Bahasa Indonesia": "Langkah Pencegahan & Pengendalian:"
  },
  "diseases": {
    "Bacterial leaf blight": {
      "en_name": "Bacterial Leaf Blight",
      "id_name": "Hawar Daun Bakteri",
      "en_desc": "A bacterial disease that causes wilting and yellowing of rice leaves, usually in warm, humid climates.",
      "id_desc": "Penyakit bakteri yang menyebabkan layu dan menguning pada daun padi, biasanya di iklim hangat dan lembap.",
      "en_prevent": [
        "Use resistant rice varieties.",
        "Avoid excessive nitrogen fertilizers.",
        "Maintain proper field drainage.",
        "Use certified seeds and practice crop rotation."
      ],
      "id_prevent": [
        "Gunakan varietas padi tahan penyakit.",
        "Hindari penggunaan pupuk nitrogen yang berlebihan.",
        "Jaga saluran air sawah agar tidak tergenang.",
        "Gunakan benih bersertifikat dan lakukan rotasi tanaman."
      ]
    },
    "Brown spot": {
      "en_name": "Brown Spot",
      "id_name": "Bintik Cokelat",
      "en_desc": "A fungal disease that causes brown lesions on leaves and reduces grain yield.",
      "id_desc": "Penyakit jamur yang menyebabkan lesi coklat pada daun dan mengurangi hasil biji-bijian.",
      "en_prevent": [
        "Use balanced fertilizers (especially potassium).",
        "Ensure good drainage and avoid water stagnation."
        "Use resistant varieties and treat seeds with fungicide."
      ],
      "id_prevent": [
        "Gunakan pupuk berimbang (terutama kalium).",
        "Pastikan drainase yang baik dan hindari genangan air.",
        "Gunakan varietas yang tahan dan obati benih dengan fungisida.",
      ]
    },
    "Healthy": {
      "en_name": "Healthy",
      "id_name": "Sehat",
      "en_desc": "Leaves are green and free from visible symptoms or infections.",
      "id_desc": "Daunnya hijau dan bebas dari gejala atau infeksi yang terlihat.",
      "en_prevent": [
        "Continue good agricultural practices.",
        "Monitor crops regularly for early signs of stress or disease."
      ],
      "id_prevent": [
        "Lanjutkan praktik pertanian yang baik.",
        "Pantau tanaman secara teratur untuk mengetahui tanda-tanda awal stres atau penyakit.",
      ]
    },
    "Leaf smut": {
      "en_name": "Leaf Smut",
      "id_name": "Api Daun",
      "en_desc": "Caused by a fungal pathogen, this disease forms blackish spots or streaks on leaves.",
      "id_desc": "Disebabkan oleh patogen jamur, penyakit ini membentuk bintik-bintik atau garis-garis kehitaman pada daun.",
      "en_prevent": [
        "Avoid excessive nitrogen application.",
        "Apply recommended fungicides when early symptoms appear."
        "Ensure adequate plant spacing and ventilation."
      ],
      "id_prevent": [
        "Hindari pemberian nitrogen berlebihan.",
        "Terapkan fungisida yang direkomendasikan saat gejala awal muncul.",
        "Pastikan jarak tanaman dan ventilasi yang memadai.",
      ]
    }
  }
}

current_lang = st.session_state.language

st.title(texts["title"][current_lang])
st.markdown(texts["description"][current_lang])

# Display each disease section
for disease_key, info in texts["diseases"].items():
  name = info["en_name"] if current_lang == "English" else info["id_name"]
  desc = info["en_desc"] if current_lang == "English" else info["id_desc"]
  prevent = info["en_prevent"] if current_lang == "English" else info["id_prevent"]

  st.subheader(f"🦠 {name}")
  image_file = f"assets/{disease_key.lower().replace(' ', '_')}.jpg"
  st.image(image_file, caption=name, use_container_width=True)
  st.markdown(f"**{desc}**")
  st.markdown(f"**{texts['prevention'][language]}**")
  for step in prevent:
      st.markdown(f"- {step}")
  st.markdown("---")

# Footer 
st.markdown("""
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        © 2025 RusselbinMitchel | Built with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)