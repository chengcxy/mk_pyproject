# -*- coding: utf-8 -*-
from mk_pyproject import MakeTemplate


def make_by_json_file(json_file):
    """
    create project by json_file

    json_file content like
    ```
    {
      "project_name": "your projectName",
      "template_path": "your template_path like /Users/chengxinyao/DataWarehouse/mkproj/templates",
      "targer_parent_dir": "your PythonProjects Path like /Users/chengxinyao/DataWarehouse/PythonProjects",
      "public_folders": [
        "bin",
        "test",
        "conf",
        "log",
        "docs",
        "examples"
      ],
      "public_files": [
        "README.md",
        "requirements.txt",
        ".gitignore",
        "main.py"
      ],
      "project_folders": [
        "utils",
        "scheduler"
      ]
    }

    ```
    """

    obj = MakeTemplate.from_json_file(json_file)
    obj.run()

def make_by_settings(settings):
    """
    create project by settings

    settings like
    ```
    {
      "project_name": "your projectName",
      "template_path": "your template_path like /Users/chengxinyao/DataWarehouse/mkproj/templates",
      "targer_parent_dir": "your PythonProjects Path like /Users/chengxinyao/DataWarehouse/PythonProjects",
      "public_folders": [
        "bin",
        "test",
        "conf",
        "log",
        "docs",
        "examples"
      ],
      "public_files": [
        "README.md",
        "requirements.txt",
        ".gitignore",
        "main.py"
      ],
      "project_folders": [
        "utils",
        "scheduler"
      ]
    }

    ```
    """

    obj = MakeTemplate.from_settings(settings)
    obj.run()


if __name__ == '__main__':
    json_file = 'your json file'
    make_by_json_file(json_file)
    #settings = {} #not be empty
    #make_by_settings(settings)