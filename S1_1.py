from Bio.Seq import Seq
from Bio.Align import substitution_matrices
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Emboss.Applications import NeedleCommandline
from Bio import AlignIO


matrix = substitution_matrices.load("BLOSUM62")

seq1 = input("введите первую последовательность: ")
seq2 = input("введите вторую последовательность: ")

alignments = pairwise2.align.globalds(seq1, seq2, matrix, -10, -0.5)
result = format_alignment(*alignments[-1])
total = max(len(seq1), len(seq2))
gaps = result.count("-")
coincidence = result.count("|")

print("\n\n", result, f"""
    Программа использует стандартные настройки:
                #    -datafile EBLOSUM62
                #    -gapopen 10.0
                #    -gapextend 0.5
                #    -endopen 10.0 
                #    -endextend 0.5
             Дополнительная информация\n
             Длинна последовательностей - {total},
             Количество пробелов(gaps) - {gaps},
             Количество совпадений - {coincidence}
""", sep="")
