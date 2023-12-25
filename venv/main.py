text1 = list()
book = dict()
class Count_procent_symvols():
    def count_symvols(self, start_text):
        start_text.readlines()
        text = ""
        for i in start_text:
            text += i
        text.lower()
        text = text.replace(",", "")
        text = text.replace(":", "")
        text = text.replace(".", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace("...", "")
        text = text.replace("-", "")
        text = text.replace("_", "")
        text = text.replace(")", "")
        text = text.replace("(", "")
        text = text.replace(";", "")
        text = text.replace(" ", "")
        for i in text:
            text1.append(i)
        text2 = set(text1)
        text3 = list(text2)
        text3.sort()
        for y in range(0, len(text3)):
            values = []
            for u in range(0, len(text1)):
                if text1[u] == text3[y]:
                    values.append(text1[u])
                book[text3[y]] = values
        for a, b in book.items():
            print(a, "- ", len(b) * 100 / len(text1), '%')
        start_text.close()
