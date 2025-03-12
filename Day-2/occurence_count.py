def count_occurence(string):
    word_counts = {}
    for char in string:
        if char in word_counts.keys():
            word_counts[char] += 1
        else:
            word_counts[char] = 1
    return word_counts

string = input()
print(count_occurence(string))