# pyquery_xpath
## 一个继承于 [pyquery](https://github.com/gawel/pyquery) 的python库

### 起因
- 它没有重写任何 pyquery 的方法，我非常喜欢这个库，认为它在操作 html 方面的各种方法非常简洁
- 但我习惯于使用 xpath 选择器，pyquery 仅支持 css 选择器和部分伪类选择器
- 在选择包含某些文本的节点时，总是会选择符合条件的最外层节点
- 看了 pyquery 部分代码，发现它基于 lxml.etree 模块实现了 html 路径选择，也就是说它原生支持 xpath 选择器，但却没有实现相应的方法，让我很奇怪（也可能很少有像我这样喜欢混搭的人）
- 于是我为它添加了一个 xpath 方法，仅此而已

### 使用方式
```
>>> h = '<a class="foo1"><span class="foo2"><span class="foo3">Hello</span></span></a>'
>>> d = PyQuery(h)
>>> d('a').xpath('.//span[@class="foo2"]')
[<span.foo2>]
>>> d.xpath('//span[@class="foo2"]')('.foo3')
[<span.foo3>]
>>> d.xpath('.//span[@class="foo2"]')('.foo1')
[]
```


