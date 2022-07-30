import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

tf.__version__

mnist = tf.keras.datasets.mnist
class_names = ['0','1','2','3','4','5','6','7','8','9']

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 2차원은 흑백만 가능했지만 3차원으로 만듬으로써 RGB를 사용할 수 있게 된다.
train_images_shape = tf.cast(train_images, dtype=tf.float32)
train_images_shape = tf.expand_dims(train_images_shape, axis=-1)

dataset = tf.data.Dataset.from_tensor_slices((train_images_shape, train_labels)).batch(10) #10개의 문제를 한번에 풀기위해

model1 = tf.keras.Sequential() #모델을 1차원으로
model1.add(tf.keras.layers.Conv2D(16,2,padding='SAME'))
model1.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='SAME')) # padding은 동일한 크기의 이미지를 계속 만들기 위해
model1.add(tf.keras.layers.Flatten()) #한줄로 만듬
model1.add(tf.keras.layers.Dense(100)) #100개 뉴론을 다음 레이어에 추가
model1.add(tf.keras.layers.Dense(200))
model1.add(tf.keras.layers.Dense(100))
model1.add(tf.keras.layers.Dense(10, activation='softmax')) #마지막에 10개로 추려냄, softmax로 다시 한번 가장 정확한 것을 추려냄

class TestModel(tf.keras.Model):
    def __init__(self, rate=0.1):
        super(TestModel, self).__init__()
       
        self.conv = tf.keras.layers.Conv2D(16,2,padding='SAME')
        self.maxpool = tf.keras.layers.MaxPool2D(pool_size=2,strides=2,padding='SAME')
        self.flat = tf.keras.layers.Flatten()
        self.dense1 = tf.keras.layers.Dense(100)
        self.dense2 = tf.keras.layers.Dense(200)
        self.dense3 = tf.keras.layers.Dense(100)
        self.final_layer = tf.keras.layers.Dense(10, activation='softmax')
       
    def call(self, inp):
        output = self.conv(inp)
        output = self.maxpool(output)
        output = self.flat(inp)
        output = self.dense1(output)
        output = self.dense2(output)
        output = self.dense3(output)
        final_output = self.final_layer(output)
       
        return final_output

model2 = TestModel()

model1.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model1.fit(dataset, epochs=1)#, validation_data = testset) #학습을 10번 반복함으로써 정확성을 높임
model2.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model2.fit(dataset, epochs=1)#, validation_data = testset) #학습을 10번 반복함

model1.summary()
model2.summary()

test_images_shape = tf.cast(test_images, dtype=tf.float32)
test_images_shape = tf.expand_dims(test_images_shape, axis=-1)
testset = tf.data.Dataset.from_tensor_slices((test_images_shape, test_labels)).batch(10) #학습이 잘 됐는지 테스트 하기 위해

model1.evaluate(testset)

test = tf.expand_dims(test_images[109], 0) #테스트 할 숫자를 리스트에서 고른다
result = model1(test)
result = tf.argmax(result, axis=-1)
print(result)

plt.imshow(test_images[109]) #AI가 보여주는 정답이 맞는지 확인