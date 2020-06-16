import os.path

main, py_files, result = [], [], []

for current_dir, dirs, files in os.walk("main"):
    main.append([current_dir.replace('\\', '/'), dirs, files])

for i in main:
    if not i[2]:
        pass
    else:
        for file in i[2]:
            if file[-3:] == '.py':
                if i[0] not in py_files:
                    py_files.append(i[0])

py_files.sort()

for directory in py_files:
    print(directory)
