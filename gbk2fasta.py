def gbkfile2fasta(gbkfilename):
    idlist = []
    seqlist = []
    with open(gbkfilename,'r') as gbkfile:
        
        filetext = gbkfile.read()
        feature_list = filetext.split("FEATURES")[1].replace(" ","").split("\n/")
        #print(feature_list)
        for ele in feature_list:
            if "=" in ele:
                ele_list = ele.split("=")
                key = ele_list[0]
                if key == 'protein_id':
                    try:
                        value = ele_list[1].replace(" ","").replace("\n","").split('"')[1]
                        idlist.append(value)
                        #seqlist.append(value)
                    except IndexError:
                        value = ele_list[1].replace(" ","").replace("\n","").split('"')[0]
                        idlist.append(value)
                        #seqlist.append(value)
                if key == 'translation':
                    try:
                        value = ele_list[1].replace(" ","").replace("\n","").split('"')[1]
                        #idlist.append(key)
                        seqlist.append(value)
                    except IndexError:
                        value = ele_list[1].replace(" ","").replace("\n","").split('"')[0]
                        #idlist.append(key)
                        seqlist.append(value)
                    #print(key,value)
            gbkfile.close()
    #print(idlist)
    fastafilename = gbkfilename.split(".")[0]+".fasta"
    i = 0
    with open(fastafilename,"a+") as fastafile:
        while i in range(len(idlist)):
            fastafile.write(">"+idlist[i]+"\n"+seqlist[i]+"\n")
            i += 1
        fastafile.close()
        
with open("gbk.txt","r") as f:
    for line in f:
        filename=line.strip()
        gbkfile2fasta(filename)
