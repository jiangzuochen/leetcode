# 思路（python）
1. **理清题意**：
> ZigZag转换，可以理解为之字型换换或者N型转换。此处需要将输入字符串按规定行数转换完成后，按行的顺序再连接。
2. **我的思路**
>**分隔思想**：

>观察N型转换结构，可将其分为n个block，然后将每个block的字符先连接，最后将所有block的字符串连接。

3.**借鉴思路**
>构造一个字符串数组strs=['']*min(len(s),numRows).

>遍历字符串s，并使用两个变量curRow和goingDown来控制将s的字符依次写入strs中，最后将strs中的字符串连接。