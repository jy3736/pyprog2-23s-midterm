import os
import shutil
import re, sys

if len(sys.argv) < 2:
    SOURCE_DIR = "tests"
else:
    SOURCE_DIR = sys.argv[1]

BACKUP_DIR = f"{SOURCE_DIR}_backup"
BYTECODE_DIR = f"{SOURCE_DIR}/__pycache__"

# Create backup directory if it does not exist
if not os.path.isdir(BACKUP_DIR):
    os.mkdir(BACKUP_DIR)

# Compile all python scripts in source directory
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".py"):
            py_file = os.path.join(root, file)
            os.system(f"python -m py_compile {py_file}")

# Copy all python scripts to backup directory
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".py"):
            py_file = os.path.join(root, file)
            shutil.move(py_file, BACKUP_DIR)

# Copy all compiled bytecode scripts to source directory
for root, dirs, files in os.walk(BYTECODE_DIR):
    for file in files:
        if file.endswith(".pyc"):
            pyc_file = os.path.join(root, file)
            shutil.copy2(pyc_file, SOURCE_DIR)

# Rename compiled bytecode scripts using regular expression
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".pyc"):
            pyc_file = os.path.join(root, file)
            new_file = re.sub(r"\.cpython-\d+", "", file)
            new_file = os.path.join(root, new_file)
            print(f"Renaming {pyc_file} to {new_file}")
            os.rename(pyc_file, new_file)
