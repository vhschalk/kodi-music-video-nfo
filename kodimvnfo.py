import os
from os import walk

def mvnfo(directory):
    # walk the tree
    for root, directories, files in os.walk(directory):
        for filename in files:
            a = filename.find("-")
            s = filename.find("(")
            m = filename.rfind(".")
            if s < 0:
                s = len(filename)
                info = ""
                year = ""
                s = m+1
            else:
                info = filename[s+1:m-1]

                date = [int(d) for d in info.split() if d.isdigit()]
                if len(date) > 0:
                    date.sort(reverse=True)
                    if date[0] >= 100000: #yymmdd
                        year = "20" + str(date[0])[0:2]
                    elif date[0] >= 1000: #yyyy
                        year = str(date[0])
                else:
                    year = ""

            if a > 0:
                artist = filename[0:a-1]
                song = filename[a+2:s-1]

                f = open(root + '/' + filename[0:m] + '.nfo',"w")
                f.write("<musicvideo>\n")
                f.write("<title>" + song + "</title>\n")
                f.write("<artist>" + artist + "</artist>\n")
                f.write("<year>" + year + "</year>\n")
                f.write("<plot>" + info + "</plot>\n")
                f.write("</musicvideo>")
                f.close()
                print(filename[0:m] + '.nfo ' + year)

mypath = "D:\Videos\MK Videos"

mvnfo(mypath)
