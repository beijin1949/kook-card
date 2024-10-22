<img src="https://socialify.git.ci/beijin1949/kook-card/image?description=1&font=Bitter&forks=1&language=1&logo=https%3A%2F%2Fimg.kookapp.cn%2Fassets%2F2024-10%2F12%2FgQFnDlBhTp0ep0j0.png&name=1&pattern=Brick%20Wall&stargazers=1&theme=Auto" alt="kook-card" width="100%" />

## 🎯仓库介绍
1.本库旨在封装一些常用的卡片模板，高度个性化传递参数，实现快速生成kmd卡片

2.现成的消息回复，活跃排行榜，个人信息面板开箱即用

3.灵活定制，支持生成JSON格式KMD，以用于各类场景

### 当前支持的语言
![Static Badge](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=Python&logoColor=white)


基于 [khl.py](https://github.com/TWT233/khl.py) 卡片构建器快速构建，如果你的项目本身在使用khl.py，可以在python文件夹下面直接复制你想要的模板出来单独使用，而不必使用完整的模板库

### 项目目录说明

```plaintext
python/ # python语言代码
├── kcard/ # 项目核心包
│   ├── model/ # 所有模板模块均在此，如果你需要添加新模板请在此添加
│   │   └── base.py # 基础模板，新模板可以在此基础上进行添加
│   └── __init__.py # 初始化文件，添加新的模块后需要在此添加导出
└── setup.py # 安装模块，勿动

test/ # 测试文件示例
├── a_config.py # python程序测试用例
└── py_test.py # 程序模块演示实例
```

### 快速使用
#### Python项目
请先安装模块
```commandline
pip install kcard
```
然后在任意文件中引入模块（当然你也可以选择按需引入，无需全部引入全部模块）
```python
import kcard
```

由于构建器是基于khl.py的卡片构建器构建，如果你没有使用这个SDK，你可以使用 `json.dumps()`来获取json格式的kmd，以用于其他SDK的卡片发送

### 在线文档
https://kookcard.fra1.zeabur.app/

### 在线文档建设

拷贝本项目下document，进入后执行

```commandline
npm install
```

或者你可以使用你喜欢的包管理器进行管理

安装完后运行

```commandline
npm dev
```

进行二次开发，开发后提交pr到本仓库即可！感谢您对开源做出的贡献！