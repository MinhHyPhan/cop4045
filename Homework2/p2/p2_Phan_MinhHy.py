# a) 
number_tuples = [
    (a, b, c, d)
    for a in range(1, 11)
    for b in range(1, 11)
    for c in range(1, 11)
    for d in range(1, 11)
    if a != b and a != c and a != d
    and b != c and b != d and c != d
    and a ** 2 + b ** 2 == c ** 2 + d ** 2
]
print("a)", number_tuples)

# b)
words = ['One', 'SiX','SEVEN', 'three', 'two', 'Ten']
short_words = [
    (word.lower(), len(word))
    for word in words
    if len(word) < 5
]
print("b)", short_words)

# c)
names = ['Albert Meursault Camus', 'Emily Jane Brontë', 'Herman Ishmael Melville']
short_names = [
    name.split()[0] + " " + name.split()[1][0] + ". " + name.split()[2]
    for name in names
]
print("c)", short_names)

# d)
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
anagram_pairs = [
    (w1, w2)
    for w1 in lst1
    for w2 in lst2
    if sorted(w1.lower()) == sorted(w2.lower())
]
print("d)", anagram_pairs)

# e)
s = ['one', 'two', 'three', 'six', 'seven']
word_lengths = {word: len(word) for word in s}
print("e)", word_lengths)

# f)
text = "Sancho, I have conceived an idea most ingenious!"
vowel_positions = {
    i: text[i]
    for i in range(len(text))
    if text[i].lower() in "aeiou"
}
print("f)", vowel_positions)
print("Name: Minh Hy Phan")
print("ID: 23766758")