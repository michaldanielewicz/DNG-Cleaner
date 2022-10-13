import os
from os.path import isfile
import logging


def get_files_with_extension(files: tuple[str], extension: str) -> set:
    files_tuple = ((f.split(".")[0], f.split(".")[1]) for f in files)
    return {f[0] for f in filter(lambda f: f[1] == extension, files_tuple)}


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    all_files = [f for f in os.listdir() if isfile(f)]
    dng_files = get_files_with_extension(all_files, "DNG")
    jpg_files = get_files_with_extension(all_files, "JPG")

    # Get DNG files to remove
    files_to_delete = dng_files.difference(jpg_files)

    logging.info(f" All files: {len(all_files)}")
    logging.info(f" DNG files: {len(dng_files)}")
    logging.info(f" JPG files: {len(jpg_files)}")
    logging.info(f" Files to delete: {len(files_to_delete)}")

    # Delete DNG files
    deleted_count = 0
    for f in all_files:
        if f.split(".")[0] in files_to_delete:
            try:
                os.remove(f)
                deleted_count += 1
            except FileNotFoundError:
                logging.error(f"File {file} not found")

    logging.info(f" Files removed: {deleted_count}")


if __name__ == "__main__":
    main()
