# ywq

Y W Q's script

## 流程图

```mermaid
graph TB
A[Start]-->B[定义 ez, eo, ef, hf, ho]
B-->C[手动设定 x, 初始 0.325]-->D[0x*1000 写入z_in, o_in, f_in 的IOP]
D-->E[高斯计算]-->F[得到结果 z_out, o_out, f_out]
F-->G[ez=z_out, eo ho=o_out, ef eh=f_out]
G-->H{判断结果是否满足要求}
H-->|满足|I[结束迭代,输出结果]
H-->|不满足|J[继续迭代]-->C
I-->K[End]
```

---

## 待定

- 每次迭代前，都需要手动输入 X ？

- 判断循环终止的条件 ？
- 0x*100000 是什么东西，好奇怪的值
- IOP 的值每次都固定为 iop(3/107=0x*1000000,3/108=0x*100000) 吗？
- 每个输入文件的 IOP 都一样吗？
    - 既然 IOP 是输入文件的内容，按理说每次运算只会改变输出文件，不会改动输入文件，那么输入文件只需设定一次即可，为何要进行循环迭代 ？

---
## 已解决
- x 只需设定一次

---
## 相关文档

![原需求描述](https://github.com/Assiyvril/ywq/raw/main/explanation_of_map.jpg "原需求描述")

![e值实例](https://github.com/Assiyvril/ywq/raw/main/value_of_e.jpg "示例")

![学委的承诺](https://github.com/Assiyvril/ywq/raw/main/dinner.jpg "请客吃饭")


