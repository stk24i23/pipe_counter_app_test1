
import streamlit as st

st.set_page_config(
    page_title="PNGアップロード・ダウンロード",
    page_icon="🖼️"
)

st.title("PNGアップロード・ダウンロードアプリ")
st.write("PNG画像をアップロードして、ダウンロードできます。")

uploaded_file = st.file_uploader(
    "PNG画像を選択してください",
    type=["png"]
)

if uploaded_file is not None:
    image_data = uploaded_file.getvalue()

    if not image_data.startswith(b"\x89PNG\r\n\x1a\n"):
        st.error("正しいPNGファイルをアップロードしてください。")
    else:
        st.success("画像のアップロードが完了しました。")

        st.image(
            image_data,
            caption=uploaded_file.name,
            use_container_width=True
        )

        st.download_button(
            label="PNG画像をダウンロード",
            data=image_data,
            file_name=uploaded_file.name,
            mime="image/png"
        )
