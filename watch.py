import re

def main():
    print(parse(input("HTML: ")))
#piyushgopal
def parse(s):
    # extract URL with src
    URL = re.search(r'src=[\'"]([^\'"]+)', s)
    if URL:
        URL = URL.group(1)
        youtubeLink = re.search(r'(youtube)', URL)
        if youtubeLink:
        #piyushgopal     # extract youtube ID
            ytID = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", URL)
            return f"https://youtu.be{ytID}"
        else:
            return None

#piyushgopal
if __name__ == "__main__":
    main()
