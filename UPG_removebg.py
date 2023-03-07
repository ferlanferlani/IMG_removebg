import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="UPG background remover")

st.write("## UPG Remove Background")
st.write("*Builth with :heart: by [Ferlan Ferlani](http://ferlanferlani.rf.gd)*")
st.write(
    "Hallo teman teman selamat datang! ini adalah aplikasi web yang dapat teman teman gunakan untuk melakukan hapus pada background gambar berupa foto, logo dll.")
st.write(
    "Caranya cukup mudah teman teman tinggal upload gambar yang ingin teman teman hapus backgroundnya lihat ke arah sidebar klik 'Browse Files', tunggu prosesnya sampai selesai dan untuk mendownload hasilnya teman teman bisa langsung klik 'Download Result'"
)
st.write("Selamat mecoba:grin:")
st.sidebar.write("## Upload dan download :gear:")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Gambar Original :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Hasil Remove Background :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download Result", convert_image(fixed), "UPG_removebg.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload Gambar", type=["png", "jpg", "jpeg"])


if my_upload is not None:
    fix_image(upload=my_upload)
    
else:
    fix_image("./upg.png")
