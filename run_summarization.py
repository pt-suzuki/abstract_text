from transformers import pipeline

nlp = pipeline('summarization')

text = 'Huggingface Transformers is a deep learning framework provided ' \
       'by Huggingface that specializes in natural language processing. It' \
       'supports both TensorFlow and PyTorch. You can use deep learning to solve' \
       'natural language processing tasks such as text classification, question' \
       'answering, and summary.'

print(nlp(text, max_length=20, min_length=10))
