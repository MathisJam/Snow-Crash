import sys


def decryptor():
    try:
        assert len(sys.argv) > 1, "please enter a file to decrypt"
        assert len(sys.argv) == 2, "more than one argument is provided"

        # with : automatically handles setup and cleanup safely, even if errors occur
        # rb : ouvre le fichier en binaire
        with open(sys.argv[1], "rb") as file:
            encrypted_data = file.read()

        # on retire le \n
        encrypted_data = encrypted_data[:-1]

        # chr() : prend un nombre en parametre et renvoie le caractere ASCII correspondant
        # (byte - i) % 256 : modulo pour empeche le resultat de tomber en negatif
        # enumerate() : ft qui ajoute un compteur a un objet iterable, renvoie un objet qui peu etre utilise
        #  pour enumerer les elements d'une sequence et de leur attribuer un index ("ahoh" -> (0-a) (1-h) (2-o) (3-h))
        decrypted_data = "".join(
            chr((byte - i) % 256) for i, byte in enumerate(encrypted_data)
        )
        print(decrypted_data)
        return 0

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1


if __name__ == "__main__":
    decryptor()
