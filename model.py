from tensorflow import keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

def get_model(input_shape, num_classes):
    # 加载ResNet50预训练模型，去掉顶部全连接层
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

    # 添加自定义的全连接层
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)

    # 构建新模型
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # 编译模型
    optimizer = Adam(lr=0.001)
    loss = 'categorical_crossentropy'
    metrics = ['accuracy']
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    
    return model

# def get_model(width, height, num_classes):
    # model = keras.models.Sequential()
    # # 卷积层1，32个3*3的卷积核，输出维度为(48,48,32)，因为是灰度图像所以是(width,height,1)的
    # model.add(keras.layers.Conv2D(filters=32,kernel_size=3,
    #                             padding='same',activation='relu',
    #                             input_shape=(width,height,1)))
    # # model.add(keras.layers.BatchNormalization())

    # # 卷积层2，32个3*3的卷积核，输出维度为(48,48,32)。
    # model.add(keras.layers.Conv2D(filters=32,kernel_size=3,
    #                             padding='same',activation='relu'))
    # # model.add(keras.layers.BatchNormalization())

    # # 池化层1，2*2的池化核，输出维度为(24,24,32)。
    # model.add(keras.layers.MaxPool2D(pool_size=2))

    # # 卷积层3，64个3*3的卷积核，输出维度为(24,24,64)。
    # model.add(keras.layers.Conv2D(filters=64,kernel_size=3,
    #                             padding='same',activation='relu'))
    # # model.add(keras.layers.BatchNormalization())

    # # 卷积层4，64个3*3的卷积核，输出维度为(24,24,64)。
    # model.add(keras.layers.Conv2D(filters=64,kernel_size=3,
    #                             padding='same',activation='relu'))
    # # model.add(keras.layers.BatchNormalization())

    # # 池化层2，2*2的池化核，输出维度为(12,12,64)。
    # model.add(keras.layers.MaxPool2D(pool_size=2))

    # # 卷积层5，128个3*3的卷积核，输出维度为(12,12,128)。
    # model.add(keras.layers.Conv2D(filters=128,kernel_size=3,
    #                             padding='same',activation='relu'))
    # # model.add(keras.layers.BatchNormalization())

    # # 卷积层6，128个3*3的卷积核，输出维度为(12,12,128)。
    # model.add(keras.layers.Conv2D(filters=128,kernel_size=3,
    #                             padding='same',activation='relu'))
    # # model.add(keras.layers.BatchNormalization())

    # # 池化层3，2*2的池化核，输出维度为(6,6,128)。
    # model.add(keras.layers.MaxPool2D(pool_size=2))

    # # 扁平化层，将三维的矩阵转换为一维向量，输出维度为(66128)。
    # model.add(keras.layers.Flatten())
    # # model.add(keras.layers.AlphaDropout(0.5))

    # # 全连接层1，128个神经元，输出维度为(128)。
    # model.add(keras.layers.Dense(128,activation='relu'))

    # # Dropout层，随机失活40%的神经元。
    # model.add(keras.layers.Dropout(0.4))

    # # 全连接层2，num_classes个神经元，输出维度为(num_classes)。
    # model.add(keras.layers.Dense(num_classes,activation='softmax'))
    # # adam=tf.optimizers.Adam(lr=0.01)
    # # callbacks=[keras.callbacks.EarlyStopping(patience=5,min_delta=1e-3)]

    # # 编译模型，其中使用adam优化器、交叉熵损失函数和精确度作为评估指标。
    # model.compile(optimizer='adam',
    #             loss='categorical_crossentropy',
    #             metrics=['accuracy'],
    #             )
    # model.summary()
    # return model