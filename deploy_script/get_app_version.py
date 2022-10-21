import os
from datetime import datetime
import re

debug = 0


def get_app_version(version_first=None):
    current_path = os.path.dirname(os.path.abspath(__file__)).split('\\')
    root_path = '\\'.join(current_path[0: len(current_path) - 1]) + "\\"
    if debug:
        print("tool root app", root_path)
    if debug:
        print("metadata filename", os.path.join(root_path, 'metadata.txt'))
    metadata_file = open(os.path.join(root_path, 'metadata.txt'), 'r')
    lines = metadata_file.readlines()
    metadata_file.close()
    ver_line_num = None
    for num, line in enumerate(lines):
        if re.match('^version\s*=.*$', line) is not None:
            ver_line_num = num
            break
    version, version_build = lines[ver_line_num].strip().split('=')[1].split(' build ')
    version_current_build_date =  datetime.strptime(version_build.split('.')[0], '%Y%m%d')
    version_current_build_num = int(version_build.split('.')[1])
    if debug:
        print("version_current_build_date:", version_current_build_date,
              '\nversion_current_build_num:', version_current_build_num)
    if version_current_build_date.date() == datetime.now().date():
        version_build_num = int(version_current_build_num) + 1
        version_build_date = version_current_build_date
    else:
        version_build_num = 0
        version_build_date = datetime.now().date()
    lines[ver_line_num] = 'version={} build {}.{}\n'.format(version, version_build_date.strftime('%Y%m%d'), version_build_num)
    metadata_file = open(os.path.join(root_path, 'metadata.txt'), 'w')
    for line in lines:
        metadata_file.write(line)
    metadata_file.close()
    if debug:
        print('metadata.txt updated')


if __name__ == "__main__":
    get_app_version()
