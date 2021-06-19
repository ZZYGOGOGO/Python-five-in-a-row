# 五子棋项目说明

## 1.1、概述

​				学习了一个学期的python，掌握了基本的语法和数据结构，了解了python制作小游戏的基本过程。因在本次期末考核内容中，我选择尝试制作一个自己感兴趣的游戏——五子棋。由于时间和能力有限，本次制作仅实现了最基本的功能：双人对战、查看游戏规则、游戏开始与暂停



## 1.2、游戏截图



## 2.1、代码解析

####  2.1.1、导入包

```python
import pygame,time,sys
from pygame.locals import *
```

#### 2.1.2 设置全局变量

```python
Board = []
Role = 2
resultFlag = 0
isRun =0
```

