import sys, copy, random


from compute import *
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


def write_time(x):

	time_format="%Y-%m-%d %H:%M:%S"
	return xleft.strftime(time_format)

	

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



if __name__ == '__main__':
			
	k = int(sys.argv[1])
	start_algo(k)