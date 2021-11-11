#!/usr/bin/python3

log_title = ""

project_name = input("Введите название проекта\n")

react_temp = input("Введите температуру проведения реакции\n")
log_title += ("melting low " + react_temp + "\n")

primer_length = input("Введите желаемую длину праймеров\n")
log_title += ("lenght low " + primer_lenght+ "\n")

codon_freq = input("Введите пороговое значение частоты встречаемости кодоновn\")
log_title += ("frequency threshold " + codon_freq + "\n")
                   
sys_expr = input("Укажите систему экспрессии:\n
                  1 - E.coli\n
                  2 - CHO\n
                  3 - Human\n
                  4 - Sf9\n")
if sys_expr == 1:
  log_title += ("codon E.coli\n")
elif sys_expr == 3:
  log_title += ("codon H. sapiens\n")
elif sys_expr == 2:
  log_title += ("""Gly     GGG      2063.00     13.44      0.00\n 
                Gly     GGA      2425.00     15.80      0.00\n
Gly     GGT      1968.00     12.82      0.00\n
Gly     GGC      3268.00     21.29      0.00\n
Glu     GAG      6311.00     41.11      0.00\n
Glu     GAA      4355.00     28.37      0.00\n
Asp     GAT      3781.00     24.63      0.00\n
Asp     GAC      4310.00     28.07      0.00\n
Val     GTG      4628.00     30.14      0.00\n
Val     GTA      1202.00      7.83      0.00\n
Val     GTT      1780.00     11.59      0.00\n
Val     GTC      2408.00     15.68      0.00\n
Ala     GCG       765.00      4.98      0.00\n
Ala     GCA      2497.00     16.26      0.00\n
Ala     GCT      3432.00     22.35      0.00\n
Ala     GCC      3973.00     25.88      0.00\n
Arg     AGG      1570.00     10.23      0.00\n
Arg     AGA      1557.00     10.14      0.00\n
Ser     AGT      1756.00     11.44      0.00\n
Ser     AGC      2521.00     16.42      0.00\n
Lys     AAG      5895.00     38.40      0.00\n
Lys     AAA      3782.00     24.63      0.00\n
Asn     AAT      2671.00     17.40      0.00\n
Asn     AAC      3248.00     21.16      0.00\n
Met     ATG      3538.00     23.04      0.00\n
Ile     ATA      1053.00      6.86      0.00\n
Ile     ATT      2673.00     17.41      0.00\n
Ile     ATC      3808.00     24.80      0.00\n
Thr     ACG       685.00      4.46      0.00\n
Thr     ACA      2418.00     15.75      0.00\n
Thr     ACT      2172.00     14.15      0.00\n
Thr     ACC      3118.00     20.31      0.00\n
Trp     TGG      2012.00     13.11      0.00\n
End     TGA       177.00      1.15      0.00\n
Cys     TGT      1397.00      9.10      0.00\n
Cys     TGC      1589.00     10.35      0.00\n
End     TAG        84.00      0.55      0.00\n
End     TAA        93.00      0.61      0.00\n
Tyr     TAT      2017.00     13.14      0.00\n
Tyr     TAC      2519.00     16.41      0.00\n
Leu     TTG      2169.00     14.13      0.00\n
Leu     TTA       978.00      6.37      0.00\n
Phe     TTT      3005.00     19.57      0.00\n
Phe     TTC      3381.00     22.02      0.00\n
Ser     TCG       529.00      3.45      0.00\n
Ser     TCA      1577.00     10.27      0.00\n
Ser     TCT      2450.00     15.96      0.00\n
Ser     TCC      2529.00     16.47      0.00\n
Arg     CGG      1558.00     10.15      0.00\n
Arg     CGA      1102.00      7.18      0.00\n
Arg     CGT       863.00      5.62      0.00\n
Arg     CGC      1429.00      9.31      0.00\n
Gln     CAG      5122.00     33.36      0.00\n
Gln     CAA      1587.00     10.34      0.00\n
His     CAT      1563.00     10.18      0.00\n
His     CAC      1980.00     12.90      0.00\n
Leu     CTG      5955.00     38.79      0.00\n
Leu     CTA      1174.00      7.65      0.00\n
Leu     CTT      2023.00     13.18      0.00\n
Leu     CTC      2818.00     18.36      0.00\n
Pro     CCG       657.00      4.28      0.00\n
Pro     CCA      2388.00     15.55      0.00\n
Pro     CCT      2563.00     16.69      0.00\n
Pro     CCC      2608.00     16.99      0.00\n
//""")

print(log_title)
                  
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
                   
#for i in range(fragm_num):
  
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
