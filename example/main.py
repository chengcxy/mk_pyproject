# -*- coding: utf-8 -*-

import sys
from mk_pyproject import MakeTemplate


__author__ = 'chengcxy'

def main(json_file):
    obj = MakeTemplate.from_json_file(json_file=json_file)
    obj.run()

if __name__ == '__main__':
    args = sys.argv
    json_file = None
    if len(args) <= 1:
        raise Exception('缺少项目名称')
    if '--json_file' in args:
        _index = args.index('--json_file') + 1
        json_file = args[_index]
    main(json_file=json_file)