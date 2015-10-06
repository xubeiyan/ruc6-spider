# -*- coding: utf-8 -*-
import requests, re
f = open("galgameresult.txt", 'w')
f.write('\r\n')
f.close()
# 用户名和密码
unpw = {
	'username':'重写青空after',
	'password':'123456789',
	'quickforward':'yes',
	'handlekey':'ls'
}

# 使用session
s = requests.Session()
r = s.post('http://bt.ruc6.edu.cn/b/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', unpw)

postername = {}

for i in range(1,12+1): #为什么是12我也不知道（捂脸
	url = "http://bt.ruc6.edu.cn/b/forum-57-" + str(i) + ".html"
	r = s.get(url, cookies=r.cookies)
	
	data = r.text.encode('utf-8')
	links = re.findall(r' <a href="thread.+?class="xst".+?(?=<\/cite>)', data, re.S) # 先找出游戏名字, 链接以及作者，re.S表示是多行匹配
	#print links
	for link in links: 
		if not re.findall(r'\[游戏', link): #不是游戏就跳过
			print link
			continue
		url = re.findall(r'(?<=<a href=").+?(?=")', link)[0] #链接
		gamename = re.findall(r'\[游戏.+?(?=<\/a>)', link)[0] #游戏名字
		# 作者名字需要一些操作技巧……是的我的正则表达式用得很烂
		poster = re.findall(r'(?<=<a href="home.php\?mod=space&amp;uid).+?(?=<\/a>)', link)[0].split('>')[1]
		if postername.has_key(poster): #统计发种次数的
			postername[poster] += 1
		else:
			postername[poster] = 1
		f = open('galgameresult.txt', 'a')	
		f.write('[url=' + url + ']' + gamename + '[/url]') #bbcode的链接是[url=xxxxx]aaaa[/url]
		f.write("\n") #write函数只会会加上\r，所以还得手动添加\n(in Windows)
		f.close()
		
f = open('galgameresult.txt', 'a')
f.write("\n发种次数统计:\n")
total = 0
for key in postername:
	total += postername[key]
	f.write(key + ":" + str(postername[key]))
	f.write("\n")
f.write("total:" + str(total))
f.close()
# 最后的galgame.txt应该是这样的结果
# ...
# [url=thread-197272-1-1.html][游戏][Free Friends 2][WRP汉化组][フリフレ2][PC][RAR][/url]
# [url=thread-196624-1-1.html][游戏][塔の下のエクセルキトゥス][日文原版][PC][ISO][/url]
# [url=thread-196621-1-1.html][游戏][天気雨][日文原版][PC][ISO][/url]
# [url=thread-196619-1-1.html][游戏][妹のセイイキ][日文原版][PC][ISO][/url]
# [url=thread-196618-1-1.html][游戏][NOBLE☆WORKS][私立秀峰学院汉化组][PC][ISO][/url]
# [url=thread-194372-1-1.html][游戏][紅い瞳に映るセカイ ず~っと真紅といっしょ][日文原版][PC][ISO][/url]
# [url=thread-194141-1-1.html][游戏][HOLY BREAKER][ATF汉化组][PC][ISO][/url]
# ...
# 发种次数统计:
# 重写青空after:18
# 水萤灯:1
# 神的茄子:2
# 大地无敌:1
# miemie0:1
# 哀伤喵:1
# 二阶堂真红:9
# greatgary:1
# nicisha:8
# 三年目:1
# tichaosius:2
# boring痕:2
# xiangyizhe:2
# 三途河的天空:1
# 逆流半影:12
# qratosone:1
# 命运玩人:1
# seraph1992:1
# rick1995:1
# loveSasuke:1
# z85778148:2
# PhilosophyZ:72
# 风异样的南至:1
# daizyply:1
# koneats:91
# enternal:5
# total:239