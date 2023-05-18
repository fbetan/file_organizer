import os
from pathlib import Path

dirty_path = input("Path to messy folder: ")

media = {'.jpg', '.png', '.mp3', '.mp4', '.gif', '.mov', '.wav', '.jpeg',
         '.aif', '.cda', '.mpa', '.svg'}

document = {'.docx', '.xlsx', '.pdf', '.txt', '.pptx', '.ppt', '.csv'}

code = {'.py', '.sql', '.cpp', '.ipynb', '.rs', '.rb',
        '.cs', '.json', '.html', '.css', '.sh', '.go'}

system = {'.exe', '.dmg', '.bin'}

new_folder_names = ['media_files', 'document_files', 'code_files', 'system_files']

for new_folder_name in new_folder_names:
    potential_path = os.path.join(dirty_path, new_folder_name)
    existence = os.path.exists(potential_path)
    if not existence:
        os.makedirs(potential_path)
        print(f'New folder: {new_folder_name} created!')


def move_files(path):
    files = (file for file in os.listdir(path))
    for file in files:
        suffix = Path(file).suffix
        if suffix in media:
            os.rename(os.path.join(path, file), (os.path.join(path, 'media_files', file)))
            print(f'{file} moved')
        elif suffix in document:
            os.rename(os.path.join(path, file), (os.path.join(path, 'document_files', file)))
            print(f'{file} moved')
        elif suffix in code:
            os.rename(os.path.join(path, file), (os.path.join(path, 'code_files', file)))
            print(f'{file} moved')
        elif suffix in system:
            os.rename(os.path.join(path, file), (os.path.join(path, 'system_files', file)))
            print(f'{file} moved')
        else:
            continue


if __name__ == "__main__":
    move_files(dirty_path)
    print("This folder is clean.")
