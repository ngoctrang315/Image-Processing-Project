import streamlit as st
import cv2
import sys
import os
import numpy as np
import base64
sys.path.append('D:/Year3/HK2/XLA/do_an_cuoi_ki/Image-Processing-Project/ModelXuLyAnh')
import Chuong3 as c3
import Chuong4 as c4
import Chuong5 as c5
import Chuong9 as c9
import StreamlitColorNew as StCN

st.set_page_config(
    page_title="Xử lý ảnh",
    page_icon="👋",
)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('D:/Year3/HK2/XLA/do_an_cuoi_ki/Image-Processing-Project/Background/XuLyAnh.jpg')  
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #748A88;
    }
</style>
""", unsafe_allow_html=True)
  
st.markdown(
    """
    <style>
    .red-text {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # st.session_state = SessionState()
    if 'imgin' not in st.session_state:
        st.session_state.imgin = None
    if 'imgout' not in st.session_state:
        st.session_state.imgout = None
    if 'caption' not in st.session_state:
        st.session_state.caption=None
    st.title("Computer Vision")
        
    menu = st.sidebar.selectbox("Menu", ("Chuong3", "Chuong4", "Chuong5", "Chuong9"))
    
    if menu == "Chuong3":
        menu = st.sidebar.selectbox("Menu", ("GRAYSCALE Image", "Color Image"))
        if menu=="GRAYSCALE Image":
            chuong3()
        else:
            StCN.main_Color()

    if menu == "Chuong4":
        chuong4()
    if menu=="Chuong5":
        chuong5()
    if menu=="Chuong9":
        chuong9()

def chuong3():
    st.subheader("Chương 3")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])

    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        st.session_state.imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        col1, col2= st.columns([3, 3])
        with col1:
            st.subheader("Input Image")
            st.image(st.session_state.imgin, use_column_width=True)
        with col2:
            st.subheader("Output Image")

        #with col3:
        st.subheader("Buttons")
        buttons_layout = st.columns(4)

        if buttons_layout[0].button("Negative"):
            st.session_state.imgout = c3.Negative(st.session_state.imgin)
            st.session_state.caption= "Nagative Image"
            display_image(col2, st.session_state.imgout, "Negative Image")

        if buttons_layout[1].button("Logaric"):
            st.session_state.imgout = c3.Logarit(st.session_state.imgin)
            st.session_state.caption= "Logaric Image"
            display_image(col2, st.session_state.imgout, "Logaric Image")  

        if buttons_layout[2].button("Power"):
            st.session_state.imgout = c3.Power(st.session_state.imgin)
            st.session_state.caption= "Power Image"
            display_image(col2, st.session_state.imgout, "Power Image")  
        
        if buttons_layout[3].button("PiecewiseLinear"):
            st.session_state.imgout = c3.PiecewiseLinear(st.session_state.imgin)
            st.session_state.caption= "PiecewiseLinear Image"
            display_image(col2, st.session_state.imgout, "PiecewiseLinear Image") 
        
        if buttons_layout[0].button("Histogram"):
            st.session_state.imgout = c3.Histogram(st.session_state.imgin)
            st.session_state.caption= "Histogram Image"
            display_image(col2, st.session_state.imgout, "Histogram Image") 

        if buttons_layout[1].button("HistEqual"):
            st.session_state.imgout = c3.HistEqual(st.session_state.imgin)
            st.session_state.caption= "HistEqual Image"
            display_image(col2, st.session_state.imgout, "HistEqual Image")
            
        if buttons_layout[3].button("LocalHist"):
            st.session_state.imgout = c3.LocalHist(st.session_state.imgin)
            st.session_state.caption= "LocalHist Image"
            display_image(col2, st.session_state.imgout, "LocalHist Image")

        if buttons_layout[0].button("HistStat"):
            st.session_state.imgout = c3.HistStat(st.session_state.imgin)
            st.session_state.caption= "HistStat Image"
            display_image(col2, st.session_state.imgout, "HistStat Image")

        if buttons_layout[1].button("MyBoxFilter"):
            st.session_state.imgout = c3.MyBoxFilter(st.session_state.imgin)
            st.session_state.caption= "MyBoxFilter Image"
            display_image(col2, st.session_state.imgout, "MyBoxFilter Image")
        
        if buttons_layout[2].button("Gauss"):
            st.session_state.imgout = c3.BoxFilter(st.session_state.imgin)
            st.session_state.caption= "Gauss Image"
            display_image(col2, st.session_state.imgout, "BoxFilter Image")

        if buttons_layout[3].button("Threshold"):
            st.session_state.imgout = c3.Threshold(st.session_state.imgin)
            st.session_state.caption= "Threshold Image"
            display_image(col2, st.session_state.imgout, "Threshold Image")
        
        if buttons_layout[0].button("MedianFilter"):
            st.session_state.imgout = c3.MedianFilter(st.session_state.imgin)
            st.session_state.caption= "MedianFilter Image"
            display_image(col2, st.session_state.imgout, "MedianFilter Image")

        if buttons_layout[1].button("Sharpen"):
            st.session_state.imgout = c3.Sharpen(st.session_state.imgin)
            st.session_state.caption= "Sharpen Image"
            display_image(col2, st.session_state.imgout, "Sharpen Image")
        
        if buttons_layout[2].button("Gradient"):
            st.session_state.imgout = c3.Gradient(st.session_state.imgin)
            st.session_state.caption= "Gradient Image"
            display_image(col2, st.session_state.imgout, "Gradient Image")



def chuong4():
    st.subheader("Chương 4")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])
    if st.sidebar.button("DrawNotchRejectFilter"):
        st.session_state.imgout = c4.DrawNotchRejectFilter()
        st.session_state.caption= "DrawNotchRejectFilter"
        st.sidebar.image(st.session_state.imgout,use_column_width=True,caption="DrawNotchRejectFilter")


    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        st.session_state.imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        col1, col2, col3= st.columns([3, 3, 2])
        with col1:
            st.subheader("Input Image")
            st.image(st.session_state.imgin, use_column_width=True)
        with col2:
            st.subheader("Output Image")
        with col3:
            st.subheader("Buttons")
    
            if st.button("Spectrum"):
                st.session_state.imgout = c4.Spectrum(st.session_state.imgin)
                st.session_state.caption= "Spectrum Image"
                display_image(col2, st.session_state.imgout, "Spectrum Image")

            if st.button("FrequencyFilter"):
                st.session_state.imgout = c4.FrequencyFilter(st.session_state.imgin)
                st.session_state.caption= "FrequencyFilter Image"
                display_image(col2, st.session_state.imgout, "FrequencyFilter Image")  
            
            if st.button("RemoveMoire"):
                st.session_state.imgout = c4.RemoveMoire(st.session_state.imgin)
                st.session_state.caption= "RemoveMoire Image"
                display_image(col2, st.session_state.imgout, "RemoveMoire Image") 


def chuong5():
    st.subheader("Chương 5")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])

    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        st.session_state.imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        col1, col2, col3= st.columns([3, 3, 2])
        with col1:
            st.subheader("Input Image")
            st.image(st.session_state.imgin, use_column_width=True)
        with col2:
            st.subheader("Output Image")
        with col3:
            st.subheader("Buttons")

            if st.button("CreateMotionNoise"):
                st.session_state.imgout = c5.CreateMotionNoise(st.session_state.imgin)
                st.session_state.caption= "CreateMotionNoise Image"
                display_image(col2, st.session_state.imgout, "CreateMotionNoise Image")  
            
            if st.button("DenoiseMotion"):
                st.session_state.imgout = c5.DenoiseMotion(st.session_state.imgin)
                st.session_state.caption= "DenoiseMotion Image"
                display_image(col2, st.session_state.imgout, "DenoiseMotion Image") 

            if st.button("DenoisestMotion"):
                st.session_state.temp = cv2.medianBlur(st.session_state.imgin, 7)
                st.session_state.imgout =c5.DenoiseMotion(st.session_state.temp)
                st.session_state.caption= "DenoisestMotion Image"
                display_image(col2, st.session_state.imgout, "DenoisestMotion Image") 

def chuong9():
    st.subheader("Chương 9")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])

    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        st.session_state.imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        col1, col2, col3= st.columns([3, 3, 3])
        with col1:
            st.subheader("Input Image")
            st.image(st.session_state.imgin, use_column_width=True)
        with col2:
            st.subheader("Output Image")
        with col3:
            st.subheader("Buttons")

            if st.button("ConnectedComponen"):
                st.session_state.imgout = c9.ConnectedComponent(st.session_state.imgin)
                st.session_state.caption= "ConnectedComponen Image"
                display_image(col2, st.session_state.imgout, "ConnectedComponen Image")  

            if st.button("CountRice"):
                st.session_state.imgout = c9.CountRice(st.session_state.imgin)
                st.session_state.caption= "CountRice Image"
                display_image(col2, st.session_state.imgout, "CountRice Image")  

def display_image(column, img, caption):
    column.image(img, caption, use_column_width=True)


if __name__ == "__main__":
    main()
