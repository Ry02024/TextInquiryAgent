import google.generativeai as genai
import numpy as np
# 埋め込みベクトルの計算
def embed_fn(text, model, ai):
    # API_KEY を genai.embed_content に渡す際は正しい引数名を使用する
    return ai.embed_content(model=model,
                               content=text,
                               task_type="retrieval_document",
                               )["embedding"]

# 最良のパッサージを見つける関数
def find_best_passage(query, dataframe, model, ai):
    query_embedding = genai.embed_content(model=model,
                                          content=query,
                                          task_type="retrieval_query")["embedding"]
    dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding)
    idx = np.argmax(dot_products)
    return dataframe.iloc[idx]['Text']
