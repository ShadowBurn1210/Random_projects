import hashlib

# The last password is formatted like user:hash$salt and is generated with the rule 'sha1(md5($p.$s).lc($u))'
# concatenating password with the salt, getting a md5 hash, adding a lowercase username,
# and then hashing the outcome with SHA1.

# full pasword: "saulitis.leo:5585cb1e395cf6aeededb75dcc6049021dcde7df$ZkI4oue3"

target_hash = "5585cb1e395cf6aeededb75dcc6049021dcde7df"
username = "saulitis.leo"
salt = "ZkI4oue3"
wordlist_path = "rockyou.txt"


def custom_hash(password, salt, username):

    # concatenating password with the salt
    md5_input = password + salt

    # getting a md5 hash
    md5_hash = hashlib.md5(md5_input.encode()).hexdigest()

    # adding a lowercase username
    combined = md5_hash + username.lower()

    # hashing the outcome with SHA1
    sha1_hash = hashlib.sha1(combined.encode()).hexdigest()
    return sha1_hash


with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
    for password in wordlist:

        password = password.strip()

        # Recreate the steps used to generate the hash
        generated_hash = custom_hash(password, salt, username)

        # Check if it matches the target hash
        if generated_hash == target_hash:
            print(f"Password found: {password}")
            break
    else:
        print("Password not found in the wordlist.")
