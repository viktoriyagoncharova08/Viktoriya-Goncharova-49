#Лабораторная4.3
from Bio import SeqIO
from Bio.Seq import Seq
file_path = "D:\питон\example_cds.gb"
for record in SeqIO.parse(file_path, "genbank"):
    desc = record.description
    if desc.startswith(record.id):
        desc = desc[len(record.id):].lstrip()
    for feature in record.features:
        if feature.type == "CDS":
            location = feature.location
            start = location.start + 1 
            end = location.end
            strand = "+" if location.strand >= 0 else "-"
            coords = f"[{start}:{end}]({strand})"
            cds_seq = feature.extract(record.seq)
            protein_seq = cds_seq.translate(to_stop=True)
            gene_name = feature.qualifiers.get('product', [''])[0]
            if not gene_name:
                gene_name = feature.qualifiers.get('gene', [''])[0]
            if not gene_name:
                gene_name = "CDS"
            print(f"{record.id}: {desc}")
            print(f"Coding sequence location = {coords}")
            print(f"Translation =")
            seq_str = str(protein_seq)
            for i in range(0, len(seq_str), 60):
                print(seq_str[i:i+60])
            break