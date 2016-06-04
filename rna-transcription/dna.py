def to_rna(seq):
    seq_dict = {'A':'U','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in (seq)])
	


