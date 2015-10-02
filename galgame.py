# -*- coding: utf-8 -*-
import requests, re
# 用户名和密码
unpw = {
	'username':'重写青空after',
	'password':'wwwwwwww', # 这不是我密码
	'quickforward':'yes',
	'handlekey':'ls'
}

# 使用session
s = requests.Session()
r = s.post('http://bt.ruc6.edu.cn/b/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', unpw)

# for cookie in r.cookies:
	# print cookie
# f = open('postresult.txt', 'w')
# f.write(r.text.encode('utf-8'))
# f.close()
postername = {}

for i in range(1,12+1): #为什么是12我也不知道（捂脸
	url = "http://bt.ruc6.edu.cn/b/forum-57-" + str(i) + ".html"
	r = s.get(url, cookies=r.cookies)
	
	data = r.text.encode('utf-8')
	links = re.findall(r'\[游戏.+?(?=<\/cite>)', data, re.S) # 先找出游戏名字以及作者，re.S表示是多行匹配
	#print links
	for link in links: 
		
		gamename = re.findall(r'\[游戏.+?(?=<\/a>)', link)[0] #游戏名字
		# 作者名字需要一些操作技巧……是的我的正则表达式用得很烂
		poster = re.findall(r'(?<=<a href="home.php\?mod=space&amp;uid).+?(?=<\/a>)', link)[0].split('>')[1]
		if postername.has_key(poster):
			postername[poster] += 1
		else:
			postername[poster] = 1
		f = open('galgameresult.txt', 'a')	
		f.write(gamename + ' ' + poster)
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
# f = open('result.txt', 'w')
# f.write(r.text.encode('utf-8'))
# f.close()