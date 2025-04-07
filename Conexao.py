from flask import Flask, render_template, request
import firebirdsql
app = Flask(__name__)

# Função para buscar dados no Firebird com filtros
def get_data_from_firebird(data_inicial=None, data_final=None, setor=None):
    conn = firebirdsql.connect(
        host='192.168.0.139',
        database='C:\\sgi\\database\\SGI.FDB',
        user='SYSDBA',
        password='masterkey'
    )

    cursor = conn.cursor()

    # Construção da query SQL com filtros opcionais
    sql = "SELECT DESTINO, COUNT(DESTINO) FROM VISITA WHERE 1=1"
    params = []

    if data_inicial:
        sql += " AND DT_VISITA >= ?"
        params.append(data_inicial)
    
    if data_final:
        sql += " AND DT_VISITA <= ?"
        params.append(data_final)
    
    if setor:
        sql += " AND DESTINO LIKE ?"
        params.append(f"%{setor}%")  # Busca parcial do setor

    sql += " GROUP BY DESTINO ORDER BY COUNT(DESTINO) DESC"

    cursor.execute(sql, params)  # Evita SQL Injection
    rows = cursor.fetchall()
    conn.close()
    return rows

# Função para buscar setores disponíveis no Firebird
def get_setores_from_firebird():
    conn = firebirdsql.connect(
        host='192.168.0.139',
        database='C:\\sgi\\database\\SGI.FDB',
        user='SYSDBA',
        password='masterkey'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT DESTINO FROM VISITA ORDER BY DESTINO")
    setores = [row[0] for row in cursor.fetchall()]
    conn.close()
    return setores

@app.route('/')
def index():
    data_inicial = request.args.get('data_inicial')
    data_final = request.args.get('data_final')
    setor = request.args.get('setor')  # Captura o setor selecionado no formulário
    
    # Obter a lista de setores disponíveis
    setores = get_setores_from_firebird()

    # Chama a função que busca os dados no banco Firebird
    data = get_data_from_firebird(data_inicial, data_final, setor)

    return render_template('index.html', data=data, setores=setores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
