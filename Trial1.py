import hashlib
import random
from random import randint

chars = '0123456789abcdefghijklmnopqrstuvwxyz'  # all possible characters
msg = 'Me gusta el helado'

def random_string():  # generate a random string of random length up to 50
    randomLength = randint(1, 50)
    randomString = ''.join(random.choice(chars) for i in range(randomLength))
    return randomString   
 
def hash_input(user_input):  # hashing function, encoding, and subscripting
    hashed_input = hashlib.sha256(user_input.encode())
    hashed_input = hashed_input.hexdigest()  # hashing function that encodes into printable as well as subscripting
    hashed_input = hashed_input[:6]  # this is 24 bits
    return hashed_input

def brute_one_way(message):
    hashed_message = hashlib.sha256(message.encode())  # first hashing the given input string
    hashed_message = hashed_message.hexdigest()[:6]
    print('Message is :', msg)
    print('The hashed input reduced to 24 bits is: ', hashed_message)  # printing that string and its hash value
    
    done = False
    loops = 0
    while (done == False):  # finding a random generated string that hashes to the same hash value as the given input
        loops = loops + 1
        randString = random_string()
        randHashedString = hash_input(randString)
        if (randHashedString == hashed_message):  # if so, print
            print('Brute forcing one-way property completed:')
            print('Found a match!', randString, ' also hashes to ', randHashedString)
            print('# of iterations: ', loops)
            return None
    
def brute_collision():  # brute collision here uses 2 randomly generated strings and compares their hash values
    done = False
    loops = 0
    while (done == False):
        loops = loops + 1
        randomFirst = random_string()
        randomSecond = random_string()
        randomFirstHashed = hash_input(randomFirst)
        randomSecondHashed = hash_input(randomSecond)
        if (randomFirstHashed == randomSecondHashed and randomFirst != randomSecond):
            print('Brute forcing collision-free property completed:')
            print('Found a match!')
            print('# of iterations: ', loops)
            print(randomFirst, 'and ', randomSecond, ' both hash to ', randomFirstHashed, '!')
            return None
    

brute_one_way(msg)
brute_collision()

    
    
