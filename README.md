# MultiFastaCollector

## Overview
A simple Python tool for collecting and organizing multi-FASTA sequence data into convenient dictionary structures.

## What it does
- Parses multi-FASTA files
- Converts sequences into a Python dictionary
- Uses FASTA headers as keys and sequences as values

## Constraints
- Assumes valid FASTA format
- Headers must start with `>`
- Sequences may span multiple lines

## Example fasta format
In this repo an example FASTA is provided. FASTA generally have the following format
```text
>sp|P49913|CAMP_HUMAN Cathelicidin antimicrobial peptide OS=Homo sapiens OX=9606 GN=CAMP PE=1 SV=1
MKTQRDGHSLGRWSLVLLLLGLVMPLAIIAQVLSYKEAVLRAIDGINQRSSDANLYRLLD
LDPRPTMDGDPDTPKPVSFTVKETVCPRTTQQSPEDCDFKKDGLVKRCMGTVTLNQARGS
FDISCDKDNKRFALLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES
>sp|P27695|APEX1_HUMAN DNA repair nuclease/redox regulator APEX1 OS=Homo sapiens OX=9606 GN=APEX1 PE=1 SV=2
MPKRGKKGAVAEDGDELRTEPEAKKSKTAAKKNDKEAAGEGPALYEDPPDQKTSPSGKPA
TLKICSWNVDGLRAWIKKKGLDWVKEEAPDILCLQETKCSENKLPAELQELPGLSHQYWS
APSDKEGYSGVGLLSRQCPLKVSYGIGDEEHDQEGRVIVAEFDSFVLVTAYVPNAGRGLV
RLEYRQRWDEAFRKFLKGLASRKPLVLCGDLNVAHEEIDLRNPKGNKKNAGFTPQERQGF
GELLQAVPLADSFRHLYPNTPYAYTFWTYMMNARSKNVGWRLDYFLLSHSLLPALCDSKI
RSKALGSDHCPITLYLAL
```

## Installation
Disclaimer: Requires Git to be installed on your system

The run this comand
```bash
pip install git+https://github.com/jcapecci09/MultiFastaCollector.git
```

## Usage instructions

Ensure the FASTA file is in your current working directory (or provide a full file path). In this we use the FASTA provided in the repo: `multifasta.txt`. 

```python
from multifasta_collector import mfc

# Collect multifasta into dictionary
d = mfc('multifasta.txt')

# with a dictionary you can do a variety of different actions
# collect values and keys in list
headers = list(d.keys())
sequences = list(d.values())

# Show first sequence and its header
print(f'header: {headers[0]}\nsequence: {sequences[0]}')

print()

# Show last sequence and its header
print(f'header: {headers[-1]}\nsequence: {sequences[-1]}')
```

## Data Source
The exmaple multi-FASTA was collected from [UniProt](https://www.uniprot.org/).
