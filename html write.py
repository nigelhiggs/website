from dominate.tags import *

#print(html(body(h1("hello world"))))

def table_create(first_names,last_names,pics):


    h = html()

    with h.add(body()).add(div(id='content')):
        h1('hello worlkd')
        p('lorem ispum')


        
        with table().add(tr()):
            l = th()
            l.add(th('one'))
            l.add(th('two'))
            l.add(th("three"))
            with table().add(tr()):
                for x in range(len(names)):
                    z=tr()
                    
                    z.add(td(str(first_names[x])))
                    z.add(td(str(last_names[x])))
                    
                    z.add(td(img(src = pics[x], width = "200", height = "250", alt="Inmate")))
                    #z.add(img(str(pics[x])))
                    
    print(h)

def name_list():
    container=[]


    f=open("D:/jail text files/fileresults.txt","r")
    #f opens the path to the txt folder and reads ("file.txt", "r")
    #f = open(path+"fileresults.txt","r")

    #mode confirms that the file is being read. 
    if f.mode == "r":
        contents = f.read()
        file_len=len(contents)
        
    #for loop that is reading the contents of "file.txt" and using the length of file to
    #determine how far it should loop.
        for x in range(file_len):
            file = contents[x]
            if file == '<':
                if contents[x+1] == 'a':
                    numbers = ""
                    
                    #print(contents[x+34])
                    for z in range(x+34,file_len):
                        if contents[z] =="<":
                            break
                        else:
                            numbers+=str(contents[z])
                    container.append(numbers)
    return container

def picture(names):

    container_pic=[]
    for x in range(len(names)):
        container_pic.append("Pictures/"+str(x)+".jpg")
    return container_pic

    

def first_name_container(names):

    
    first_name_container=[]
    for x in range(len(names)):
        first_name = ""
        parse = names[x]
        for y in range(len(parse)):
            if parse[y] ==',':
                first_name_container.append(first_name)
                break
            else:
                first_name+=parse[y]
        
    return first_name_container

    
def last_name_container(names):

    last_name_container=[]
    
    for z in range(len(names)):
        switch = 0
        last_name=""
        parse = names[z]
        
        for d in range(len(parse)):
            if parse[d]==',':
                switch = int(d)
                break
            else:
                continue
            
        for y in range(switch+1,len(parse)):
            last_name+=parse[y]
            
        last_name_container.append(last_name)
                
    return last_name_container



############################################################################################################

##this will be my main area.
name_list()

names = name_list()
first_name = first_name_container(names)

last_names = last_name_container(names)

pics = picture(names)

table_create(first_name,last_names,pics)

#z=open("C:/Users/nigel/Desktop/school/website/names.txt","r+")

#print(z.readline(3))






#table_create()
