
# python3 nMAP_genotype_determination.py nMAP_test_sample.txt result_20.txt 20

#sys.argv[1];input file
#sys.argv[2];output file
#sys.argv[3];minimum cluster size


import sys
import re

f1 = open(sys.argv[1])

###SNP information
#line_l[0] ;Probe Set ID
#line_l[1] ;dbSNP RS ID
#line_l[2] ;Chromosome
#line_l[3] ;Chromosome Start
#line_l[4] ;Genotype-AA
#line_l[5] ;Genotype-AB
#line_l[6] ;Genotype-BB

###400 Control information (Itv:Interval)
#line_l[7] ;Strength_Number
#line_l[8] ;Strength_Itv_Bottom
#line_l[9] ;Strength_Itv_Up
#line_l[10];Ratio-AA_Number
#line_l[11];Ratio-AA_Itv_Bottom
#line_l[12];Ratio-AA_Itv_Up
#line_l[13];Ratio-AB_Number
#line_l[14];Ratio-AB_Itv_Bottom
#line_l[15];Ratio-AB_Itv_Up
#line_l[16];Ratio-BB_Number
#line_l[17];Ratio-BB_Itv_Bottom
#line_l[18];Ratio-BB_Itv_Up

###Sample information	
#line_l[19];Log_Ratio of sample
#line_l[20];Log_Strength of sample


file_out = open(str(sys.argv[2]),'a')
file_out_count =open("Summury_Of_Genotype_Determination_Minimum_Cluster_Size_"+str(sys.argv[3])+".txt",'a')

count_d = {}
total = 0

for line in f1:
	line = line.replace("\n",'')
	line_l = line.split("\t")
	#print(line_l)

	if line_l[0] =="Probe Set ID":
		output_info = line_l[0:]
		output_info_str = "\t".join(output_info)

		text =(output_info_str,"\t","Genotype","\n")
		file_out.writelines(text)
		continue

	Genotype = ""
	Call = ""
	if str(line_l[8]) == "---" or str(line_l[9]) == "---" :
		Genotype = "---"
		Call = "Un-called"

	elif float(line_l[20]) <= float(line_l[8]) or float(line_l[9]) <= float(line_l[20]):
		Genotype = "---"
		Call = "Un-called"

	#Call = AA
	elif float(line_l[8])<=float(line_l[20])<=float(line_l[9]) and str(line_l[11])!= "---" and int(sys.argv[3]) <= int(line_l[10]) and float(line_l[11])<=float(line_l[19])<=float(line_l[12]):
		Genotype = str(line_l[4])
		Call = "AA"

	#Call = AB
	elif float(line_l[8])<=float(line_l[20])<=float(line_l[9]) and str(line_l[14])!= "---" and int(sys.argv[3]) <= int(line_l[13]) and float(line_l[14])<=float(line_l[19])<=float(line_l[15]):
		Genotype = str(line_l[5])
		Call = "AB"

	#Call = BB
	elif float(line_l[8])<=float(line_l[20])<=float(line_l[9]) and str(line_l[17])!= "---" and int(sys.argv[3]) <= int(line_l[16]) and float(line_l[17])<=float(line_l[19])<=float(line_l[18]):
		Genotype = str(line_l[6])
		Call = "BB"

	else:
		Genotype = "---"
		Call = "Un-called"
		#print(line_l[0])

	output_info = line_l[0:]
	output_info_str = "\t".join(output_info)
	text =(output_info_str,"\t",Genotype,"\n")
	file_out.writelines(text)

	count_d[Call] = count_d.get(Call,0)+1
	total +=1


k, v = zip(*sorted(count_d.items()))

if len(count_d.keys()) == 5:
	#print(k,v)
	text =(str(sys.argv[1]),"\n","total","\t",str(k[0]),"\t",str(k[1]),"\t",str(k[2]),"\t",str(k[3]),"\t",str(k[4]),"\n",str(total),"\t",str(v[0]),"\t",str(v[1]),"\t",str(v[2]),"\t",str(v[3]),"\t",str(v[4]),"\n")       
	file_out_count.writelines(text)

elif len(count_d.keys()) == 4:
	text =(str(sys.argv[1]),"\n","total","\t",str(k[0]),"\t",str(k[1]),"\t",str(k[2]),"\t",str(k[3]),"\n",str(total),"\t",str(v[0]),"\t",str(v[1]),"\t",str(v[2]),"\t",str(v[3]),"\n")       
	file_out_count.writelines(text)

elif len(count_d.keys()) == 3:
	text =(str(sys.argv[1]),"\n","total","\t",str(k[0]),"\t",str(k[1]),"\t",str(k[2]),"\n",str(total),"\t",str(v[0]),"\t",str(v[1]),"\t",str(v[2]),"\n")       
	file_out_count.writelines(text)

elif len(count_d.keys()) == 2:
	text =(str(sys.argv[1]),"\n","total","\t",str(k[0]),"\t",str(k[1]),"\n",str(total),"\t",str(v[0]),"\t",str(v[1]),"\n")       
	file_out_count.writelines(text)

elif len(count_d.keys()) == 1:
	text =(str(sys.argv[1]),"\n","total","\t",str(k[0]),"\n",str(total),"\t",str(v[0]),"\n")       
	file_out_count.writelines(text)

else:
	print(sorted(count_d.keys()))

print("total=",total)
#print(count_d)
file_out.close()
file_out_count.close()
