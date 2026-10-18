
import streamlit as st
from pypdf import PdfReader

from comparison import compare_documents
from report_generator import generate_report


st.set_page_config(
    page_title="AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Comparison Assistant")
st.write(
    "Upload two PDF documents to generate AI-powered "
    "summaries, similarities, differences and a report."
)


def extract_text(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += (page.extract_text() or "") + "\n"

        return text.strip(), len(reader.pages)

    except Exception:
        return "", 0


# Upload section
col1, col2 = st.columns(2)

with col1:
    file_a = st.file_uploader(
        "📄 Upload Document A",
        type=["pdf"],
        key="file_a"
    )

with col2:
    file_b = st.file_uploader(
        "📄 Upload Document B",
        type=["pdf"],
        key="file_b"
    )


# Comparison button
if st.button("🔍 Compare Documents", type="primary"):

    if file_a is None or file_b is None:
        st.warning("Please upload both PDF documents.")

    elif file_a.size == 0 or file_b.size == 0:
        st.error("One of the uploaded PDF files is empty.")

    else:
        with st.spinner("Extracting PDF text..."):
            text_a, pages_a = extract_text(file_a)
            text_b, pages_b = extract_text(file_b)

        if not text_a or not text_b:
            st.error(
                "No readable text found. "
                "Please upload text-based PDF documents."
            )

        else:
            st.success("Both PDF files were read successfully!")

            with st.expander("📑 Document Information"):
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Document A")
                    st.write("File:", file_a.name)
                    st.write("Pages:", pages_a)
                    st.write("Characters:", len(text_a))
                    st.text_area(
                        "Preview A",
                        text_a[:1000],
                        height=180
                    )

                with col2:
                    st.subheader("Document B")
                    st.write("File:", file_b.name)
                    st.write("Pages:", pages_b)
                    st.write("Characters:", len(text_b))
                    st.text_area(
                        "Preview B",
                        text_b[:1000],
                        height=180
                    )

            with st.spinner("AI is comparing your documents..."):
                try:
                    result = compare_documents(text_a, text_b)

                    report = generate_report(
                        result,
                        file_a.name,
                        file_b.name
                    )

                    st.session_state["result"] = result
                    st.session_state["report"] = report
                    st.session_state["file_names"] = (
                        file_a.name,
                        file_b.name
                    )

                except Exception as e:
                    st.error(f"Comparison failed: {e}")


# Display saved comparison results
if "result" in st.session_state:

    st.divider()
    st.success("AI comparison completed successfully!")

    st.subheader("🤖 AI Comparison Results")
    st.markdown(st.session_state["result"])

    st.divider()

    st.download_button(
        label="📥 Download Comparison Report (DOCX)",
        data=st.session_state["report"],
        file_name="AI_Document_Comparison_Report.docx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        )
    )

