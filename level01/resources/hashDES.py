import crypt

hash_target = "42hDRfypTqqnw"

with open("rockyou.txt", "r", encoding="latin-1") as f:
    for word in f:
        word = word.strip()
        if crypt.crypt(word, hash_target[:2]) == hash_target:
            print("Password trouvé :", word)
            break
