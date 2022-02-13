"""
pip一次性安装很多库

1、问题描述：有时候我们想要安装许多python库来进行work，但一条条安装过于麻烦，所以想一次性安装所需的所有库。

2、问题解决：首先将自己所需的库放在一个requirement.txt文件中，然后通过参数-r来安装文件里所列出的所有库。示例如下：

pip install -r requirement.txt

1、   如果安装的比较慢，可以换安装源，需要参数-i，示例如下：

    pip install -i https://pypi.douban.com/simple -r requirement.txt
        or
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
        or
    pip install -i https://mirrors.aliyun.com/pypi/simple -r requirement.txt

"""