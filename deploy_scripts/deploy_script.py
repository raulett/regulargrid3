import os
import re
import shutil
import compile_script
import datetime
import get_app_version

debug = 1
compile_script.compile_files()
qgis_plugins_path = os.environ["QGIS_PLUGINPATH"]

print("QGIS plugin path is: {}".format(qgis_plugins_path))

current_path = os.path.dirname(os.path.abspath(__file__)).split('\\')
deploy_path = os.path.dirname(os.path.abspath(__file__)).split('\\')
deploy_path = '\\'.join(deploy_path[0:len(deploy_path)-2])+'\\deploy'

root_path = '\\'.join(current_path[0: len(current_path)-1])+"\\"
print('Current path: {}\n Deploy path: {}\n Root path: {}\n'.format(current_path, deploy_path, root_path))
# files_to_copy_pattern = r'\.py$|README.MD$|.*\.png$|metadata.txt$'
ignore_pattern = re.compile('deploy_scripts|\\.git\\|.idea|TestScript|.pyc|tests', re.IGNORECASE)
files_to_copy_pattern = re.compile('.py$|README.MD$|.*\.png$|metadata.txt', re.IGNORECASE)


def get_files_to_copy(dir_name):
    files_to_copy_list = []
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            cause = bool(re.search(files_to_copy_pattern, os.path.join(root, name))) and not bool(re.search(ignore_pattern, os.path.join(root, name)))
            if cause:
                files_to_copy_list.append(os.path.join(root, name))
        # files_to_copy_list += [os.path.join(root, name) for name in files if (bool(re.search(files_to_copy_pattern, os.path.join(root, name))) and (bool(re.search(ignore_pattern, os.path.join(root, name)))))]
    print(files_to_copy_list)
    return files_to_copy_list

files_to_copy = get_files_to_copy(root_path)
if debug:
    for file in files_to_copy:
        print(file)

# Очищаем папку с предыдущей версией плагина
if debug:
    print('\n\n ___________________________________\nclear qgis plugin folder')
for root, dirs, files in os.walk(qgis_plugins_path + '\\regulargrid3\\', topdown=False):
    for file in files:
        curpath = os.path.join(root, file)
        os.remove(curpath)
        if debug:
            print(file)


    for d in dirs:
        curpath = os.path.join(root, d)
        if not os.listdir(curpath):
            os.rmdir(curpath)

for file in files_to_copy:
    if debug:
        print(file)
    target_path = file.replace(root_path, qgis_plugins_path + '\\regulargrid3\\')
    if not os.path.exists(os.path.dirname(target_path)):
        os.mkdir(os.path.dirname(target_path))
    shutil.copy(file, target_path)


result_file = open("counter.txt", 'a')
counter = 0
for file in files_to_copy:
    curr_file = open(file, 'rb')
    data = curr_file.read()
    counter += len(data)
    curr_file.close()

result_file.write('{}\t{}\n'.format(datetime.datetime.now().strftime("%d.%m.%YT%H:%M:%S"), counter))
result_file.close()

get_app_version.get_app_version()
