# Brute-force-against-one-way-and-collision-free
A program that juxtaposes the difference between breaking the one-way property and collision property

There are 2 functions that run the one-way as well as the collision parts of the program.
Functions are broken down as:
1) random_string() which generates a random string between 1-50 chars (containing both 0-9 and a-z)
2) hash_input() hashes the input with SHA256, encodes it and subscripts it to 24 bits (6 hex)
3) brute_one_way() utilizes your built-in string named 'msg' at the top of the program, pushes it through hash_input and randomly generates random_strings() and hashes them until one of them matches the hash output of your chosen 'msg'
4) brute_collision*() generates 2 random_string()s and hashes them until both of them hash to the same output.
