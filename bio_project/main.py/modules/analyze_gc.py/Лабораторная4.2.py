#Лабораторная4.2
from Bio import SeqIO
file_path ="D:\питон\example_cds.gb"
cds_list = []
for record in SeqIO.parse(file_path, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            cds_seq = feature.extract(record.seq)
            g = cds_seq.count('G')
            c = cds_seq.count('C')
            total = len(cds_seq)
            if total > 0:
                gc_content = (g + c) / total
            else:
                gc_content = 0.0
            desc = record.description
            if desc.startswith(record.id):
                desc = desc[len(record.id):].lstrip()
            description = f"{record.id}: {desc}, complete cds"
            
            cds_list.append({
                'description': description,
                'gc_content': gc_content
            })
cds_list_sorted = sorted(cds_list, key=lambda x: x['gc_content'])
for cds in cds_list_sorted:
    print(f"{cds['description']}, GC = {cds['gc_content']}")