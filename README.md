# yuque_create

因为语雀API好像失效了(返回405), 录了个playwright脚本勉强能用

需要安装 playwright 库, 使用Python3环境, 有异常可以自己调整代码

```
python -m pip install --upgrade pip
pip install fire
pip install playwright
playwright install
```

用法: 
```
python yuque_create.py [url] [times] [username] [password] [headless]
```

url: 
- 可以是 https://www.yuque.com/kebayi/yuebao 这样的首页
- 也可以是 https://www.yuque.com/kebayi/yuebao/vcm8d0 这样的目录页

times:
- 创建页面数量

username password:
- 用户名 密码

headless
- 无头模式, 设置为1或者True, 可以不显示浏览器

速度较慢, 但是跑1w个页面也应该够用了, 喜欢还是充值吧, 不喜欢就换.

推荐开源项目: https://github.com/outline/outline 自己搭建笔记系统.


## 2022-10-27 更新
- 因为页面改版, 元素位置调整, 所以调整了一下代码, 增加进度显示
- 不过新的会员策略是每个月100篇, 貌似够用了, 整体也有诚意很多, 所以也不用这个脚本了