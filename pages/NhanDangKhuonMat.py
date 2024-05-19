import streamlit as st
import numpy as np
import cv2 as cv
import joblib
import base64

# Streamlit configuration
st.set_page_config(
    page_title="Nhận dạng khuôn mặt",
    page_icon="📷",
)

# Function to set background image from local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Setting the background image
add_bg_from_local('../Project/Background/NhanDangKhuonMat.png')

# Custom sidebar style
st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #748A88;
        }
    </style>
    """, unsafe_allow_html=True)

# Custom text color style
st.markdown("""
    <style>
    .red-text {
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize the video capture
FRAME_WINDOW = st.image([])
cap = cv.VideoCapture(0)

# Initialize session state for stopping video capture
if 'stop' not in st.session_state:
    st.session_state.stop = False

# Stop button
press = st.button('Stop')
if press:
    if st.session_state.stop == False:
        st.session_state.stop = True
        cap.release()
    else:
        st.session_state.stop = False

# Load the stop image
if 'frame_stop' not in st.session_state:
    frame_stop = cv.imread('../Project/ModelNhanDangKhuonMat/stop.jpg')
    st.session_state.frame_stop = frame_stop

# Display stop image if capture is stopped
if st.session_state.stop == True:
    FRAME_WINDOW.image(st.session_state.frame_stop, channels='BGR')

# Load face recognition model
svc = joblib.load('../Project/ModelNhanDangKhuonMat/svc.pkl')
mydict = ['NgocHan', 'NgocTrang', 'ThanhHien', 'ThuyLinh', 'TrongDung']

# Function to visualize the detection results
def visualize(input, faces, fps, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            coords = face[:-1].astype(np.int32)
            cv.rectangle(input, (coords[0], coords[1]), (coords[0] + coords[2], coords[1] + coords[3]), (0, 255, 0), thickness)
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)
    cv.putText(input, 'FPS: {:.2f}'.format(fps), (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Main function
def main():
    detector = cv.FaceDetectorYN.create(
        '../Project/ModelNhanDangKhuonMat/face_detection_yunet_2023mar.onnx',
        "",
        (320, 320),
        0.9,
        0.3,
        5000
    )

    recognizer = cv.FaceRecognizerSF.create(
        '../Project/ModelNhanDangKhuonMat/face_recognition_sface_2021dec.onnx',
        ""
    )

    tm = cv.TickMeter()
    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize([frameWidth, frameHeight])

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        # Inference
        tm.start()
        faces = detector.detect(frame)
        tm.stop()

        if faces[1] is not None:
            for idx, face in enumerate(faces[1]):
                face_align = recognizer.alignCrop(frame, face)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                results = [mydict[pred] for pred in test_predict]
                text_to_display = ', '.join(results)
                cv.putText(frame, text_to_display, (int(face[0]), int(face[1]) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw results on the input image
        visualize(frame, faces, tm.getFPS())

        # Visualize results
        FRAME_WINDOW.image(frame, channels='BGR')
    
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
