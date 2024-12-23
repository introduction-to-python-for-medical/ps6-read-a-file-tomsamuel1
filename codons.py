def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    codon2aa = {}
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      aa = cells[2]
      codon2aa[codon] = aa
    return codon2aa

