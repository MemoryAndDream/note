基于python2 selenium的验证码识别脚本
运行seleniumTest.py测试，测试前需要关闭开启的chrome
默认chrome.exe在桌面上(默认安装)

使用了联众的人工打码服务
#windows下必须用unicode

同一配置文件不能运行2个chrome实例

#如截图之类的命令 google-chrome --headless --disable-gpu --user-data-dir=/home/gfeng/.config/google-chrome/ --print-to-pdf="zzzz.pdf" https://mail.google.com/mail/u/0/#inbox


 selenium grid 分布式测试


Chrome每开一个新标签页面,都会在系统进程里加入一个Chrome.exe进程



开页面的情况默认会访问谷歌首页，这样会出错！


https://www.ghacks.net/2013/10/06/list-useful-google-chrome-command-line-switches/