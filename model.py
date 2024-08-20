from keras.models import load_model # Do działania Keras wymagany jest TensorFlow
from PIL import Image, ImageOps  # Instalowanie poduszki zamiast PIL
import numpy as np
def get_class(model, labels,image):
  np.set_printoptions(suppress=True)
  model = load_model(model, compile=False)
  class_names = open(labels, "r").readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(image).convert("RGB")
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  data[0] = normalized_image_array
  # Przewiduje model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  if confidence_score >= 0.60000000 :
    confidence_score = "Wysoce Prawdopodobne" 
  else:
    confidence_score = "Mniej Prawdopodobne"

  return class_name, confidence_score
