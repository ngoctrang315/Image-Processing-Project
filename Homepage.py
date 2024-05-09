import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon=" ",
)

st.write("<h1 style='font-size: 50px;color:black'>Welcome to the website! </h1>", unsafe_allow_html=True)
st.sidebar.success("You can choose one of my projects above.")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('../Project/background/Home.png')  
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

st.markdown(
"""
    <div class="red-text">
        Hello!
         <p><b style="font-size: 40px;">Personal Information:</b></p>
        <div>
        - Full name: Tran Thi Ngoc Trang</p>
        - Student code: 21133109</p>
        - School name: HCMC University of Technology and Education
        </div>
	<p><b style="font-size: 40px;">Contact me:</b></p>
        <p>- Ngoc Trang: <a style="color:green" href="21133109@student.hcmute.edu.vn">21133109@student.hcmute.edu.vn</a></p>
	<p><b style="font-size: 40px;">Instructor Information:</b></p>
   	<div>
        <p>- Teacher: Tran Tien Duc</p>
        <p>- Email:<a style="color:green" href="ductt@hcmute.edu.vn"> ductt@hcmute.edu.vn</a></p>
	</div>
    </div>
    """,
    unsafe_allow_html=True
)