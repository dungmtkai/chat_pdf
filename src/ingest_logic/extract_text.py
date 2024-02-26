import fitz

class TextExtraction:
    def __init__(self) -> None:
        pass

    def extract_text(self, file_name, start_page=1, end_page=None):
        doc = fitz.open(file_name)
        total_pages = doc.page_count
        if end_page is None:
            end_page = total_pages

        page_infos = []
        for i in range(start_page - 1, end_page):
            text = doc.load_page(i).get_text("text")
            page_infos.append({
                "text": text,
                "page": i
            })

        doc.close()
        return page_infos

if __name__ == "__main__":
    file_name = "dataset/testv1.pdf"
    extraction = TextExtraction()
    extraction.extract_text(file_name, 1)
