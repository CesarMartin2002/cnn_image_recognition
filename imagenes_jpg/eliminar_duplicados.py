import os
from hashlib import sha256

def get_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_object = sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def find_and_remove_duplicate_images(root_folder):
    """Find and remove duplicate JPG images in subfolders."""
    image_hashes = {}

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.jpg'):
                file_path = os.path.join(foldername, filename)
                file_hash = get_file_hash(file_path)

                if file_hash in image_hashes:
                    print(f"Duplicate found: {file_path}")
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting file: {file_path} - {e}")
                else:
                    image_hashes[file_hash] = file_path

if __name__ == "__main__":
    current_directory = os.getcwd()
    find_and_remove_duplicate_images(current_directory)
