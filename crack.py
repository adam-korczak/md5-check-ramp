import hashlib


def check_md5_hash(hash_to_check, salt, string_file_path):
    with open(string_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            hashed_string = hashlib.md5((line + salt).encode()).hexdigest()
            if hashed_string == hash_to_check:
                return line
    return None


# Example usage
md5_hash = '568fc2dfd281e9b6eb0e4211455c2e35'
salt = 'c925c9a25bfd'

strings_file_path = 'word-list-7-letters.txt'

result = check_md5_hash(md5_hash, salt, strings_file_path)
if result:
    print("Match found:", result)
else:
    print("No match found.")
