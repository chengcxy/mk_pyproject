# 一.项目模板生成工具

1. 所有Python开发项目统一放到指定目录 比如(我的都放在这个目录 /Users/chengxinyao/DataWarehouse/PythonProjects 使用该工具时候 json_file里targer_parent_dir参数保持一致)
2. 每个项目最好用统一的模板生成，防止各个项目都是不同的风格，维护起来心累
3. 通过该工具可快速启动新项目 通过配置文件生成项目开发文档README.md等

# 二.目录结构实例,可通过配置文件定义,比如创建的logstreaming项目

```
├── README.md 项目文档
├── bin       shell脚本
├── conf      项目配置文件
├── docs      项目里一些doc文件
├── examples  样例
├── log       日志目录
├── logstreaming
│   ├── __init__.py
│   ├── 模块A
│   │   └── __init__.py
│   ├── 模块B
│   │   └── __init__.py
│   └── 模块C
│       └── __init__.py
├── main.py   入口main函数
├── requiirements.txt 依赖包
└── test      测试脚本
```

# 三.安装使用

```
git clone git@github.com:chengcxy/mk_pyproject.git
cp mk_pyproject/templates/* 你的模板路径(使用该工具时候 json_file里template_path参数保持一致)
执行下面命令 可创建一个Bpoint项目的json_file
python3 gen_json_file.py Bpoint
下面是输出信息:
/Users/chengxinyao/DataWarehouse/PythonProjects/Bpoint 项目创建成功~
查看配置文件 cat /Users/chengxinyao/DataWarehouse/PythonProjects/global_config/Bpoint.json
```

# 四.配置文件内容

```
{
  "project_name": "logstreaming",
  "template_path": "/Users/chengxinyao/DataWarehouse/mk_pyproject/templates",
  "targer_parent_dir": "/Users/chengxinyao/DataWarehouse/PythonProjects",
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
  "project_modules": [
    "utils",
    "scheduler",
    "app"
  ],
  "project_desc": "填写项目描述",
  "python_version": "3.5.2"
}
```

# 五.配置文件参数

|参数|参数注释
|---|---
|project_name|项目名称
|template_path|模板全路径
|targer_parent_dir|所有python项目的父目录
|public_folders|项目的公共目录列表 配置文件里自自定即可 会自动再项目目录里创建
|public_files|模板全路径下的公共文件 README.md/requirements.txt/启动脚本main.py等 会自动再项目目录里创建
|project_modules|项目的模块列表 可自定义
|project_desc|项目描述 填写后会自动渲染到README.md
|python_version|python版本信息 填写后会自动渲染到README.md
|其他参数|其他信息 填写后会自动渲染到README.md >三.其他信息下


# 六.将该工具安装为命令行工具 以后可通过复制配置文件 创建项目

```
(1)源码安装:
git clone git@github.com:chengcxy/mk_pyproject.git
cd 目录/mk_pyproject/bin
sh build.sh
此时 已将mk_pyproject模块添加到python 系统模块包路径下
(2)pip install mk-pyproject==0.0.1
将第三步生成的Bpoint.json 通过命令行工具生成
mk_pyproject --json_file ~/DataWarehouse/PythonProjects/global_config/Bpoint.json
```

# 七.注意事项

```
如果已经创建过项目 进入开发流程 请勿重复执行创建项目命令 会覆盖
```

