from MultiFastaCollector.tool import multi_fasta_collector as mfc

# collect sequence
d = mfc('multifasta.txt')

# collect values and keys in list
headers = list(d.keys())
sequences = list(d.values())

# Show first sequence and its header
print(f'header: {headers[0]}\nsequence: {sequences[0]}')

print()

# Show last sequence and its header
print(f'header: {headers[-1]}\nsequence: {sequences[-1]}')

