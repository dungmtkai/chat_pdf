from typing import List

import fitz
from loguru import logger

from src.utils.pre_check import is_mostly_english


class ProcessingPdf:
    def __init__(self) -> None:
        self.threshold = 0.8
        self.max_page = 100

    def extract_text(self, file_name, start_page=1, end_page=None):
        doc = fitz.open(file_name)
        total_pages = doc.page_count
        if end_page is None:
            end_page = total_pages

        page_text = []
        page_number = []
        for i in range(start_page - 1, end_page):
            text = doc.load_page(i).get_text("text")
            if text:
                page_text.append(text)
                page_number.append(i)

        doc.close()
        return page_text, page_number

    def check_condition(self, page_text: List[str], page_number: List[int]):
        # Check the pdf file is empty
        if not page_text:
            return {"status": "error", "message": "The pdf is empty"}
        
        # Check if the file meets the condition of containing 80% of English content.
        if not is_mostly_english(page_text, self.threshold):
            logger.info("The text is not mostly in English.")
            return {"status": "error", "message": "The text is not mostly in English."}

        # Check if number page of pdf is smaller 100 pages
        if len(page_number) > self.max_page:
            logger.info(
                "The page number of pdf file is bigger than 100 pages.")
            return {
                "status": "error",
                "message": "The page number of pdf file is bigger than 100 pages.",
            }

        return {
            "status": "success",
            "message": "Extract and pass conditions",
        }

    def validate_pdf_extraction(self, file_name, start_page, end_page):
        page_text, page_number = self.extract_text(
            file_name, start_page, end_page)
        response = self.check_condition(page_text, page_number)
        return response
