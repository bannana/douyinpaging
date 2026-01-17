<p align="center">
   <img width="300" height="auto" src="https://ghproxy.com/https://raw.githubusercontent.com/cniu6/douyinpaging/main/png/%E7%BF%BB%E9%A1%B5%E7%AC%94%E6%8A%96%E9%9F%B3ico.png?raw=true">
 </p>


# 翻页笔抖音
 douyinpaging


 
抖音翻页笔抖音 - 使用翻页笔上下模拟键盘上下键滑动抖音短视频、快手、TIKTOK、SHOUTS、基本通用。

## 功能

- [x] 上下滑动刷视频
- [x] 长按下键快速关闭当前页，并退出程序
- [x] 长按上键打开或关闭全屏

## 基于Python编写
打包命令

```shell script
Pyinstaller -F -i douyinfanyebiRes.ico main.py
```

## 原理

翻页笔对电脑输入page_up/page_done键
- 翻页笔(page_up)    =>   程序模拟(up)
- 翻页笔(page_down)  =>   程序模拟(down)
- 翻页笔长按下键(B)   =>   程序模拟(cmd+q)
- 翻页笔长按上键(shift+q或esc)   =>   程序模拟(h)或esc不变

让程序自动监听 并且自动模拟输入 up/done键
从而用翻页笔也能滑动视频。

翻页笔长按下键，一般绑定`<B>`键，使PPT黑屏，让注意力转移到讲师上来。
那就让`<B>`绑定 输入 Alt+F3快速关闭网页。


## 使用到的项目

* python
* pypnut
* time 我的
