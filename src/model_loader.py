def load_model(model_path):
    import pickle
    model=pickle.load(open(model_path, 'rb'))
    return model
