
import cv2
from deepface import DeepFace
from tkinter import Tk, Canvas
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def detectar_emocion():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("foto_usuario.jpg", frame)
        cam.release()
        resultado = DeepFace.analyze(img_path="foto_usuario.jpg", actions=["emotion"])
        emocion = resultado[0]['dominant_emotion']
        return emocion
    else:
        print("Error al acceder a la cámara.")
        return None

def mostrar_arte(emocion):
    ventana = Tk()
    ventana.title(f"Arte basado en la emoción: {emocion}")
    lienzo = Canvas(ventana, width=400, height=400)
    lienzo.pack()

    colores = {
        'happy': 'yellow',
        'sad': 'blue',
        'angry': 'red',
        'surprise': 'purple',
        'fear': 'black',
        'disgust': 'green',
        'neutral': 'gray'
    }

    color = colores.get(emocion, 'white')
    lienzo.create_oval(50, 50, 350, 350, fill=color)
    ventana.mainloop()

if __name__ == "__main__":
    emocion_detectada = detectar_emocion()
    if emocion_detectada:
        print(f"Emoción detectada: {emocion_detectada}")
        mostrar_arte(emocion_detectada)
