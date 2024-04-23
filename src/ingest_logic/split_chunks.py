class TextSplitter:
    def __init__(self) -> None:
        self.window_size = 500
        self.overlap = 200

    def split_text(self, text):
        chunks = []
        start = 0
        end = self.window_size
        while start < len(text):
            while end < len(text) and text[end] not in [".", " ", "\n"]:
                end += 1
            chunks.append(text[start : end + 1])  # Include the end character
            start = end - self.overlap
            end = start + self.window_size
        return chunks

