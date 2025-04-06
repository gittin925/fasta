import streamlit as st
from Bio import SeqIO
import io

st.set_page_config(page_title="FASTA 配列カウンター", layout="centered")
st.title("🧬 FASTAファイルの配列数をカウントするアプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("FASTAファイルをアップロードしてください", type=["fasta", "fa"])

if uploaded_file is not None:
    try:
        # バイナリからテキストに変換
        stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
        records = list(SeqIO.parse(stringio, "fasta"))

        num_sequences = len(records)
        st.success(f"✅ 配列の数: {num_sequences}")

        # 各配列のヘッダー（ID）を表示
        st.subheader("📋 配列ヘッダー一覧")
        for i, record in enumerate(records, start=1):
            st.write(f"{i}. {record.id}")

    except Exception as e:
        st.error("❌ FASTAファイルの読み込みに失敗しました。形式を確認してください。")
        st.exception(e)
else:
    st.info("⬆️ 上の欄からFASTAファイルをアップロードしてください。")
