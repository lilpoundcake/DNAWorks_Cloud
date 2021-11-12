#!/usr/bin/python3

#генерация файлов из формата DNAWorks

import primer3
import pandas as pd
import numpy as np

primer_list = [] #записывает все последовательности праймеров
sequence = ''
start_primer = 0
start_seq = 0

data_log = open("data_log.txt", "r")
file_name = data_log.readline().split()[1]

for n in range(int(data_log.readline().split()[1])):
    primers = open(file_name + '_' + str(n+1) +'.txt', 'r')
    for i in primers:
        if 'oligonucleotides need to be synthesized' in i:
            start_primer += 1
            number_of_primers = int(i.strip().split(' ')[0])
            #print(number_of_primers)
        elif 'The DNA sequence' in i:
            start_seq += 1
        elif start_seq == 1:
            for z in primers:
                if "---" in z:
                    start_seq = 0
                    break
                else:
                    if len(z.strip().split(' ')) > 1:
                        sequence += z.strip().split(' ')[1]
                    else:
                        continue
        elif start_primer == 1:
            for _ in range(number_of_primers):
                primer_list.append(primers.readline().strip().split(' ')[1])
            start_primer = 0
            break
    primers.close()

project_name = file_name #input('Введите имя проекта ')
list_primer = open(project_name + '_SG_primers.fasta', 'w')
for i in range(len(primer_list)):
    list_primer.write('>' + file_name + '_%i' % i + '\n' + primer_list[i] + '\n')

project_seq = open(project_name + '_sequence.fasta', 'w')
project_seq.write('>' + project_name + '\n' + sequence)

list_primer.close()
primers.close()
project_seq.close()

primers_files = open(project_name + '_SG_primers.fasta', 'r')
primers = dict()
for i in primers_files:
    primers[i.strip('>').strip('\n')] = primers_files.readline().strip()
    
df1 = pd.DataFrame(index=primers.keys(), columns=('Seq', 'Tm', 'Hairpin')) #для анализа гомодимеров
df1.index.name = 'Name'
react_temp = int(data_log.readline().split()[1])

for i in df1.index:
    df1.loc[i, 'Seq'] = primers[i].upper()
    df1.loc[i, 'Tm'] = primer3.calcTm(primers[i], mv_conc=25.0, dv_conc=1.5, dntp_conc=0.8, dna_conc=0.04)
    df1.loc[i, 'Hairpin'] = primer3.calcHairpinTm(primers[i], mv_conc=25.0, dv_conc=1.5, dntp_conc=0.8, dna_conc=0.04,temp_c=25)
    df1.loc[i, 'Homodimer'] = primer3.calcHomodimerTm(primers[i], mv_conc=25.0, dv_conc=1.5, dntp_conc=0.8, dna_conc=0.04, temp_c=25)
    df1.loc[i, 'GC content'] = int(100 * (primers[i].count('G') + primers[i].count('C')) / len(primers[i]))
    df1.loc[i, 'React_temp'] = react_temp
    
    
df2 = pd.DataFrame(index=primers.keys(), columns=primers.keys()) #для анализа гетеродимеров

for i in df1.index:
    for j in df1.index:
        if df2.loc[i, j] == df2.loc[j, i] and df2.loc[i, j] != 'NaN':
            continue
        else:
            df2.loc[i, j] = primer3.calcHeterodimerTm(primers[i], primers[j], mv_conc=25.0, dv_conc=1.5, dntp_conc=0.8, dna_conc=0.04, temp_c=25)
            df2.loc[j, i] = df2.loc[i, j]

hetero_Tm = dict()
n = 0

for i in df2.index:
    for j in df2.index:
        if df2.loc[i, j] > react_temp:
            hetero_Tm[n] = [i, j, df2.loc[i, j]]
            n += 1
            
df3 = pd.DataFrame(hetero_Tm, index=['Seq1', 'Seq2', 'Tm']) #для анализа гетеродимеров с высокой температурой отжига
df3 = df3.transpose()

GC_30 = dict()
for i in range(len(sequence) - 30):
    GC_30[i] = int(100 * (sequence[i: i+30].count('G') + sequence[i: i+30].count('C')) / len(sequence[i: i+30]))

GC_content = pd.DataFrame(GC_30, index=['GC_content'])
GC_content = GC_content.transpose()

mean_GC = int(100 * (sequence.count('G') + sequence.count('C')) / len(sequence))

for i in GC_content.index:
    GC_content.loc[i, 'Max'] = 100
    GC_content.loc[i, 'Min'] = 0
    GC_content.loc[i, 'Mean'] = mean_GC

print('Hairpins \n', df1[df1.Hairpin > react_temp].loc[:, ['Hairpin', 'Seq']], '\n', df3)

high_hairpin = df1[df1.Hairpin > react_temp].loc[:, ['Hairpin', 'Seq']]

high_hairpin.to_csv(project_name + "_hairpin.csv")
df3.to_csv(project_name + "_high_temp.csv")

primers_files.close()
