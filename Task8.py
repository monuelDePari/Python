import os
import hashlib


blockSize = 512



def calculate_md5hash(path, blockSize):

    try:

        with open(path, 'rb') as file:

            md5_hash = hashlib.md5()

            chunk = file.read(blockSize)

            while chunk:

                md5_hash.update(chunk)

                chunk = file.read(blockSize)

                return md5_hash.hexdigest()

    except PermissionError as e:

        return e



def get_duplicates(parent_dir):

    hashes = {}

    for root, directories, files in os.walk(parent_dir):

        for name in files:

            path = os.path.join(root, name)

            filehash = calculate_md5hash(path, blockSize)

            hashes[path] = filehash

    duplicate_files = []

    for k, v in hashes.items():

        if list(hashes.values()).count(v) > 1:

            duplicate_files.append(k)

    return duplicate_files





if __name__ == "__main__":

    folder_path = input("path to your folder: ")

    print(get_duplicates(folder_path))