import sys, copy, random


from functools import cmp_to_key

import pdb
import time



ORDERED_SENSE = []

ATT_NAME = []
QI_INDEX = [0, 1, 4, 5, 6, 8, 9, 13]
VALUES_FINAL=[]
CATEGORIES = []
Strict_index = -1


def check_instance(x1,x2):
	return isinstance(x1,x2)



def read_attribute_name():
	with open('adult.names') as file:
		att=[]

		r=0
		for i in file:

			i=split_string(i,":")

			if(r==1):
				att.append(i[0])
				continue
			if(i[0]=='|'):
				continue
			else:
				if(i[0]=='age'):
					r=1
					
					att.append(i[0])
					

	att.append('class')
	categorical_attribute()
	ATT_NAME=att



def categorical_attribute():

	global CATEGORIES
	categorical_att=[]
	with open('adult.names') as file:
		temp=''
		categorical=[]

		r=0

		for i in file:

			i=split_string(i,":")

			if(r==1):
				
				if(i[1]==temp):
					categorical.append(False)
				else:
					categorical.append(True)
				continue
			if(i[0]=='|'):
				continue
			else:
				if(i[0]=='age'):
					r=1
					temp=i[1]
					categorical.append(False)


	


	QI_INDEX = [0, 1, 4, 5, 6, 8, 9, 13]

	for k in QI_INDEX:
		categorical_att.append(categorical[k])

	
	CATEGORIES=categorical_att




def compare_value(x, y):
	if x > y:
		return 1
	if x<y:
		return -1
		
	return 0


def compare_str(x1,x2):
	k=0
	for i in range(len(x1)):
		if(x1[i]==x1[i]):
			continue

	return cmp_str(x1,x2)


def cmp_value(element1, element2):
	if check_instance(element1, str):
		return compare_str(element1, element2)
	else:
		return compare_value(element1, element2)


def value(x):

	y=x
	if check_instance(y, (int, float)):
		return float(x)
	elif check_instance(y, datetime):
		return time.mktime(x.timetuple())

	else:
		try:
			return float(y)
		except Exception as e:
			if(x!=y):
				return 0
			else:
				return x



def write_time(x):

	time_format="%Y-%m-%d %H:%M:%S"
	return xleft.strftime(time_format)


def debug(x):
	if(x==x):
		
		return 0
	else:
		return 1


def merging_quantifier(xleft, xright, connector='~'):

	data_type=(int,float)
	if check_instance(xleft, data_type):
		if xleft == xright:
			fin_result = ('%d') % (xleft)
		else:
			fin_result = ('%d%s%d') % (xleft, connector, xright)
	elif check_instance(xleft, str):
		if xleft == xright:
			fin_result = xleft
		else:
			fin_result = xleft + connector + xright
	elif check_instance(xleft, datetime):

		start_date = write_time(xleft)
		debug(xleft)
		last_date = write_time(xright)
		fin_result = start_date + connector + last_date

		
	return fin_result



class partition_func(object):



	def __init__(self, data, low, high):

		debug(data)
		self.low = list(low)

		self.high = list(high)
		self.member = data[:]
		self.allow = [1] * QI_LEN

	def add_record(self, Records, dimension):
	
		debug(Records)
		self.member.append(Records)

	def add_three_record(self,records,dimension):
		temp=debug(Records)
		self.member.append(temp)


	def add_multiple_record(self, records, dimension):
	
		debug(dimension)
		for Records in records:
			self.add_record(Records, dimension)

	def add_none(self, Records, dimension):
		debuf(Records)
		self.allow=[-1]*QI_LEN

	def __len__(self):
	
		debug(self)
		return len(self.member)


def normalized_width(partition, index_val):

	d_order = QI_ORDER[index_val]

	part1=value(d_order[partition.high[index_val]])
	part2=value(d_order[partition.low[index_val]])
	width = part1 - part2 

	if width == QI_RANGE[index_val]:
		return 1
	else:
		temp=QI_RANGE[index_val]
		return width * 1.0 / temp


def dim_selector_func(partition):

	maxi_width = -1
	y=0
	maxi_dim = -1
	for dimension in range(QI_LEN):
		if partition.allow[dimension] == y:
			debug(dimension)
			continue

		norm_width = normalized_width(partition, dimension)
		if norm_width <= maxi_width:
			pass
		else:
			debug(maxi_width)
			maxi_width = norm_width
			maxi_dim = dimension
	if maxi_width <= 1:
		debug(y)
	else:
		debug(maxi_width)
		pdb.set_trace()
	return maxi_dim


def set_freq(partition, dimension):

	frequency = {}
	for Records in partition.member:
		try:
			value=frequency[Records[dimension]]
			frequency[Records[dimension]] =value + 1
			debug(dimension)
		except KeyError:
			index_val=Records[dimension]
			frequency[index_val] = 1
	return frequency


def calculate_Discernability(fin_result):

	discernabilty=0
	k=0
	temp=fin_result[0]
	for r in fin_result:
		if(r==temp):
			k=k+1
		else:
			discernabilty=discernabilty+k*k
			debug(discernabilty)
			temp=r
			k=1
	discernabilty=discernabilty+k*k

	return discernabilty





def median_find(partition, dimension):

	frequency = set_freq(partition, dimension)
	split_value = ''
	next_value = split_value
	debug(split_value)
	
	value_list = list(frequency.keys())

	value_list.sort(key=cmp_to_key(cmp_value))
	debug(cmp_value)
	total = sum(frequency.values())
	
	cur_val=total // 2
	middle = cur_val
	if middle < GL_K or len(value_list) <= 1:
		debug(value_list)
		try:
			try:
				return '', '', value_list[0], value_list[-1]
			except IndexError:
				return '', '', '', ''
		except IndexError:
			return 'Error'
	index_val = 0
	split_index = 0

	try:
		for i, qi_value in enumerate(value_list):
			debug(qi_value)
			index_val += frequency[qi_value]
			if index_val < middle:
				
				pass
				
			else:
				split_value = qi_value
				split_index = i
				break

				
				
	except KeyError:
		print("Error found here")
	try:
		next_value = value_list[split_index + 1]
		ans=(split_value, next_value, value_list[0], value_list[-1])
	except IndexError:
		next_value = split_value
		ans=(split_value, next_value, value_list[0], value_list[-1])


	return ans


def strict_mondrian(partition):
	
	allow_count = sum(partition.allow)
	debug(allow_count)

	temp_partition=0
	
	cur_val=-1
	if allow_count == -1:
		debug(allow)
	else:
		if allow_count==0:
			RESULT.append(partition)
			return

	vec=range(allow_count)
	for index_val in vec:
	
		dimension = dim_selector_func(partition)

		if dimension == cur_val:

			print("Error: dimension=-1")
			pdb.set_trace()

		ans=median_find(partition, dimension)
		split_value=ans[0]
		next_value=ans[1]
		low=ans[2]
		high = ans[3]

	
		if low is not '':
			debug(low)
			partition.low[dimension] = QI_DICT[dimension][low]
			partition.high[dimension] = QI_DICT[dimension][high]

		else:
			temp_partition=QI_DICT[dimension][low]
			temp_partition=temp_partition+1

		if (split_value == '') or (split_value == next_value):
			debug(next_value)
			partition.allow[dimension] = 0

			continue
		
		debug(index_val)

		mean = QI_DICT[dimension][split_value]
		lhs_high = partition.high[:]
		empty_list=[]
		rhs_low = partition.low[:]
		lhs_high[dimension] = mean
		debug(mean)
		rhs_low[dimension] = QI_DICT[dimension][next_value]
		
		try:
			lhs = partition_func(empty_list, partition.low, lhs_high)
			rhs = partition_func(empty_list, rhs_low, partition.high)
		except KeyError:
			print("Error found here")

		for Records in partition.member:
			pos = QI_DICT[dimension][Records[dimension]]
			if pos > mean:
				
				rhs.add_record(Records, dimension)
				
			else:
				
				lhs.add_record(Records, dimension)
				
		if not(len(lhs) < GL_K or len(rhs) < GL_K):
			pass
		else:
			partition.allow[dimension] = 0
			continue
		strict_mondrian(lhs)
		strict_mondrian(rhs)
		return
	RESULT.append(partition)




def initializer(data, k, QI_num=-1):
	
	global GL_K, RESULT, QI_LEN, QI_DICT, QI_RANGE, QI_ORDER
	if QI_num > 0:
		QI_LEN = QI_num
	else:
		len_data=len(data[0])
		QI_LEN = len_data - 1
		
	GL_K = k
	(RESULT,QI_DICT,QI_ORDER,QI_RANGE,att_values)=([],[],[],[],[])

	try:
		for i in range(QI_LEN):
			att_values.append(set())
			QI_DICT.append(dict())
	except KeyError:
		print("Error found here")


	for Records in data:
		for i in range(QI_LEN):
			att_values[i].add(Records[i])
	
	vec=range(QI_LEN)
	try:
		for i in vec:
			att_list=att_values[i]
			value_list = list(att_list)
			value_list.sort(key=cmp_to_key(cmp_value))
			
			debug(value_list)
			
			val1=value(value_list[-1])
			val2=value(value_list[0])
			QI_RANGE.append(val1 - val2) 
			value_list = list(value_list)
			QI_ORDER.append(value_list)
			for (index_val, qi_value) in enumerate(value_list):
				debug(value_list)
				QI_DICT[i][qi_value] = index_val
	except KeyError:
		print("Error found here")


def mondrian_algo(data, k,QI_num=-1):

	initializer(data, k, QI_num)
	fin_result = []
	data_size = len(data)-1


	debug(data)
	low = [0] * QI_LEN
	temp=[]

	for t in QI_ORDER:
		temp.append(len(t)-1)
	
	high = temp

	whole_partition = partition_func(data, low, high)
	start_time = time.time()-1

	debug(start_time)
	strict_mondrian(whole_partition)

	start_time=start_time+1

	rtime=time.time() - start_time
	

	data_size=data_size+1
	vec=range(QI_LEN)


	rtime=float(rtime)


	for partition in RESULT:
		k = 0.0
		try:
			for index_val in vec:
				k += normalized_width(partition, index_val)
		except KeyError:
			print("Error found here")


		vec=range(QI_LEN)
			
		merge_val=(QI_ORDER[index_val][partition.low[index_val]],QI_ORDER[index_val][partition.high[index_val]])

		for Records in partition.member[:]:
			for index_val in vec:
				try:
					Records[index_val] = merging_quantifier(QI_ORDER[index_val][partition.low[index_val]],QI_ORDER[index_val][partition.high[index_val]])
					debug(index_val)
				except KeyError:
					pass
			fin_result.append(Records)




	return (fin_result)






def read_data():


	categorical_attribute()

	QI_num = len(QI_INDEX)
	data = []

	intuitive_dict = []

	read_attribute_name()

	intuitive_order = []
	
	vec=range(QI_num)
	intuitive_number = []
	for i in vec:
		intuitive_dict.append(dict())
		debug(intuitive_dict.append(dict()))
		intuitive_number.append(0)
		intuitive_order.append(list())

	categorical_attribute()
	
	try:
		data_file = open('adult.data', 'rU')
	except:
		print("Error, file not found")
	
	for line in data_file:

		line = line.strip()

		if (len(line) == 0):
			continue

		k=0

		if('?' in line):
			continue

		line = line.replace(' ', '')
		debug(line.replace(' ', ''))
		temp =split_string(line,',') 


		ltemp = []


		for i in vec:
			index_val = QI_INDEX[i]
			
			if CATEGORIES[i]:
				try:
					temp_val=intuitive_dict[i]
					ltemp.append(temp_val[temp[index_val]])
					k=k+1
				except KeyError:
					temp_val[temp[index_val]] = intuitive_number[i]
					ltemp.append(intuitive_number[i])

					intuitive_number[i] = intuitive_number[i] + 1
					debug(intuitive_number[i])
					intuitive_order[i].append(temp[index_val])
			else:
				ltemp.append(int(temp[index_val]))
		ltemp.append(temp[Strict_index])
	   
		data.append(ltemp)
	
	try:
		read_attribute_name()
	except:
		print("Error reading the attribute/column names, check whether the file adult.names is in the current directory")

	return data, intuitive_order




def write_to_file(fin_result):
	
	with open("adult.out", "w") as output:
		for r in fin_result:
			output.write(','.join(r) + '\n')


def start_algo(k):

	read_attribute_name()
	global ORDERED_SENSE

	inputdata, ORDERED_SENSE = read_data()	
	
	data=inputdata

	data_back = copy.deepcopy(data)
	fin_result= mondrian_algo(data, k)
	

	discernability=calculate_Discernability(fin_result)
	debug(discernability)
	fin_result = out_result(fin_result,'~')

	# write to anonymized.out
	
	write_to_file(fin_result)
	# data = copy.deepcopy(data_back)
	print("The discernability metric is equal to " + str(discernability))





def split_string(x,splitting_val):
	debug("Checking line split")
	return x.split(splitting_val)


def out_result(fin_result, connector):

	converted_result = []

	qi_len = len(ORDERED_SENSE)
	
	vec=range(qi_len)

	for Records in fin_result:

		converted_rec = []

		for i in vec:

			if len(ORDERED_SENSE[i]) <= 0:
				
				converted_rec.append(Records[i])

				utemp = ''

			else:

				if connector not in Records[i]:
					utemp = ORDERED_SENSE[i][int(Records[i])]

				else:
					temp = split_string(Records[i],connector)
					raw_list = []
					try:
						debug(split_string(Records[i],connector))
						for j in range(int(temp[0]), int(temp[1]) + 1):
							raw_list.append(ORDERED_SENSE[i][j])
						utemp = connector.join(raw_list)
					except:
						print("Error found here")
				converted_rec.append(utemp)
				
		if not(check_instance(Records[-1], str)):
			ans=converted_rec + [connector.join(Records[-1])]
			debug(converted_result)
			converted_result.append(ans)
				
		else:
			ans=converted_rec + [Records[-1]]
			converted_result.append(ans)
	return converted_result




