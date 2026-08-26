# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> They are all hash functions because they take a key, such as a word, and turn it into a number. This number can then
> be used as an index in a hash table. The main properties they share are:
> 
> - They take a key as input
> - They return a number as output
> - The same key will produce the same result each time
> - Most use % size so the result fits within the hash table
> - Different keys can sometimes produce the same result. This is called collision.
> 
> The function use different methods to calculate the result. For example, one always returns 1, another adds the ASCII 
> values, the others use Person hashing, Python's built-in hash(), or SHA-256. Some methods spread keys across the 
> table better than others, but they all still convert a key into a hash value.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> Stupidly Simple Hash (SSH)
> - Uniformity: Very poor because every key returns 1.
> - Determinism: Good because it always gives the same result.
> - Efficiency: Very fast because it performs no calculations
> - Collision resistance: Extremely poor because every key collides
> - Sensitivity: None because changing the key does not change the result.
> - Security: None because the result is completely predictable
> 
> Sum of ASCII Values
> - Uniformity: Poor to average because similar words often produce similar totals.
> - Determinism: Good because the same key and table size always gives the same result
> - Efficiency: Good because it only adds the value of each character/
> - Collision resistance: Poor because many keys can have the same total. For example, "abs" and "cab" can produce the 
> the same result
> - Sensitivity: Poor because rearranging the characters does not change the result
> - Security: Poor because the calculation is simple and predicable
> 
> Pearson Hash
> - Uniformity: Good because the shuffled table helps spread results more evently.
> - Determinism: Good, as long as the same Pearson table is used.
> - Efficiency:  Good because it processes each character once and uses simple operations.
> - Collision resistance: Better than adding ASCII values, although collision can still happen
> - Sensitivity: Good because changing or rearranging characters will usually change the result/
> - Security: Poor because pearson hashing is not designed for passwords or other secure information.
> 
> Python Built-in Hash
> - Uniformity: Generally good because Python is designed to distribute values effectively. 
> - Determinism: The same key gives the same result during one program run. However, string hashes may change when the 
> program restarts
> - Efficiency: Very good because it is built into Python and highly optimised
> - Collision resistance: Good for normal hash-table uyse, but collisions are still possible
> - Sensitivity: Good because a small change to the key will usually produce a very different result.
> - Security: It includes protection against some hash-table attacks, but it should not be used for passwords or
> cryptography.
> 
> SHA-256 Hash
> - Uniformity: Very good because its results are spread evenly across its possible output values.
> - Determinism: Good because the same key always produces the same SHA-256 value.
> - Efficiency: Slower than the other functions because it performs more complicated calculations.
> - Collision resistance: Extremely good because finding two inputs with the same full SHA-256 result is extremely 
> - difficult. However, % size creates more collisions when reducing it to a small table index.
> - Sensitivity: Excellent because even a tiny change to the key produces a very different result.
> - Security: Very good for cryptographic hashing, although passwords should use specialised password-hashing 
> functions such as Argon2, bcrypt or scrypt.
> 
> Overall, Python’s built-in hash is the most suitable for an ordinary Python hash table because it is fast and provides
> good distribution. SHA-256 provides the strongest security, while the simple hash and ASCII-sum hash mainly demonstrate
> how hashing works rather than being good practical choices.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> The three most important attributes of a hash function in a hash map are:
> 
> - Uniformity - The hash function should spread keys evently across the hash map. This reduces the number of keys stored
> at the same index and keeps operations fast.
> - Efficiency - The hash function should calculate an index quickly. Hash maps are designed to provide fast insertion,
> searching and deletion, so a slow hash function would reduce their performance
> - Determinism - The same key must produce the same hash value while the hash map is being used, otherwise, the program
> may store a value at one index but search for it at a different index later.
> 
> Collision resistance is also important, but good uniformity already helps reduce collision. Security and sensitivity 
> to small input changes are more important for cryptographic hashing than for normal hash map.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would choose the Pearson hash function. It is efficient because it processes each character once using simple 
> operations, and its shuffled lookup table provides better distribution than the Stupidly Simple Hash or ASCII-sum 
> methods. It is also deterministic when the same lookup table is used, so a player’s UID will consistently produce the 
> same hash value. Pearson hashing reduces collisions and responds well to small changes in a UID without the 
> unnecessary processing cost of SHA-256. Python’s built-in hash is fast, but string hash results can change between 
> program runs, making Pearson hashing more predictable for this implementation.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

>  `import random` imports Python’s random module so the Pearson lookup table can be shuffled.
>
> `random.seed(42)` gives the random generator a fixed starting point. This makes the shuffled table deterministic, 
> meaning it will be created in the same order each time the program runs.
>
> `pearson_table = list(range(256))` creates a list containing every integer from 0 to 255 exactly once. These values 
> fit the range used by the Pearson hash algorithm.
>
> `random.shuffle(pearson_table)` rearranges the lookup-table values. The shuffled table improves uniformity by helping 
> distribute similar keys across different hash values. Because a fixed seed is used, the shuffle remains deterministic.
>
> `def pearson_hash(key: str, size: int) -> int:` defines a function that accepts a string key and the size of the 
> hashmap and returns an integer index.
>
> `hash_ = 0` creates the initial hash value. Every key begins with the same value so the calculation is repeatable.
>
> `for char in key:` processes each character once. This makes the function efficient, with a time complexity of O(n), 
> where n is the number of characters in the key.
>
> `hash_ = pearson_table[hash_ ^ ord(char)]` converts the character to an integer with `ord()`, combines it with the
> current hash using XOR, and uses the result to select a new value from the shuffled table. This makes the hash 
> sensitive to changes in the key and provides better uniformity and collision resistance than simply adding ASCII values.
>
> `return hash_ % size` uses modulo to convert the hash into a valid hashmap index between zero and `size - 1`. 
> Reducing the result means collisions are still possible, particularly when the hashmap is small.
>
> Overall, Pearson hashing is fast, deterministic and provides reasonable distribution for a hashmap. However, it is not
> cryptographically secure and should not be used for passwords or other sensitive information.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> 1. Create a hash map containing ten separate PlayerList objects.
> 2. Receive the player’s UID and name.
> 3. Pass the UID into the Pearson hash function.
> 4. Use the hash value modulo the hashmap size to calculate a bucket index.
> 5. Retrieve the PlayerList stored at that index.
> 6. Search that PlayerList for a node with the same UID.
> 7. If the player already exists, update the existing player’s name.
> 8. Otherwise, create a new Player using the UID and name.
> 9. Place the Player inside a PlayerNode.
> 10. Insert the PlayerNode into the selected PlayerList.
> 11. Increase the hashmap’s player count.
> 12. If different UIDs produce the same index, store their nodes in the same PlayerList as a collision chain.

## Reflection

1. What was the most challenging aspect of this task?

>  The most challenging part was connecting the hash map to my existing PlayerList structure. I had to calculate the 
> correct bucket index, search the linked list for an existing UID, and handle collisions when multiple players used the
> same index. I also had to make sure that updating an existing player did not increase the size and that deleting a 
> player correctly updated both the linked list and the hashmap's player count.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

>  If I did not have to use PlayerList, I would store a normal Python list in each hashmap bucket. Each bucket could 
> contain Player objects directly, so I would not need to create PlayerNode objects or manage next and previous 
> references. This would make the implementation shorter and easier to maintain while still allowing collisions to be 
> handled by storing several players in the same bucket. In a real application, I could also use Python's built-in 
> dictionary because it already provides efficient hashing and collision handling.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
