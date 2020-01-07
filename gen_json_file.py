# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import sys
from mk_pyproject import MakeTemplate

__author__ = 'chengcxy'


USAGE = """
python3 gen_json_file.py 项目名称

"""

def main(project_name):
    obj = MakeTemplate(project_name=project_name)
    obj.run()

if __name__ == '__main__':
    args = sys.argv
    json_file = None
    if len(args) <= 1:
        raise Exception('缺少项目名称')
    project_name = args[-1]
    main(project_name)