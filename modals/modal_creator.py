

for x in range(0, 45):  
    file = open(str(x) + ".html", 'a')
    file.write("<div class=\"modal_div\">\n")
    file.write("    <img src='" + str(x) + ".png'/>\n")
    file.write("</div>")
    file.close()

