esearch -db assembly -query $1 \
    | esummary \
    | xtract -pattern DocumentSummary -element FtpPath_GenBank \
    | while read -r line ; 
    do
        fname=$(echo $line | grep -o 'GCA_.*' | sed 's/$/_genomic.gbff.gz/') ;
        wget "$line/$fname" ;
    done
