import os
folder_path = input("Enter the folder path to scan: ")
print("Scanning folder:", folder_path)
files = os.listdir(folder_path)
print("Files found:", files)
for file in files:
    file_permissions = os.stat(file).st_mode
    print(file, "-", file_permissions)
    print(file, "-", file_permissions)
    for file in files:
        file_permissions = os.stat(file).st_mode
        readable_permissions = oct(file_permissions)[-3:]
        print(file, "-", readable_permissions)
        if readable_permissions[-1] in ["2", "3", "6", "7"]:
            print(file, "is WORLD-WRITABLE - flag this!")
            