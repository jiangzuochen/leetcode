# 思路(Python)
1. 利用Python的Set结构不重复的特性，得到Unique Email的数量。

2. 图方便使用了列表生成式，如果要追求执行效率，利用for循环结构并且单独判断每个原始地址是否含有'@'字符，能够提升一些执行速度。