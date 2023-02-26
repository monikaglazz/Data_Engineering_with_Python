#  get value of variaable

echo $OSTYPE

#  create a shell variable

head -n 1 $testing

# for loops for commands

for filetype in docx odt pdf ; do echo $filetype; done

for filename in people/* 
do 
    echo $filename
done

# many commands in a for loop

for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done
