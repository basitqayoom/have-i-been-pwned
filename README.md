# have-i-been-pwned
Check if your password is in a data breach



request_api_data function (called from pwned_api_check function) takes first fives hash keys of the password and returns the data (hashes with same first five keys)

get_password_leaks compares the remaining keys of hashes with the data returned from request_api_data function and returns the count of it

pwned_api_check function (called from main function) takes each password as an argument, it creates the hash(sha1) of the password 

main function takes arguments as list of passwords


