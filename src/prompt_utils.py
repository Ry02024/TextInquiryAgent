import textwrap
# プロンプトを作成する関数
def make_prompt_jp(query, relevant_passage):
    escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = textwrap.dedent("""
  あなたは、以下の参考文の文章を使って質問に答える、親切で情報豊富なボットです。\
  関連するすべての背景情報を含め、包括的に、完全な文章で答えるようにしてください。\
  しかし、あなたは専門家ではない聴衆に向かって話しているので、必ず複雑な概念を分解し、 フレンドリーで話しやすい口調で話してください。
  友好的な口調で話してください。\
  その文章が解答に関係ない場合は、無視してもかまいません。

  QUESTION: '{query}'
  PASSAGE: '{relevant_passage}'

    ANSWER:
  """).format(query=query, relevant_passage=escaped)
    return prompt
