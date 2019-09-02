'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    def counting_th(word, count):
        index = word.find("th")
        # if th is found, add one to count and check the rest of the word if there's more
        if index != -1:
            count += 1 + counting_th(word[index+2:], count)
        return count

    return counting_th(word, 0)
