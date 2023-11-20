# Esta clase servirá para procesar las imagenes con las que se entrenará el modelo
# en TensorFlow
import cv2 as cv        # Importando OpenCV


def cargarImagen(ruta):
    img = cv.imread(ruta)

    if img is None:
        print('No valió verga la imagen')
        return None
    
    cv.imshow('image',img)
    return img

def tratarImagen(img):
    imgResized = cv.resize(img, (28, 28))   # Hay que buscar una resolución apropiada
    return cv.cvtColor(imgResized, cv.COLOR_BGR2RGB)

