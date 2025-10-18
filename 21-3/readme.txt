To find a good mo3 constant I used generating functions to make different input.txt files to test
with. In one I ran "shuf -i 100000000-999999999 -n 10000 > input.txt" to create a file filled with
random numbers using increments of time I found that 45 was the best value with this txt file.
(1. Time: 0.031632 sec) secondly I created another file using "seq -f "%09.0f" 100000000 10001000
> input.txt" which was an already sorted txt file the value for this one was 15. (2. Time: 0.0358
2 sec) lastly was a reversed version of the second txt file, a reverse sorted list of numbers.
this one took longer with the value being 50 (3. Time: 0.049891 sec). with these I did increments
of 5 to the Mo3 value to get those results. Because of the difference in lines I used math to
calculate a number 50+45+15 = 110/3 -> 36.66666667 rounded this down to 35. when tested I got
real	0m0.138s
user	0m0.117s
sys	0m0.021s which was better overall when I had it set to 30 so I feel like I made the right
choice keeping it up here because of the difference from the random to the sorted list I wanted to
make sure it didn't get too hindered on either test. I did use helpfrom the stem center to create
a file similar to the p3.py file but with the time library/module.
