import pandas as pd
import os
MarRef = pd.read_table("MarRef.tsv",sep="\t")
MarRef.head()
acc_list = MarRef["assembly_accession_genbank"]
for acc in acc_list:
    get_cmd = "./get_gffb.sh "
    os.system(get_cmd+'"'+acc+'"')
