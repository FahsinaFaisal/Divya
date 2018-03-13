echo "Enter a number:"
read a
i=0
fact=1
while [ $i -ne $a ]
do
i=`expr $i + 1`
fact=`expr $fact \* $i`
done
echo "Factorial=$fact" 
