#!/usr/bin/python3

log_title = ""

project_name = input("Введите название проекта\n")

react_temp = input("Введите температуру проведения реакции\n")
log_title += ("melting low " + react_temp + "\n")

primer_lenght = input("Введите желаемую длину праймеров\n")
log_title += ("lenght low " + primer_lenght+ "\n")

codon_freq = input("Введите пороговое значение частоты встречаемости кодонов\n")
log_title += ("frequency threshold " + codon_freq + "\n")
                   
sys_expr = input("Укажите систему экспрессии:\n1 - E.coli\n2 - CHO\n3 - Human\n4 - Sf9\n")
log_title += ("codon ")
if sys_expr == 1:
  log_title += ("codon E.coli\n")
elif sys_expr == 3:
  log_title += ("codon H. sapiens\n")
elif sys_expr == 2:
  CHO = open("CHO.txt", "r")
  for i in CHO:
    log_title += (i + "\n")
else:
  Sf9 = open("Sf9.txt", "r")
  for i in Sf9:
    log_title += (i + "\n")

print(log_title)
                  
if input("Последовательность аминокислотная или нуклеотидная?\n1 - аминокислотная\n2 - нуклеотидная\n") == "1":
  seq_prot = input("Введите последовательность белка\n")
  seq_nt = ""
else:
  seq_nt = input("Введите нуклеотидную последовательность\n")
  seq_prot = ""

fragment_list = []
if seq_prot == "":
  seq_len = len(seq_nt)
else:
  seq_len = len(seq_prot)                 
                   
if seq_len >= 500 and seq_prot == "":
  fragment_num = round(len(seq_nt)/350)
  fragment_len = round(seq_len/fragment_num)
  for i in range(fragment_num):
    if i == fragment_num-1:
      fragment_list.append(seq_nt[(seq_len-fragment_len*i):len(seq_nt)])
    else:
      fragment_list.append(seq_nt[(fragment_len*i):(fragment_len*(i+1))])
elif seq_len < 500:
  fragment_num = 1
  fragment_list.append(seq_nt)
elif seq_len >= 166 and seq_nt == "":
  fragment_num = round(len(seq_prot)/166)
  fragment_len = round(seq_len/fragment_num)
  for i in range(fragment_num):
    if i == fragment_num-1:
      fragment_list.append(seq_prot[(seq_len-fragment_len*i):len(seq_prot)])
    else:
      fragment_list.append(seq_prot[fragment_len*i:fragment_len*(i+1)])
else:
  fragment_num = 1
  fragment_list.append(seq_prot)
                   
for i in fragment_list:
  output_i = open(project_name + "_" + i + ".txt", "w")
  output_i.write(log_title + "\nnucleotide\n" + i + "//")
  output_i.close()  
                   
data_log = open("data_log.txt", "w")
data_log.write("project_name " + project_name + "\nfragment_num" + str(fragment_num) + "\nreact_temp " + str(react_temp))
data_log.close()

bash_script = open("bash_next.sh", "w")
bash_script.write("#!/bin/bash\n")

for i in range(fragment_num):
  bash_script.write("dnaworks " + project_name + "_" + str(i) + ".inp\n")
  
bash_script.write("python3 Primer_Alg.py\n")
bash_script("mkdir " + project_name + "\n" )

for i in range(fragment_num):
  bash_script("cp " + project_name + "_" + str(i) + ".inp\n" + "rm -rf " + project_name + "_" + str(i) + ".inp\n")

bash_script("cp " + project_name + ".txt\n" +  "rm -rf " + project_name + ".txt\n")
bash_script("cp " + project_name + "_hairpin.txt\n" +  "rm -rf " + project_name + "_hairpin.txt\n")
bash_script("cp " + project_name + "_high_temp.txt\n" +  "rm -rf " + project_name + '_high_temp.txt\n')

bash_script.close()










