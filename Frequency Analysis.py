
encrypted = input("Enter the encrypted plaintext: ")

encrypted1 = encrypted.lower()

letters = []

for letter in encrypted1:
    count = encrypted1.count(letter)
    if letters.count(letter) == 0:
        print(letter + ' - ' + str(count))
    letters.append(letter)
