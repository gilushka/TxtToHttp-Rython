def sql_add():
    sql_command = ["select", "from", 'where', 'join', 'and']
    fw = file_open("sql")
    file_string = fr.readline()
    fw.write('\n<p class="sql-q">')
    while file_string != '':
        for word in sql_command:
            if word in file_string:
                file_string = file_string.replace(word, '<span class="sql_com">' + word.upper() + "</span>")
        file_string = file_string.replace("\n", "</br>\n")
        fw.write(file_string)
        file_string = fr.readline().lower()
    fw.write("</p>")
    return

def file_open(name):
    return open("C:\\Users\\user.MGEKALO\\Desktop\\MarkPage\\" + name + ".html", 'a')

def file_close():
    return

if __name__ == '__main__':
    fr = open("C:\\Users\\user.MGEKALO\\Desktop\\MarkPage\\in.txt", 'r')
#    fw = open("C:\\Users\\user.MGEKALO\\Desktop\\MarkPage\\out.html", 'a')
#    sql_command = ["select", "from", 'where', 'join', 'and']
    json_command = []

    file_string = fr.readline().lower()
    if file_string.startswith("select"):
        sql_add()

    else:
        file_open("json")


    fr.close()
    fw.close()





"""    
fw.write(
'<html lang="ru">\n\
	<head>\n\
		<meta http-equiv="Content-Type" content="text/html" />\n\
		<link href="style.css" rel="stylesheet">\n\
	</head>\n')
            if word not in s:
                s = "\t" + s	
"""




