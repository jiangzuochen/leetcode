# 思路（python）
1. **理清题意**：
> 输入字符串包含了电话机按键2-9中的数字，每个数字对应着电话按键上的字母中的一个，题目要求根据输入字符串，把对应的所有字母组合输出。例如：输入:'2'，输出则为['a','b','c'],输入'23',则输出为["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

2.**解决思路**
> 此题属于典型的递归问题，即从总combinations依次分解为combination+digit的形式，而每一个combination又可分解，直至分解到第一个digit。

>构造递归函数为：def combinationTwo(self,l,digit)。其中l为上一级combination的输出。

>假设第一个digit为'2'，查询字典，构造第一级combination=['a','b','c']