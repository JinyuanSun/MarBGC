for file in *gbff
do
	antismash -c 8 --genefinding-tool none $file
done
