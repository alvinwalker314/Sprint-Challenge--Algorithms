'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, cursor = 0, total = 0):
    if len(word) == 0:
        print("Total: 0")
        return 0
    if cursor == len(word) - 1:
        print(f"Total: {total}")
        return total
    if word[cursor] == "t" and word[cursor + 1] == "h":
        total += 1
    return count_th(word, cursor + 1, total)
    
