import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import shutil
import os
from google.cloud import storage


def summarization(text: str):
    os.makedirs('output', exist_ok=True)

    storage_client = storage.Client.from_service_account_json('service-account-key.json')
    bucket = storage_client.bucket('fir-example-template.appspot.com')
    blobs = bucket.list_blobs(prefix="ml/output/")
    for blob in blobs:
        if blob.name == 'ml/output/':
            continue
        down_load(blob.name, bucket)

    tokenizer = AutoTokenizer.from_pretrained('sonoisa/t5-base-japanese')
    model = AutoModelForSeq2SeqLM.from_pretrained('output/')

    input = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)

    model.eval()
    result = ''
    with torch.no_grad():
        summary_ids = model.generate(input)
        for id in summary_ids:
            result += tokenizer.decode(id)

    shutil.rmtree('output')
    return result


def down_load(file_name, bucket):
    blob = storage.Blob(file_name, bucket)

    content = blob.download_as_string()
    with open(file_name.lstrip('ml/'), mode='wb') as f:
        f.write(content)
