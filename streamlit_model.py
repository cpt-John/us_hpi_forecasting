import tensorflow as tf
from keras.models import load_model
import pandas as pd
import numpy as np
from joblib import load

serialized_fpath = './serialized'

model = load_model(f'{serialized_fpath}/keras.model')
scaler_X, scaler_y = load(f'{serialized_fpath}/scaler.joblib')
features_info = load(f'{serialized_fpath}/features_info.joblib')


def df_to_LSTM_input(df: pd.DataFrame, window=1, ):
    df_ = pd.DataFrame(df.apply(
        list, axis=1)).reset_index()
    df_ = df_.apply(lambda x: list(df_[0][max(
        int(x.name)-window, 0):int(x.name)].values), axis=1)
    return df_[window:].to_list()


def get_features_info():
    return features_info


def gradient_importance(seq, model):
    seq = tf.Variable(seq[np.newaxis, :, :], dtype=tf.float32)
    with tf.GradientTape() as tape:
        predictions = model(seq)
    grads = tape.gradient(predictions, seq)
    grads = tf.reduce_mean(grads, axis=1).numpy()[0]

    return grads


def forecast_(features_val):
    df = pd.DataFrame(columns=features_val.keys())
    df.loc[0] = [val*0.99 for val in features_val.values()]
    df.loc[1] = features_val.values()
    df.loc[2] = 0
    df.reset_index(inplace=True, drop=True)
    df = df[list(features_info.keys())]
    # scaling
    df_X, df_y = df.drop(
        "HPI", axis=1), df[["HPI"]]
    scaled_X, scaled_y = pd.DataFrame(scaler_X.transform(
        df_X), columns=df_X.columns), pd.DataFrame(scaler_y.transform(df_y), columns=df_y.columns)
    df_scaled = scaled_X.join(scaled_y)
    # transforming
    X = df_to_LSTM_input(df_scaled, 2)
    predicted = model.predict(X)
    predicted = scaler_y.inverse_transform(
        pd.DataFrame(predicted)).flatten()[0]
    importance = [gradient_importance(np.array(seq), model) for seq in X]
    importance_df = pd.DataFrame(
        importance, columns=list(map(lambda f: f['name'], features_info.values())), index=["value"])
    return [predicted, importance_df]
