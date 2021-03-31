import re

def clean_data(path, out_path):
	with open(path, 'r') as f:
		with open(out_path, 'w') as out_f:
			for i in range(22):
				line = f.readline()
				#out_f.write(line)
			line = f.readline()
			while line:
				left = line.strip()
				left = re.sub(r'\s+', ',', left)
				line = f.readline()
				right = re.sub(r'\n+', '', line.strip())
				right = re.sub(r'\s+', ',', right)
				out_f.write(left + ',' + right)
				line = f.readline()
				if line:
					out_f.write('\n')

