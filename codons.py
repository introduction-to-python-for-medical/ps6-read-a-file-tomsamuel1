def create_codon_dict(file_path):
    codon2aa = {}
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      aa = cells[2]
      codon2aa[codon] = aa
    return codon2aa

