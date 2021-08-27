# 单例模式
## 意图
**单例模式**是一种创建型设计模式， 让你能够保证一个类只有一个实例， 并提供一个访问该实例的全局节点。
![](https://refactoringguru.cn/images/patterns/content/singleton/singleton.png?id=108a0b9b5ea5c4426e0a)

## 问题
单例模式同时解决了两个问题， 所以违反了**单一职责原则**：
1. **保证一个类只有一个实例**。 为什么会有人想要控制一个类所拥有的实例数量？ 最常见的原因是控制某些共享资源 （例如数据库或文件） 的访问权限。

    它的运作方式是这样的： 如果你创建了一个对象， 同时过一会儿后你决定再创建一个新对象， 此时你会获得之前已创建的对象， 而不是一个新对象。
    
    注意， 普通构造函数无法实现上述行为， 因为构造函数的设计决定了它必须总是返回一个新对象。
    ![](https://refactoringguru.cn/images/patterns/content/singleton/singleton-comic-1-zh.png?id=70da542e5e19f0df3dfc)
    
    客户端甚至可能没有意识到它们一直都在使用同一个对象。
    
2. **为该实例提供一个全局访问节点**。 还记得用过的那些存储重要对象的全局变量吗？ 它们在使用上十分方便， 但同时也非常不安全， 因为任何代码都有可能覆盖掉那些变量的内容， 从而引发程序崩溃。

    和全局变量一样， 单例模式也允许在程序的任何地方访问特定对象。 但是它可以保护该实例不被其他代码覆盖。

    还有一点： 你不会希望解决同一个问题的代码分散在程序各处的。 因此更好的方式是将其放在同一个类中， 特别是当其他代码已经依赖这个类时更应该如此。
    


## 解决方案
所有单例的实现都包含以下两个相同的步骤：
- 将默认构造函数设为私有， 防止其他对象使用单例类的 `new`运算符。

- 新建一个静态构建方法作为构造函数。 该函数会 “偷偷” 调用私有构造函数来创建对象， 并将其保存在一个静态成员变量中。 此后所有对于该函数的调用都将返回这一缓存对象。

如果你的代码能够访问单例类， 那它就能调用单例类的静态方法。 无论何时调用该方法， 它总是会返回相同的对象。

## 单例模式结构
![](https://refactoringguru.cn/images/patterns/diagrams/singleton/structure-zh.png?id=207b153c1abb131ee4eb)

单例 （Singleton） 类声明了一个名为 `getInstance` `获取实例`的静态方法来返回其所属类的一个相同实例。

单例的构造函数必须对客户端 （Client） 代码隐藏。 调用 `获取实例` 方法必须是获取单例对象的唯一方式。

## 单例模式适合应用场景
- 如果程序中的某个类对于所有客户端只有一个可用的实例， 可以使用单例模式。

    单例模式禁止通过除特殊构建方法以外的任何方式来创建自身类的对象。 该方法可以创建一个新对象， 但如果该对象已经被创建， 则返回已有的对象。

- 如果你需要更加严格地控制全局变量， 可以使用单例模式。

    单例模式与全局变量不同， 它保证类只存在一个实例。 除了单例类自己以外， 无法通过任何方式替换缓存的实例。
    
请注意， 你可以随时调整限制并设定生成单例实例的数量， 只需修改 `获取实例`方法， 即 `getInstance` 中的代码即可实现。

比如： 数据库连接（数据库连接池对象和配置对象），Socket 创建连接，项目中的日志操作 ==> 信息一致，避免重复创建对象造成的时间和空间上的开销，也避免了对资源的多重占用

## 实现方式
1. 在类中添加一个私有静态成员变量用于保存单例实例。

2. 声明一个公有静态构建方法用于获取单例实例。

3. 在静态方法中实现"延迟初始化"。 该方法会在首次被调用时创建一个新对象， 并将其存储在静态成员变量中。 此后该方法每次被调用时都返回该实例。

4. 将类的构造函数设为私有。 类的静态方法仍能调用构造函数， 但是其他对象不能调用。

5. 检查客户端代码， 将对单例的构造函数的调用替换为对其静态构建方法的调用。

## 单例模式优缺点
### 优点
- 你可以保证一个类只有一个实例。

- 你获得了一个指向该实例的全局访问节点。

- 仅在首次请求单例对象时对其进行初始化。

### 缺点
-  违反了**单一职责原则**。 该模式同时解决了两个问题。

- 单例模式可能掩盖不良设计， 比如程序各组件之间相互了解过多等。

- 该模式在多线程环境下需要进行特殊处理， 避免多个线程多次创建单例对象。

- 单例的客户端代码单元测试可能会比较困难， 因为许多测试框架以基于继承的方式创建模拟对象。 由于单例类的构造函数是私有的， 而且绝大部分语言无法重写静态方法， 所以你需要想出仔细考虑模拟单例的方法。 要么干脆不编写测试代码， 或者不使用单例模式。

## 与其他模式的关系
- 外观模式类通常可以转换为单例模式类， 因为在大部分情况下一个外观对象就足够了。

- 如果你能将对象的所有共享状态简化为一个享元对象， 那么享元模式就和单例类似了。 但这两个模式有两个根本性的不同。

    1. 只会有一个单例实体， 但是享元类可以有多个实体， 各实体的内在状态也可以不同。
    2. 单例对象可以是可变的。 享元对象是不可变的。

- 抽象工厂模式、 生成器模式和原型模式都可以用单例来实现。

### 与单例模式功能相似的概念
- 全局变量

    全局变量可能会有名称空间的干扰，如果有重名的可能会被覆盖
    
- 静态变量（方法）



## Python 实现单例模式的几种方式
### 1. 使用模块

**Python 的模块就是天然的单例模式**，因为模块在第一次导入时，会生成 `.pyc` 文件，当第二次导入时，就会直接加载 `.pyc` 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：

mysingleton.py
```
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
```
将上面的代码保存在文件 `mysingleton.py` 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
```
from mysingleton import Singleton
```

### 2. 使用装饰器
```
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(id(a1) == id(a2))
# True
```

另一种实现方式

```
from functools import wraps


def singleton(cls):
    _instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper
```
在写装饰器的时候，带装饰功能的函数（上面代码中的 `wrapper` 函数）通常都会用 `functolls` 模块中的 `wraps` 再加以修饰，这个装饰器最重要的作用是给被装饰的类或者函数动态添加一个 `__wrapped__` 属性，这个属性会被装饰器之前的类或函数保留下来，这样在我们不需要装饰功能的时候，可以通过它来取消装饰器，例如可以 `class_name = class_name.__wrapped__` 来取消对 `class_name` 类做的单例处理。

需要注意的是：上面的单例并不是**线程安全的**，如果要做到线程安全，需要对创建对象的代码进行加锁处理。

### 3. 使用类
```
class Singleton(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
```
上面的代码在使用多线程时会存在问题
```
import time
import threading


class Singleton(object):
    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```

执行结果如下

```
<__main__.Singleton object at 0x00000261A1F29A30>
<__main__.Singleton object at 0x00000261A1F2DF10>
<__main__.Singleton object at 0x00000261A1F2D730>
<__main__.Singleton object at 0x00000261A1F29910>
<__main__.Singleton object at 0x00000261A1F2D1F0>
<__main__.Singleton object at 0x00000261A1F521F0>
<__main__.Singleton object at 0x00000261A1F29CA0>
<__main__.Singleton object at 0x00000261A1F2D490>
<__main__.Singleton object at 0x00000261A1F2DC70>
<__main__.Singleton object at 0x00000261A1F2D9D0>
```
解决办法，**加锁**，未加锁的部分并发执行，加锁部分串行执行，速度降低，但是保证了数据安全

```
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)
```

执行结果如下：

```
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
<__main__.Singleton object at 0x000001B9D7029A90>
```

这种方式实现的单例模式，使用时会有限制，以后实例化必须通过 `obj = Singleton.instance()`

如果用 `obj=Singleton()` ,这种方式得到的不是单例

### 4. 基于__new__方法实现（推荐使用，方便）
我们知道，当我们实例化一个对象时，是先执行了类的`__new__` 方法（我们没写时，默认调用`object.__new__` ），实例化对象；然后再执行类的`__init__` 方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
```
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```

采用这种方式的单例模式，以后实例化对象时，和平时实例化对象的方法一样 `obj = Singleton()`
执行结果如下：

```
<__main__.Singleton object at 0x0000020FE3A51BE0> <__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
<__main__.Singleton object at 0x0000020FE3A51BE0>
```

### 5. 基于 metaclass 方式实现
```
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name
```


---
参考
> [REFACTORING GURU](https://refactoringguru.cn/design-patterns/singleton)
>
> [Python中的单例模式的几种实现方式的及优化](https://www.cnblogs.com/huchong/p/8244279.html)
>
> [单例模式的四种方式](https://www.cnblogs.com/huchong/p/8522939.html)