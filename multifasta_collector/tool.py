"""Function to collect multifasta and put it 
in a dictionary with header as key and sequence as value. 

Author: Jimmy Capecci
"""


def multi_fasta_collector(fasta: str) -> dict[str, str]:
    """Collects mulit-fasta files and turns into dictionary

    :param fasta: Path to multi-fasta file
    :return: dictionary containing header as key and sequence as value
    """

    # Intialize dictionary
    header_seq = {}

    # Open file in read mode
    with open(fasta, 'r') as f:

        # Intialize orginal header
        current_header = None

        # for each line in fasta file strip new lines
        for line in f:
            line = line.strip()

            # If line is blank skip it
            if not line:
                continue
            
            # If line starts with '>' its a header initalize it and add to 
            # dictionary
            if line.startswith('>'):
                current_header = line
                header_seq[current_header] = ''

            # Else its a sequence add to dictionary
            elif current_header:
                header_seq[current_header] += line
    # Return the dictionary
    return header_seq
