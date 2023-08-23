import os
import sys


def locate_files(selected_files):
    for file_path in selected_files:
        print(f"Searching for: {file_path}")

        # You can add your own logic here to locate the file
        if os.path.exists(file_path):
            print(f"Found: {file_path}")
        else:
            print(f"Not found: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_locator.py <file1> <file2> ...")
        sys.exit(1)

    selected_files = sys.argv[1:]
    locate_files(selected_files)
