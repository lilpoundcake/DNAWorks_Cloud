#!/usr/bin/python3

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

if len(seq) >= 500 and seq_prot == 0:
  fragment_num = round(len(seq)/350)
  fragment_len = round(seq_nt/)
