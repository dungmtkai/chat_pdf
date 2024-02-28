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

if __name__=="__main__":
    large_text = """
    This is a large text that we want to split into smaller chunks with a window size of 2000 and an overlap of 500. We need to ensure that chunks end at periods ('.'), spaces (' '), or newline characters ('\n').

    For example, this is a long sentence. We will split it into smaller chunks. Each chunk should not exceed the window size, and it should end at a period, space, or newline.

    """
    text_splitter = TextSplitter()
    chunks = text_splitter.split_text(large_text)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk, len(chunk))
        print("=" * 50)
