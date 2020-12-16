其实就是一个匿名函数,为什么叫lambda?
简单来说，编程中提到的lambda表达式，
通常是需要一个函数，但是又不想费神的去命名一个函数的场合先使用，
也就是匿名函数
map(lambda x:x*x,[y for y in range(10)])

这个写法要好过
def sq(x):
    return x*x
map(sq,[y for y in range(10)])

，因为后者多定义了一个（污染环境的）函数，尤其如果这个函数只会使用一次的话。
而且第一种写法实际上更易读，因为那个映射到列表上的函数具体是要做什么，非常一目了然。
如果你仔细观察自己的代码，会发现这种场景其实很常见：

你在某处就真的只需要一个能做一件事情的函数而已，连它叫什么名字都无关紧要。
Lambda 表达式就可以用来做这件事。
进一步讲，匿名函数本质上就是一个函数，
它所抽象出来的东西是一组运算。这是什么意思呢？类比

a = [1,2,3]
&
f = lambda x: x +1

你会发现，等号右边的东西完全可以脱离等号左边的东西而存在，等号左边的名字只是右边之实体的标识符
，如果你能习惯[1,2,3] 单独存在，那么lambda x:x+1也能单独的存在也不难理解了，它的意义就是给某个数加一
这样一运算本身，

map()   枚举
它可以将一个函数映射到一个可枚举类型上面，沿用上面给出的a和f
map(f,a)
也就是将函数f依次套用在a的没一个元素上面，获得结果[2,3,4],现在用lambda表达式来替换f，
map(lambda x :x +1,[1,2,3])

类比：
a = [1, 2, 3]
r = []
for each in a:
    r.append(each+1)

这样的写法时，
你会发现自己如果能将「遍历列表，给遇到的每个元素都做某种运算」的过程从一个循环里抽象出
来成为一个函数 map，然后用 lambda 表达式将这种运算作为参数传给 map 的话，
考虑事情的思维层级会高出一些来，需要顾及的细节也少了一点。
Python 之中，类似能用到 lambda 表达式的「高级」函数还有 reduce、filter 等等，
很多语言也都有这样的工具（不过这些特性最好不要在 Python 中用太多
，原因详见 http://www.zhihu.com/question/19794855/answer/12987428 的评论部分）
。这种能够接受一个函数作为参数的函数叫做「高阶函数」（higher-order function），
是来自函数式编程（functional programming）的思想。
和其他很多语言相比，Python 的 lambda 限制多多，
最严重的当属它只能由一条表达式组成。这个限制主要是为了防止滥用，
因为当人们发觉 lambda 很方便，就比较容易滥用，可是用多了会让程序看起来不那么清晰，
毕竟每个人对于抽象层级的忍耐 / 理解程度都有所不同。

