
import streamlit as st

st.set_page_config(
    page_title="画像アップロード・ダウンロード",
    page_icon="🖼️",
    layout="centered"
)

st.title("画像アップロード・ダウンロードアプリ")

st.write(
    "PNG・JPG・JPEG画像をアップロードして、"
    "そのままダウンロードできます。"
)

uploaded_file = st.file_uploader(
    "画像ファイルを選択してください",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image_data = uploaded_file.getvalue()

    is_png = image_data.startswith(b"\x89PNG\r\n\x1a\n")
    is_jpeg = image_data.startswith(b"\xff\xd8\xff")

    if not (is_png or is_jpeg):

        st.error(
            "正しいPNGまたはJPG画像をアップロードしてください。"
        )

    else:

        st.success("画像のアップロードが完了しました。")

        st.image(
            image_data,
            caption=uploaded_file.name,
            use_container_width=True
        )

        mime_type = (
            "image/png" if is_png else "image/jpeg"
        )

        st.download_button(
            label="画像をダウンロード",
            data=image_data,
            file_name=uploaded_file.name,
            mime=mime_type
        )
