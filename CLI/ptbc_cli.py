import argparse
import getpass
import shutil
import time
import os
from pathlib import Path
from core import PetoronTimeBurnCipher

def secure_delete(path):
    if Path(path).exists():
        size = os.path.getsize(path)
        with open(path, 'ba+', buffering=0) as f:
            f.seek(0)
            f.write(os.urandom(size))
        os.remove(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['encrypt', 'decrypt'])
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    parser.add_argument('--ttl', type=int, help='Time to live in seconds')
    parser.add_argument('--autowipe', action='store_true')
    parser.add_argument('--onetime', action='store_true')
    parser.add_argument('--silent', action='store_true')
    args = parser.parse_args()

    password = getpass.getpass("password: ")
    cipher = PetoronTimeBurnCipher(password)

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    data = input_path.read_bytes()

    try:
        if args.mode == 'encrypt':
            if not args.ttl:
                raise ValueError('TTL is required for encryption')
            result = cipher.encrypt(data, args.ttl)
        else:
            result = cipher.decrypt(data)

        output_path.write_bytes(result)

        if args.autowipe:
            secure_delete(input_path)

        if args.onetime and args.mode == 'decrypt':
            Path(f"{output_path}.lock").write_text(str(int(time.time())))

        cipher.destroy()

        if not args.silent:
            print("Done.")

    except Exception as e:
        if not args.silent:
            print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()


