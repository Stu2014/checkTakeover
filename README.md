# checkTakeover

> 域名接管检测
> 
## 例子
> python checkTakeover.py 1.txt 


## 优点
>没有检测cname，直接访问通过匹配响应包的指纹，判断是否域名过期，存在被接管的可能
>更加适用于甲方了解资产的情况下去检测

## 为什么没有查询cname
> 如果去查cname，部分域名解析到cdn上，导致漏过
![image](https://user-images.githubusercontent.com/50605146/112817568-2ccc5100-90b5-11eb-977c-bdd060fffcb1.png)

## 误报
> 由于通过响应包进行匹配，所以github博客会有误报，自行检查
