# yuque_create

因为语雀API好像失效了(返回405), 录了个playwright脚本勉强能用

需要安装 playwright 库, 使用Python3环境, 有异常可以自己调整代码

```
pip install --upgrade pip
pip install playwright
playwright install
```

需要替换脚本中的账号密码

![image](https://user-images.githubusercontent.com/17432059/197738774-1f7fb5af-2bdc-458f-a557-649386f68c6d.png)


用法: 
```
python yuque_create.py [url] [times]
```

url: 
- 可以是 https://www.yuque.com/kebayi/yuebao 这样的首页
- 也可以是 https://www.yuque.com/kebayi/yuebao/vcm8d0 这样的目录页

times:
- 创建页面数量

速度较慢, 但是跑1w个页面也应该够用了, 喜欢还是充值吧, 不喜欢就换.

推荐开源项目: https://github.com/outline/outline 自己搭建笔记系统.
