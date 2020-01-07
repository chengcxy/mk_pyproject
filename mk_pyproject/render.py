# -*- coding: utf-8 -*-
import argparse
import os
import json
import re
import sys
from string import Template
import traceback

from .exceptions import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TARGET_PARENT_DIR = os.path.join(os.path.dirname(BASE_DIR), 'PythonProjects')
PUBLIC_FOLDERS = ['bin','test','conf','log','docs','examples']
PUBLIC_FILES =  ['README.md','requirements.txt','.gitignore','main.py']
PROJECT_MODULES = ['utils','scheduler','app']

DEFAULT_COMMENTS = {
    'project_desc':'填写项目描述',
    'python_version':'3.5.2',
}




class MakeTemplate(object):
    def __init__(self,
                 project_name=None,
                 template_path=None,
                 targer_parent_dir=None,
                 public_folders=None,
                 public_files = None,
                 project_modules = None,
                 *args,
                 **kwargs):
        self.project_name = project_name
        self.template_path = template_path or DEFAULT_TEMPLATE_PATH
        self.targer_parent_dir = targer_parent_dir or TARGET_PARENT_DIR
        self.public_folders = public_folders or PUBLIC_FOLDERS
        self.public_files = public_files or PUBLIC_FILES
        self.project_modules = project_modules or PROJECT_MODULES
        self.default = {}
        self.default.update(DEFAULT_COMMENTS)
        for k,v in kwargs.items():
            if not hasattr(self,k):
                setattr(self,k,v)
                self.default[k] = v

    @property
    def template_path(self):
        return self._template_path

    @template_path.setter
    def template_path(self,template_path):
        self._template_path = template_path

    @property
    def targer_parent_dir(self):
        return self._targer_parent_dir

    @targer_parent_dir.setter
    def targer_parent_dir(self, targer_parent_dir):
        self._targer_parent_dir = targer_parent_dir

    @property
    def public_folders(self):
        return self._public_folders

    @public_folders.setter
    def public_folders(self, public_folders):
        self._public_folders = public_folders

    @property
    def public_files(self):
        return self._public_files

    @public_files.setter
    def public_files(self, public_files):
        self._public_files = public_files

    @property
    def project_modules(self):
        return self._project_modules

    @project_modules.setter
    def project_modules(self, project_modules):
        self._project_modules = project_modules

    @property
    def targer_dir(self):
        return os.path.join(self.targer_parent_dir, self.project_name)

    @property
    def project_module_dir(self):
        return os.path.join(self.targer_dir, self.project_name.lower())





    def get_template_dict(self):
        files = os.listdir(self.template_path)
        if self.public_files == '*':
            self.public_files = files
        func = lambda x:open(os.path.join(self.template_path,x),'r',encoding='utf-8').read()
        self.template_dict = {file:func(file) for file in files if os.path.isfile(os.path.join(self.template_path,file))}




    def mk_project(self):
        self.mkdir(self.targer_parent_dir)
        self.mkdir(self.targer_dir)
        self.mkdir(self.project_module_dir)
        name = '__init__.py'
        file = os.path.join(self.project_module_dir,name)
        init_contents = ''
        for module in self.project_modules:
            init_contents += 'from .{} import *'.format(module) +'\n'
        self.mk_file(file, options={name: init_contents})

    def mkdir(self,path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def get_other_desc(self):
        _other_desc = ''
        if self.default:
            keys = [k for k in self.default.keys() if k not in DEFAULT_COMMENTS]
            for index,key in enumerate(keys):
                _other_desc += '3.' + str(index+1) + ' ' + str(key) + '=' +  self.default[key]
        return _other_desc

    def get_vars(self,contents):
        _other_desc = self.get_other_desc()
        other_desc_item = {'other_desc':_other_desc}
        locals().update(other_desc_item)
        locals().update(self.default)
        return Template(contents).substitute(**locals())


    def mk_file(self,file,options={}):
        with open(file,'w',encoding='utf-8') as fw:
            if options:
                _contents = options.get(file.split('/')[-1], '')
            else:
                _contents = self.template_dict.get(file.split('/')[-1],'')
            contents = self.get_vars(_contents)
            fw.write(contents)

    def render(self,path,path_type):
        if path_type == 'folder':
            self.mkdir(path)
        else:
            self.mk_file(path)

    @classmethod
    def from_json_file(cls,json_file):
        func = lambda x:json.load(open(x,'r',encoding='utf-8'))
        options = func(json_file)
        return cls.from_settings(options)

    @classmethod
    def from_settings(cls,settings):
        return cls(**settings)


    def write_base_config(self):
        global_config_path = os.path.join(self.targer_parent_dir,'global_config')
        self.mkdir(global_config_path)
        attrs = ["project_name",
                 "template_path",
                 "targer_parent_dir",
                 "public_folders",
                 "public_files",
                 "project_modules"
        ]
        default_options = {attr:getattr(self,attr) for attr in attrs}
        default_options.update(DEFAULT_COMMENTS)
        name = self.project_name + '.json'
        file = os.path.join(global_config_path,name)
        self.mk_file(file,options={name:json.dumps(default_options,ensure_ascii=False)})
        return file



    def run(self):
        if not self.project_name:
            raise ProjectNameEmptyException('项目名称不能为空')
        if not os.path.isdir(self.template_path):
            raise TemplatePathNotExistsException('模板路径{}不存在'.format(self.template_path))
        self.mk_project()
        self.get_template_dict()
        for public_folder in self.public_folders:
            self.render(path=os.path.join(self.targer_dir,public_folder),path_type='folder')
        for public_file in self.public_files:
            self.render(path=os.path.join(self.targer_dir, public_file), path_type='file')
        for project_module in self.project_modules:
            _path = os.path.join(self.project_module_dir, project_module)
            self.render(path=_path, path_type='folder')
            self.render(path=os.path.join(_path,'__init__.py'), path_type='file')
        msg = "{} 项目创建成功~".format(self.targer_dir)
        default_json_file = self.write_base_config()
        msg += '\n 查看配置文件 cat {}'.format(default_json_file)
        print(msg)
        return msg


def make_by_json_file(json_file):
    obj = MakeTemplate.from_json_file(json_file=json_file)
    obj.run()

def make_by_settings(settings):
    obj = MakeTemplate.from_settings(settings)
    obj.run()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_file", help="json_file 文件")
    parser.add_argument("--project_name", help="项目名称")
    parser.add_argument("--template_path", help="模板目录")
    parser.add_argument("--targer_parent_dir", help="python总项目目录")
    parser.add_argument("--public_folders", help="python子项目目录")
    parser.add_argument("--project_modules", help="模板文件列表")
    args = parser.parse_args()
    json_file = args.json_file
    if json_file:
        make_by_json_file(json_file)
    else:
        settings = {attr:value for attr,value in args._get_kwargs() if attr != 'json_file'}
        make_by_settings(settings)

if __name__ == '__main__':
    main()



