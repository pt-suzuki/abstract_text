# 要約処理

## 概要
こちらの書籍の4-5要約の写経+fastapiでAPI化

[BERT/GPT-3/DALL-E 自然言語処理・画像処理・音声処理 人工知能プログラミング実践入門](https://www.amazon.co.jp/BERT-GPT-3-DALL-%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E3%83%BB%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%E3%83%BB%E9%9F%B3%E5%A3%B0%E5%87%A6%E7%90%86-%E4%BA%BA%E5%B7%A5%E7%9F%A5%E8%83%BD%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%AE%9F%E8%B7%B5%E5%85%A5%E9%96%80/dp/4862465099/ref=sr_1_28?crid=8T4E44WM7Q0A&keywords=%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86&qid=1664717961&qu=eyJxc2MiOiI1LjcwIiwicXNhIjoiNC45OSIsInFzcCI6IjQuOTAifQ%3D%3D&sprefix=%2Caps%2C153&sr=8-28
)

## インストール
```
pip install -r requirements.txt
```

## ３行要約のデータセットのclone

```
git clone https://github.com/KodairaTomonori/ThreeLineSummaryDataset.git
```

## 学習環境（Huggingface Transformers）のclone

```
git clone https://github.com/huggingface/transformers.git -b v4.4.2
```

## livedoorニュースから3行要約と本文を取得

```
python get_content.py
```

## 取得した値を学習用データに変換

```
python convert.py
```

## 要約の学習

```
python  ./transformers/examples/seq2seq/run_summarization.py \
  --model_name_or_path=sonoisa/t5-base-japanese \
  --do_train \
  --do_eval  \
  --train_file=train.csv  \
  --validation_file=dev.csv \
  --num_train_epochs=10 \
  --per_device_train_batch_size=4 \
  --per_device_eval_batch_size=4 \
  --save_steps=5000 \
  --save_total_limit=3 \
  --output_dir=output/ \å
  --predict_with_generate \
  --use_fast_tokenizer=False \
  --logging_steps=100
```

## APIサーバ（FastAPI）起動

```
uvicorn main:app --reload
```

http://localhost:8000/docs