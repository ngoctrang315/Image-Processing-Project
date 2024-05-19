import streamlit as st
import base64

# Thiết lập trang
st.set_page_config(
    page_title="Trang Chào Mừng",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Hàm thêm nền từ file local
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('D:/Year3/HK2/XLA/do_an_cuoi_ki/Image-Processing-Project/background/Home.jpg')

# Tùy chỉnh thanh bên
st.markdown(
    """
    <style>
    [data-testid=stSidebar] {
        background-color: #4B8F8C;
        color: white;
    }
    [data-testid=stSidebar] .css-1d391kg {
        color: white;
    }
    [data-testid=stSidebar] .css-1v3fvcr {
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    [data-testid=stSidebar] .css-qri22k {
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    [data-testid=stSidebar] .css-1y2lm76 {
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tiêu đề chính
st.markdown("<h1 style='font-size: 50px; color: #FFFFFF; text-align: center;'>Welcome to the website!</h1>", unsafe_allow_html=True)

# CSS cho văn bản màu đỏ và các thẻ khác
st.markdown(
    """
    <style>
        .main-text {
            color: #FF6347;
            font-family: 'Arial', sans-serif;
            font-size: 18px;
        }
        .header-text {
            font-size: 40px;
            font-weight: bold;
        }
        .contact-link {
            color: #32CD32;
            text-decoration: none;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Nội dung trang chính
st.markdown(
    """
    <div class="main-text">
        <div class="info-box">
            <p class="header-text">Personal Information:</p>
            <p>- Full name: Tran Thi Ngoc Trang  -  Student code: 21133109</p>
            <p>- Full name: Do Ngoc Han - Student code: 21133030</p>
            <p>- School name: HCMC University of Technology and Education</p>
        </div>
        <div class="info-box" style="margin-top: 20px;">
            <p class="header-text">Instructor Information:</p>
            <p>- Teacher: Tran Tien Duc</p>
        </div>
        <div class="info-box" style="margin-top: 20px;">
            <p class="header-text">Module:</p>
            <p>- Nhận Dạng khuôn mặt</p>
            <p>- Nhận dạng chữ số viết tay MNIST</p>
            <p>- Nhận dạng 5 loại đối tượng dùng Yolov8 (Phương tiện)</p>
            <p>- Xử lý ảnh</p>
            <p>- Đếm số ngón tay</p>
            <p>- Nhận diện thời tiết</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
