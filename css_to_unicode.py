import sys

ignore_tags = ['code']

css = ""
with open(sys.argv[1],'r') as handle:
	css = handle.read()

print('from sty import fg, bg, ef, rs, RgbFg')
nextwasnewlineprint = False
css_in_lines = css.split('\n')[:-3]
for i,line in enumerate(css_in_lines):
	if 'code' in line:
		continue
	count = 0
	colors_count = len(line.split('color'))
	#print(colors_count)
	
	newline_prints = 0#this should be max 1 to avoid vertical spaces
	while count < colors_count-1:
		index = line.find('color:rgb')+len('color:rgb')
		line = line[index:]
		line_more = line
		rgb = line[0:line.find(';')]
		#print('Rgb:'+rgb)
		character = line[line.find(';')+3:line.find(';')+4]
		#print('Character:'+character)

		print('print(fg'+rgb+ '+\''+character +'\'+'+ 'fg.rs,end="")')
		nextwasnewlineprint = False
		count += 1
		line = line_more
	#print('print(\'\\n\')')
	if not nextwasnewlineprint:
		print('print()')
		nextwasnewlineprint = True
		

	#line = '<span style="color:rgb(139 , 133 , 124);">'
	# while len(line) > 0:
	# 	index = line.find('>')
	# 	if index >= 0:
	# 		line = line[index:]
			
	# 		character = line[0]
	# 		print(character)
		