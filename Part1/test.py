def fetch_text () :
    with open('data/data.txt') as f:
        lines = f.readlines()
    print(str(lines))

fetch_text()
