#!/usr/bin/python3

log_title = ""

project_name = input("Введите название проекта\n") """Название проекта и имя входных файлов"""
react_temp = input("Введите температуру проведения реакции\n")
primer_lenth = input("Введите желаемую длину праймеров\n")
codon_freq = input("Введите пороговое значение частоты встречаемости кодоновn\")

sys_expr = input("Укажите систему экспрессии:\n
                  1 - E.coli\n
                  2 - CHO\n
                  3 - Human\n
                  4 - Sf9\n") """Нужно дополнительно прописать кодоны CHO и Sf9"""
                  
if input("Последовательность аминокислотная или нуклеотидная?\n
          1 - аминокислотная\n
          2 - нуклеотидная") == 2:
  seq_prot = input("Введите последовательность белка\n")
  seq_nt = 0
else:
  seq_nt = input("Введите нуклеотидную последовательность\n")
  seq_prot = 0

fragment_list = []
if seq_prot == 0:
  seq_len = len(seq_nt)
else:
  seq_len = len(seq_prot)                 
                   
if len(seq_nt) >= 500 and seq_prot == 0:
  fragment_num = round(len(seq_nt)/350)
  fragment_len = round(seq_nt/fragment_num)
  for i in range(fragment_num):
    if i == fragment_num-1:
      fragment_list.append(seq_nt[seq_len-fragment_len*i)):len(seq_nt)])
    else:
      fragment_list.append(seq_nt[fragment_len*i:fragment_len*(i+1)])
elif len(seq_nt) < 500:
  fragment_num = 1
  fragment_list.append(seq_nt)
elif len(seq_prot) >= 166 and seq_nt == 0:
  fragment_num = round(len(seq_prot)/166)
  fragment_len = round(seq_prot/fragment_num)
  for i in range(fragment_num):
    if i == fragment_num-1:
      fragment_list.append(seq_prot[seq_len-fragment_len*i)):len(seq_prot)])
    else:
      fragment_list.append(seq_prot[fragment_len*i:fragment_len*(i+1)])
else:
  fragment_num = 1
  fragment_list.append(seq_prot)
                   

                   
                   
                   
                   
                   
