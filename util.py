import json
import sys
import io

data = []
with io.open(sys.argv[1], encoding="latin1") as f:
	for line in f:
		data.append(json.loads(line))

should_print = (len(sys.argv) > 3) and (sys.argv[2] == "--print")
filters = sys.argv[3 if should_print else 2 :]
for _filter in filters:
	count = 0
	for d in data:
		if _filter in d:
			if should_print:
				print d
			count +=1
	print _filter, count
	
