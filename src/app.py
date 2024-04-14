import streamlit as st
import google.generativeai as genai
from documents import get_documents
from embedding_utils import embed_fn, find_best_passage
from prompt_utils import make_prompt_jp

# 文書と埋め込みを取得
def load_documents_and_embeddings(api):
    df = get_documents()
    model = 'models/embedding-001'
    df['Embeddings'] = df['Text'].apply(lambda x: embed_fn(x, model=model, ai=api))
    return df

# 回答を生成する
def generate_answer(query, df, ai):
    passage = find_best_passage(query, df, model='models/embedding-001', ai=ai)
    prompt = make_prompt_jp(query, passage)
    answer_bot = ai.GenerativeModel('gemini-pro')
    answer = answer_bot.generate_content(prompt)
    return answer.text

# APIキーの設定とモデルの初期化
def setup_genai():
    API_KEY = st.text_input("APIキーを入力してください:", value="", type="password")
    if API_KEY:
        genai.configure(api_key=API_KEY)
        return genai
    return None

def main():
    st.title("文書検索と回答生成アプリ")
    ai = setup_genai()
    if ai:
        df = load_documents_and_embeddings(ai)
        query = st.text_input("質問を入力してください:")
        if st.button("回答を検索") and query:
            try:
                answer = generate_answer(query, df, ai)
                st.text_area("回答:", value=answer, height=300)
            except Exception as e:
                st.error("エラーが発生しました: " + str(e))

if __name__ == "__main__":
    main()
