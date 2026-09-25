import argparse
from pathlib import Path
import shutil

def create_file_name(dest_dir , file):
    counter = 1
    name = file.name
    while True :
        if (dest_dir/name).exists():
            name = f"{file.stem}_{counter}{file.suffix}"
            counter += 1
        else:
            break
    return name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path' , type=Path , default= Path.home() / "Downloads" )
    parser.add_argument('-r' , '--recursive' , action='store_true' , help ='Also organise the files in the sub-folder')
    parser.add_argument('-t' , '--test' ,action='store_true' ,help ='A test so you can see what happen without moving anything')
    args = parser.parse_args()

    path = args.path

    extension_map = {
    ".png": "Images", ".jpg": "Images", ".jpeg": "Images", ".gif": "Images",
    ".bmp": "Images", ".svg": "Images", ".webp": "Images",

    ".pdf": "Documents", ".txt": "Documents", ".docx": "Documents",
    ".doc": "Documents", ".odt": "Documents", ".rtf": "Documents", ".md": "Documents",

    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos", ".avi": "Videos",

    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".aac": "Audio", ".m4a": "Audio",

    ".zip": "Archives", ".tar": "Archives", ".gz": "Archives", ".rar": "Archives", ".7z": "Archives",

    ".py": "Code", ".cpp": "Code", ".c": "Code", ".java": "Code",
    ".js": "Code", ".html": "Code", ".css": "Code", ".json": "Code",

    ".exe": "Installers", ".msi": "Installers", ".apk": "Installers", ".dmg": "Installers",
}

    folder_names = set(extension_map.values()) | {"Others"}
    if not path.exists():
        print("The path that you entered is not found !")
        return
    elif not path.is_dir():
        print("The path that you entered needs to be a directory !")
        return
    else:
        if not args.test:
            for folder in folder_names:
                (path / folder).mkdir(parents=True , exist_ok=True)


    file_path = path.rglob("*") if args.recursive else path.iterdir()

    for file in list(file_path):
        if file.is_file():
            if file.relative_to(path).parts[0] in folder_names:
                continue
            try:
                destination  = extension_map.get(file.suffix.lower() ,"Others")
                new_name = create_file_name(path / destination , file)
                if args.test:
                    print(f"Moving {file} to {path / destination / new_name} ")
                else:
                    shutil.move(file ,(path / destination / new_name))

            except PermissionError:
                print(f"You don't have the permission to move {file.name}")
            except OSError as er:
                print(f"Couldn't move {file.name} : {er}")

if __name__ =="__main__":
    main()