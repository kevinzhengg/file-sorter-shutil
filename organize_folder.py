import os
import shutil

def sort_files(root_directory_path):
    ext_dict = {
        'images & videos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.gif', '.jfif', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webp', '.mp3'],
        'code stuff': ['.py', '.rkt', '.js'],
        'documents': ['.docx', '.doc', '.pptx', '.odt', '.rtf', '.txt'],
        'pdf': ['.pdf'],
        'applications': ['.exe'],
        'other': ['.zip', '.msi', '.xlsx'],
        # More Group if needed
    }

    extension = {ext: group for group, exts in ext_dict.items() for ext in exts}

    print(extension)

    # Create folders for each group
    for group in ext_dict:
        os.makedirs(os.path.join(root_directory_path, group), exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(root_directory_path, topdown=False):
        # Process files
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1].lower()
            if not file_extension or file_extension not in extension:
                continue

            group = extension[file_extension]
            source_path = os.path.join(dirpath, filename)
            destination_path = os.path.join(root_directory_path, group, filename)

            try:
                shutil.move(source_path, destination_path)
            except FileNotFoundError as e:
                print(f"Error moving file {filename}: {e}")

        # Process directories: Remove if empty
        if dirpath != root_directory_path and not os.listdir(dirpath):
            try:
                os.rmdir(dirpath)
            except OSError as e:
                print(f"Error removing directory {dirpath}: {e}")

downloads_path = "../../Downloads"
sort_files(downloads_path)
