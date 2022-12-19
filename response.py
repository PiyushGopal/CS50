from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email address: ")))
#piyushgopal
def validate(s):
    if checkers.is_email(s) == True:
        return "Valid"
    else:
        return "Invalid"
#piyushgopal
if __name__ == "__main__":
    main()
