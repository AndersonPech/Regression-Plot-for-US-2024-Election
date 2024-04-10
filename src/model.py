import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

     

def regression():
    data = pd.read_csv('final.csv')
    train_dataset = data.sample(frac=0.8, random_state=0)
    test_dataset = data.drop(train_dataset.index)

    print(train_dataset.head(20))
    train_features = train_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop('trump')
    test_labels = test_features.pop('trump')


    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(np.array(train_dataset))

    biden = np.array(train_features['biden'])
    biden_normal = tf.keras.layers.Normalization(input_shape=[1,], axis=None)
    biden_normal.adapt(biden)

    layers = tf.keras.layers

    biden_model = tf.keras.Sequential(
        [
            biden_normal,
            layers.Dense(units=1)
        ]
    )

    biden_model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate = 0.1),
        loss='mean_absolute_error'
    )

    history = biden_model.fit(
        train_features['biden'],
        train_labels,
        epochs=100,
        verbose=200,
        validation_split=0.2
    )

    test_results = {}

    test_results['biden_model'] = biden_model.evaluate(
        test_features['biden'],
        test_labels, verbose=0)

    x = tf.linspace(0.0, 100, 100)
    y = biden_model.predict(x)
    print(y)

    plt.scatter(train_features['biden'], train_labels, label='Data')
    plt.plot(x, y, color='k', label='Predictions')
    plt.xlabel('Biden')
    plt.ylabel('Trump')
    plt.legend()
    plt.savefig('Regression Plot')





regression()