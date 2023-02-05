#!/home/bigdata/anaconda3/bin/python
import sys


for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) == 6:
		date, time, store, item, price, payment = data
		item = item.lower()
		item = item.split()
		if any(x in ['toy', 'toys', 'electronic', 'electronics', 'consumer electronics'] for x in item):
			print('%s\t%s' % (' '.join(item), price))
		else:
			continue
	else:
		continue
