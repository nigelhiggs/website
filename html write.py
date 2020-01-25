from dominate.tags import *

#print(html(body(h1("hello world"))))

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
            for x in range(10):
                z=tr()
                
                z.add(td('first name'))
                z.add(td('last name'))
                z.add(td('age'))
            
print(h)
