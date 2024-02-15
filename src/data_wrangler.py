# def load_data(filepath):
#     import pandas as pd
#     data = pd.read_csv(filepath)
#     return data


def clean_text(text):
    # text = wordopt(text)
    # text = vectorization(text)
    text = embeddings(text)
    return text


def wordopt(text):
    import re
    text = text.lower()                               # Convert to lowercase
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'\W', ' ', text)                   # Replace non-word characters with a space
    text = re.sub(r'\n', '', text)                    # Remove newline characters
    text = re.sub(r' +', ' ', text)                   # Replace multiple spaces with a single space
    text = re.sub(r'^ ', '', text)                    # Remove leading space
    text = re.sub(r' $', '', text)                    # Remove trailing space
    return text


def vectorization(text):
    # import the model
    import pickle
    import pandas as pd
    model_vec=pickle.load(open('./models/vectorization.pkl', 'rb'))
    text=model_vec.transform(pd.Series(text))
    return text


def embeddings(text):
    from sentence_transformers import SentenceTransformer
    model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
    text_list=[]
    text_list.append(text)
    text = model_embedding.encode(text_list)
    return text
    