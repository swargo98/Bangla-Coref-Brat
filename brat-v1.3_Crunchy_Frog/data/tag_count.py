import os
bookname = "Chapter3"
filename = "tag_count"
fw = open(filename,"w")
fw.write("chapter" + "\t" + "PRON_PER" + "\t" + "PROP_PER" + "\t" + "NOM_PER" + "\t" + "relational token\n")
for file in os.listdir(bookname):
    pron_per = 0
    prop_per = 0
    nom_per = 0
    relational_token = 0
    if file.endswith(".ann"):
        print(file)
        path_file = os.path.join(bookname, file)
        with open(path_file, "r") as f:
            while True:
                line  = f.readline()
                if not line:
                    break
                # print(line)
                tag = line.split('\t')[1].split(' ')[0]
                if tag == "PRON_PER":
                    pron_per+=1
                elif tag == "PROP_PER":
                    prop_per+=1
                elif tag == "NOM_PER":
                    nom_per+=1
                else:
                    relational_token+=1
            
            
            fw.write(file + "\t" + str(pron_per) + "\t" + str(prop_per) + "\t" + str(nom_per)+ "\t" + str(relational_token) + "\n")
fw.close()           
            
