import streamlit as st
from rembg import remove
from PIL import Image
import time
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Background Image Remover")

st.write("## IMG Remove Background")
st.write("*Develop by [Ferlan Ferlani](http://ferlanferlani.rf.gd)*")
st.write(
    "Hallo teman teman selamat datang! ini adalah aplikasi web yang dapat teman teman gunakan untuk melakukan hapus background pada gambar berupa foto, logo dll.")
st.write(
    "Caranya cukup mudah teman teman tinggal upload gambar yang ingin teman teman hapus backgroundnya lihat ke arah sidebar klik 'Browse Files' tunggu prosesnya hingga selesai dan untuk mendownload hasilnya teman teman bisa langsung klik 'Download Result'"
)
st.write("Selamat mecoba:grin:")
st.sidebar.write("## Upload dan download :gear:")

# Download the fixed image1
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

st.header("Sample")
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Gambar Original")
    col1.image(image)
    
    # alert process delay
    with st.spinner(text="processing remove background") :
        time.sleep(25)
        
    fixed = remove(image)
    col2.write("Hasil Remove Background")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    
        
    st.sidebar.download_button("Download Result", convert_image(fixed), "IMG_bgremover.png", "image/png")
    

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload Gambar", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
    
else:
    fix_image("./monkey.jpeg")
