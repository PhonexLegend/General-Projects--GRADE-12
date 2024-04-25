filename = "star.txt"
file = open(filename, "r")
lines = file.readline()
split = lines.split()
longest_word ="  "

for i in split:
    if len(i) > len(longest_word):
        longest_word = i

print(i)



file.close
