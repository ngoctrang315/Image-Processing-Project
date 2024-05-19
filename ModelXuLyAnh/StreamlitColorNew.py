import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3
import os
def main_Color():
    global file_uploaded
    st.subheader("Chương 3")
    file_uploaded = st.file_uploader("Open an Color Image", type=["jpg", "tif", "bmp", "gif", "png"])

    if file_uploaded is not None:
        imgin = cv2.imdecode(np.fromstring(file_uploaded.read(), np.uint8), cv2.IMREAD_COLOR)
        #st.image(imgin, channels="BGR", caption="Input Image")

        col1, col2= st.columns([3, 3])
        with col1:
            st.subheader("Input Image")
            st.image(imgin, channels="BGR", use_column_width=True)
        with col2:
            st.subheader("Output Image")

        st.subheader("Buttons")
        buttons_layout = st.columns(4)

        if buttons_layout[0].button("HistEqualColor"):
            st.session_state.imgout = c3.HistEqualColor(imgin)
            st.session_state.caption= "HistEqualColor Image"
            display_image_color(col2, st.session_state.imgout, "HistEqualColor Image")


    if st.sidebar.button("Save Image"):
        if st.session_state.imgout is not None:
            # Th15.save_image2(st.session_state.imgout,file_uploaded)
            save_image(st.session_state.imgout)
        else:
            st.sidebar.warning("Không có ảnh đầu ra để lưu.")

def save_image(image):
    output_folder = st.sidebar.text_input("Nhập đường dẫn đến thư mục:", placeholder="path/to/output/folder")
    if output_folder:
        if os.path.isdir(output_folder):
            input_filename = os.path.basename(file_uploaded.name)
            output_filename = f"{st.session_state.caption}"+"_"+os.path.splitext(input_filename)[0] +".jpg"
            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, image)
            st.sidebar.success(f"Ảnh đã được lưu vào: {output_path}")
        else:
            st.sidebar.warning("Đường dẫn thư mục không hợp lệ.")
    else:
        st.sidebar.warning("Vui lòng nhập đường dẫn đến thư mục.")
def display_image_color(column, img, caption):
    column.image(img, caption, use_column_width=True,channels="BGR")
   