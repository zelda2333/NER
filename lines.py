#!/usr/bin/env python
with open('/home/zelda/Documents/NER DOCUMENT/example.train','r') as f1:
    with open('orin_data.txt','w') as f2:
        for line in  f1.readlines()[0:65400]:
            f2.write(line)
#1-2 lines [0:2]
