# ---------------- Day 1 Functions ----------------
# vowels in the word
def vowelCounter(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    print("The number of vowels is : ", count)

# "i" location finder

def find_i_positions(input_string):
    for idx in range(len(input_string)):
        if input_string[idx].lower() == "i":
            print(f"Found 'i' at position: {idx}")

# multiplication table
def multiplicationTable(base_num):
    for i in range(1, int(base_num) + 1):
        for k in range(1, i + 1):
            print(f"{i}x{k} = {k * i}", end="\t")
        print()

# mario pyramid
def marioPyramid(pyramid_size):
    for i in range(1, int(pyramid_size) + 1):
        print(" " * (int(pyramid_size) - i) + "*" * i)

# ---------------- Day 2 Functions ----------------

# mario pyramid with list
def marioPyramidList():
    base_list = [" "] * 5
    for i in range(len(base_list) + 1):
        if i != 0:
            base_list[-i] = "*"
        print("".join(base_list))

# sort list asc/desc
def listSorter(input_list):
    print(f"The list : {input_list}")
    asc = sorted(input_list)
    print(f"The list in ascending order : {asc}")
    desc = list(reversed(asc))
    print(f"The list in descending order : {desc}")

# multiplication table as lists
def multiplyList(user_input):
    for i in range(1, int(user_input) + 1):
        results = [k * i for k in range(1, i + 1)]
        print(results)

# username check
# print all domains from valid email list
def print_valid_domains(email_list):
    filtered_emails = filter(emailVerify, email_list)
    domains = [getDomain(addr) for addr in filtered_emails if getDomain(addr) is not None]
    print("Valid domains are:", domains)

# email verify
def emailVerify(email):
    if email.count("@") == 1 and "." in email:
        username, domain = email.split("@")
        if username and domain and domain[0] != "." and domain[-1] != ".":
            domain_parts = domain.split(".")
            if all(part for part in domain_parts):
                return True
    return False

# ---------------- Day 3 Functions ----------------

# login check
def user_login(user, passwd):
    accounts = {"ahmed": "123", "ali": "456", "john": "789"}
    if user in accounts:
        if passwd == accounts[user]:
            print("Access granted. Hello!")
        else:
            print("Wrong password.")
    else:
        print("User not found.")

# extract domains from emails
def getDomain(email):
    if "@" in email:
        return email.split("@")[1]
    return None

# email verify with exception
def verify_email_exception(email):
    try:
        if not email or ("@" not in email) or ("." not in email):
            raise ValueError("Email must contain \"@\" and \".\"")
        at_index = email.find("@")
        dot_index = email.find(".", at_index)
        if at_index < 1 or dot_index == -1 or dot_index == len(email) - 1:
            raise ValueError("Invalid \"@\" or \".\" position")
        if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
            raise ValueError("Email cannot start or end with \"@\" or \".\"")
        return True
    except Exception:
        print("Invalid email. Please enter a valid email address.")
        return False
