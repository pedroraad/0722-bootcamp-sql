from csvms.table import Table

tbl = Table('lista_frutas').ᐅ(Table('tipo_frutas'), where={'eq':['lista_frutas.tp_fruta','tipo_frutas.tp_fruta']})
print(tbl)