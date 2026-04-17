import keyword

PY_KEYWORDS = set(keyword.kwlist)

def classify(token):
    if token in PY_KEYWORDS:
        return "Keyword"
    elif token.isdigit():
        return "Literal"
    elif token in ["=", "+", "-", "*", "/", "=="]:
        return "Operator"
    elif token == ";":
        return "Punctuation"
    else:
        return "Identifier"

def main():
    code = "int sum = 10; a + b = 20; this is a keyword"

    tokens = code.replace(";", " ;").split()

    for t in tokens:
        print(f"{t} -> {classify(t)}")

if __name__ == "__main__":
    main()