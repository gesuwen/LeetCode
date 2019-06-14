# Given a text file file.txt, print just the 10th line of the file.
#
# Example:
#
# Assume that file.txt has the following content:
#
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
#
# Line 10

# Read from the file file.txt and output the tenth line to stdout.
count=0
while read line && [ $count -le 10 ]; do
    let 'count = count + 1'
    if [ $count -eq 10 ]; then
        echo $line
        exit 0
    fi
done < file.txt
