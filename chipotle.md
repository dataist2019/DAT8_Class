##Chipotle homework - Class 2

**Question 1**

*Columns*  

There are five columns. First column (order_id) represents the number of customers who ordered. The second column enumarates the quantity order. Third column provides the item's name. The fourth column describes the choices preferred. And lastly, the fifth column names the item's price.

*Rows*

The rows represent each individual order. 
code: head chipotle.tsv
tail chipotle.tsv

**Question 2**

There are 1834 costumers and 4623 orders.
code: tail chipotle.tsv
wc chipotle.tsv

**Question 3**

There are 4623 lines.

wc -l chipotle.tsv

**Question 4**

Chicken burritos are more popular!!
There are 553 chicken burrito orders compared to only 368 steak burrito orders.

code: grep -i "chicken burrito" chipotle.tsv | wc -l
grep -i "steak burrito" chipotle.tsv | wc -l

**Question 5**

People like black beans better with their chicken burritos.
282 chose black beans and 105 preferred pinto beans.
Burning question: did 166 choose not to have any kind of beans with their chicken burrito? [553-(282+105)]

code: grep -i "chicken burrito" chipotle.tsv > chicken_burrito.tsv
grep -i "black" chicken_burrito.tsv | wc -l
grep -i "pinto" chicken burrito.tsv | wc -l

*Question 6*

There are 3 CSV or TSV files in the DAT8 repo: airlines.csv, chipotle.tsv and sms.tsv

code: cd DAT8
find . -name \*.?sv
find . -name '*.?sv'

*Question 7*

The word dictionary appears 210 times.
Note: lowercase dictionary appears only 135 times.

code: grep -r 'dictionary' . | wc -w
grep -r '[Dd]ictionary . | wc -w

*Question 8*

Somebody spent $15 buying water.





