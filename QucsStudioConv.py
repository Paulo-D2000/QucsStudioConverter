import sys

def quitprogram():
     print("Usage: <input_file.sch> -v <output_version> -o <output_file_name>")
     quit()

def checkHeader(head):
    version = 0
    try:
        head.find("QucsStudio")
        for x in head:
            try:
                version = int(x)
                break;
            except:
                pass
        print("Found QucsStudio %d.x file!" % (version))
    except:
        print("Invalid QucsStudio file!")
        quitprogram()

if(len(sys.argv)<6):
    quitprogram()
else:
    #Open the desired file
    try:
        f = open(sys.argv[1], 'r')
    except:
        print("File not found!")
        quitprogram()

    #check the header
    header = f.readline()
    checkHeader(header)

    #check version
    try: 
        int(sys.argv[3][0]) #test if the version has integer part
    except:
        print("Invalid version format!")
        quitprogram()

    #check output name
    for i in sys.argv[5]:
        if(i == "."):
            print("Invalid output name! Please remove the \".\" and/or extension")
            quitprogram()

    #generate the temp file
    try:
        f1 = open(sys.argv[5]+".sch",'w')
        print("Creating Qucs %s file" %(sys.argv[3]))
    except:
        print("Cant create file %s" %(sys.argv[5]))
        quit()

    #change the header & version
    f1.write("<Qucs Schematic %s>\n" %(sys.argv[3]))

    #add the < and >
    for line in f:
        if  not ('<') in line:
            f1.write("<")
        if  not ('>') in line:
            f1.write(line.replace('\n', '>\n'))
        else:
            f1.write(line)

    f.close()
    f1.close()
    print("Done!\nFile: %s.sch saved!" % (sys.argv[5]))
