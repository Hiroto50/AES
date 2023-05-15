import argparse
from classes.AES import AESCipher



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="encyption key")
    parser.add_argument("mode", help="mode to run in: 'encrypt' or 'decrypt'")
    parser.add_argument("text", help="text to encrypt or decrypt")
    args = parser.parse_args()

    cipher = AESCipher(args.key)

    if args.mode == "encrypt":
        encrypted_text = cipher.encrypt(args.text)
        print("Encrypted text:", encrypted_text)
    elif args.mode == "decrypt":
        decrypted_text = cipher.decrypt(args.text)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid mode. Please specify 'encrypt' or 'decrypt'")

if __name__ == "__main__":
    main()