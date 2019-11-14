#讀取對話紀錄
def read_file(filesname):
	record = []
	with open(filesname,'r',encoding='utf-8-sig') as f:
		for line in f:
			record.append(line.strip())
	return record
#改變
def conver(record):
	new = []
	person = None
	for line in record:
		if line == 'Allen':
			person = 'Allen'
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + line)
	return(new)
#寫入
def write_file(filesname,record):
	with open(filesname,'w') as f:
		for line in record :
			f.write(line + '\n')

def main():
	record = read_file('input.txt')
	record = conver(record)
	write_file('output.txt',record)
main()
