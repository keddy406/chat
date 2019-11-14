#讀取對話紀錄
def read_file(filesname):
	record = []
	with open(filesname,'r',encoding='utf-8-sig') as f:
		for line in f:
			record.append(line.strip())
	return record
#改變 暫時儲存continue的用法
def conver(record):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_stick_count = 0
	viki_stick_count = 0
	for line in record:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_stick_count += len(m)
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_stick_count += len(m)
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen says :' , allen_word_count ,'words' , allen_stick_count , 'sticks')
	print('Viki says :' , viki_word_count , 'words' , viki_stick_count , 'sticks')

#寫入
def write_file(filesname,record):
	with open(filesname,'w') as f:
		for line in record :
			f.write(line + '\n')

def main():
	record = read_file('[LINE]Viki.txt')
	record = conver(record)
	#write_file('output.txt',record)
main()
