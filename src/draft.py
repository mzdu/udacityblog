# This experiment proves that insert(index,item) is much faster than list concatenation.

from timeit import Timer


listInsert = Timer("x.insert(0,4)",
                "from __main__ import x")
listConc = Timer("x=[4]+x",
               "from __main__ import x")



print("insert() Concatenation")
for i in range(10000,1000001,10000):
    x = list(range(i))
    in1 = listInsert.timeit(number=1000)
    x = list(range(i))
    in2 = listConc.timeit(number=1000)

    
    print("%15.5f, %15.5f" %(in1,in2))
 
 
 """
 insert() Concatenation
        0.02579,         0.06255
        0.02078,         0.12232
        0.02868,         0.18239
        0.03865,         0.24140
        0.04952,         0.31012
        0.05783,         0.51143
        0.06829,         0.72902
        0.07755,         0.72720
        0.08572,         0.80986
        0.09598,         0.94011
        0.10729,         1.12687
 """   