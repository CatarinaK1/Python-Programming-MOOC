# Write your solution here
def longest(strings: list) -> str:
    
    longest_string = strings[0]

    for i in strings:

        if len(longest_string) < len(i):
            longest_string = i

    return longest_string






if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
