from src.ingest_logic.extract_pdf import extract_text
from src.ingest_logic.split_chunks import TextSplitter
from loguru import logger

class Ingestion:
    def __init__(self) -> None:
        self.text_splitter = TextSplitter()

    def processing_pdf(self, pdf_path, start_page, end_page):
        # Extract text of pdf file
        page_infos = extract_text(pdf_path, start_page, end_page)
        if page_infos:
            all_text = " ".join(content["text"] for content in page_infos)
            # Split chunks
            list_chunks = self.text_splitter.split_text(all_text)

    def insert_collection(self):
        pass


if __name__=="__main__":
    path = "dataset/testv1.pdf"
    ingestation = Ingestion()
    ingestation.processing_pdf(path, 2, None)
