# 这个AOP一听起来有点懵,同学面阿里的时候就被问懵了…
面向切面编程，通过预编译方式和运行期间动态代理实现在不修改源码的情况下，给程序动态添加
功能的一种技术，，可以理解为动态代理，是spring框架的一个重要内容，
利用 AOP 可以对业务逻辑的各个部分进行隔离，使业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高开发的效率

#装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志
# 性能测试，失误处理等，装饰器是解决这类问题的绝佳设计，

有了装饰器：
我们就可以抽离出大量函数中与函数本身无关的雷同代码并继续使用，
装饰器的作用就是为已经存在的对象添加额外的功能。