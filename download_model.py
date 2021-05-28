from keras import applications
from keras.applications import mobilenet

model = mobilenet.MobileNet()
model.save('./mobilenet-model.h5')
