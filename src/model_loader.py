def load_model(model_path):
    
    # pickle - linear regression
    # import pickle
    # model=pickle.load(open(model_path, 'rb'))
    
    # tensor flow
    from keras.models import load_model
    model=load_model(model_path)

    return model
