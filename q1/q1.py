def search(pat, txt, i):
     outputname = "patternmatch"+str(i)+".txt"
     file = open(outputname, "w")
     lp = len(pat)               #length of pattern
     ls = len(txt)               #length of string
     flag = 0
     for i in range(ls-lp+1):
         j = 0
         while j < lp and (txt[i+j] == pat[j] or pat[j] == '_'):
             j+=1
             if j == lp:
                 flag = 1
                 f = open(outputname, "a")
                 f.write("A pattern found at position "+str(i))
                 f.write("\n")
                 break
     if flag == 0:
         f = open(outputname, "a")
         f.write("There is no substring that matching the pattern")

for i in range(1, 5):
    textname = "text"+str(i)+".txt"           #name of the text file
    patternname = "pattern"+str(i)+".txt"       #name of the pattern file
    

    text = open(textname, "r").read()           #open the string file and read the string
    pattern = open(patternname, "r").read()     #open the pattern file and read the pattern
    if not text or not pattern:                 #if pattern or string is empty write in 
        file = "patternmatch"+str(i)+".txt"     #output file name
        f = open(file, "w").write("empty pattern or text")
        continue
    search(pattern, text, i)
