#Using Dictionaries As Indexes Solution

dict = {}
index_key = ('aa','bb','cc','dd')

def dict_change(dict1):
    for i in range(len(index_key)):
        dict1[index_key[i]] = i * 2
        
    return dict1
    
print dict_change(dict)
print dict

# this actually will add 'ww' = 121 to the dictionary
dict['ww'] = 121
print dict

#{'aa': 0, 'cc': 4, 'dd': 6, 'bb': 2}
#{'aa': 0, 'cc': 4, 'dd': 6, 'bb': 2}

print dict.get('dd')
print '==================='
dict['ww'] = 122
print dict
