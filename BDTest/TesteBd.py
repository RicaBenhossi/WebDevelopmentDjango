import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'bruce')
con.select_db('calangcoach')

con_bd = con.cursor()

# estado = str(input('Digite o Estado: '))
# sigla = str(input('Digite a UF do estado: ')).upper()
# salvar = str(input('Deseja salvar os dados? (S/N)')).upper()
# if (salvar == 'S'):
#     # cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))
#     conection.execute('insert into estados (dcrEstado, dcrUF) values (%s,%s);', (estado, sigla))
#     con.commit()
#     conection.execute('select * from estados;')
#     print(list(conection))

con_bd.execute('select * from estados')
print(list(con_bd))
# busca uma linha ou;
print(con_bd.fetchone())
# busca todas as linhas ou;
print(con_bd.fetchone())
print(con_bd.fetchall())

# con_bd.execute('delete from estados where dcrUF = %s', ('AC',))
# con.commit()
