import urllib

def read_text():
    open_file=open("F:\Quotes.txt")
    read_file=open_file.read()
    print(read_file)
    open_file.close()
    slang_check(read_file)
def slang_check(check_slang):
    connection=urllib.urlopen("http://www.purgomalum.com/service/xml?text="+check_slang)
    output = connection.read()
    print (output)
    connection.close()

read_text()
