import re

def main():
    print(count(input("Text: ")))
#piyushgopal
def count(s):
    return len(re.findall(r"\b(um)|(Um)|('...')", s))

#piyushgopal
if __name__ == "__main__":
    main()
