# checkTakeover

> 域名接管检测
> 
## 例子
> python checkTakeover.py 1.txt 


## 优点
>没有检测cname，直接访问通过匹配响应包的指纹，判断是否域名过期，存在被接管的可能

## 误报
> 由于通过响应包进行匹配，所以github博客会有误报，自行检查
