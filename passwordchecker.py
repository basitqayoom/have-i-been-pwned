from itertools import count
import requests  # allow us to make request
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + \
        query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_counts(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[0:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_counts(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times.. you should probably change your password')
        else:
            print(f'{password} was not found. carry on!')
    return


# get passwords as input from input.txt
with open("input.txt", mode="r") as file:
    my_list = file.readlines()
    new_list = []
    for password in my_list:
        new_list.append(password.splitlines())

    final = []
    for i in new_list:
        for j in i:
            final.append(j.split(' '))
    print(final)
    if __name__ == "__main__":
        for i in final:
            main(i)
