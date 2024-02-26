class TextSplitter:
    def __init__(self) -> None:
        self.window_size = 500
        self.stride = 200

    def split_text(self, list_text):
        all_text = "\n".join(list_text)
        chunks = []
        old_start = -1
        start = 0
        len_chunk = 0
        starting_chunk_id = 0
        while start < len(all_text):
            assert start > old_start, "Infinite loop"
            old_start = start
            chunk = {}
            end = start + self.window_size
            if end < len(all_text):
                while end > start + self.stride and all_text[end - 1] not in [" ", "\n", "."]:
                    end -= 1
                # If we didn't find a space, just split at the end of the window
                if end <= start + self.stride:
                    end = start + self.window_size
            chunks.append(all_text[start:end])
            if end >= len(all_text):
                break
            start = end - self.stride
            while start > old_start and all_text[start - 1] not in [" ", "\n", "."]:
                start -= 1
            # If we didn't find a space, just use the start of the window
            if start <= old_start:
                start = end - self.stride
        return chunks

