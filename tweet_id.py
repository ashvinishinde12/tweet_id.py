from collections import Counter
  
tweet_names =[]
for i in range(4):
    x=input("Enter the username and tweet id")
    tweet_names.insert(i,x)
    
print(tweet_names) 
uniq_names = [pref_names.split()[0] for
              pref_names in tweet_names]
  
times = Counter(uniq_names)
repeat = times.values()
  
for element in set(repeat):
    dupl = ([(key, value) for
             key, value in sorted(times.items()) if
             value == element])
      
    if len(dupl) > 1:
        for (key, value) in dupl:
            print (key,'',value)
    max_value = max(times.values())
    temp_max_result = [(key, value) for 
                       key, value in sorted(times.items()) if
                       value == max_value]
      
    if temp_max_result != dupl:
        for (key,value) in temp_max_result:
            print (key,'',value)
