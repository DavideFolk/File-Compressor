import zipfile
import pathlib


def make_archive(filepaths, dest_folder):
    dest_path = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
