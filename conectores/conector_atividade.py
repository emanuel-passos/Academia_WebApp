import conectores.conector_plano as plano
from database.run_sql import run_sql
from Classes.atividade import Atividade
from Classes.Membro import Membro

def get_all():
    
    atividades = []
    
    sql = "SELECT * FROM webuser.TB_ATIVIDADES "
    results =run_sql(sql)
    
    for row in results:
        tipo_plano = plano.get_one(row["plano"])
        
        atividade = Atividade(row["nome"],
                                row["instrutor"],
                                row["data"],
                                row["duracao"],
                                row["capacidade"],
                                tipo_plano,
                                row["ativo"],
                                row["id"])
        
        atividades.append(atividade)
    
    return atividades

def get_members(id):
    
    membros = []
    
    sql = "SELECT membros.* FROM  webuser.TB_MEMBROS INNER JOIN webuser.TB_AGENDAMENTOS ON membros.id = webuser.TB_AGENDAMENTOS.membro WHERE webuser.TB_AGENDAMENTOS.atividade = %s"
    value = [id]
    
    result = run_sql(sql, value)
    
    for row in result:
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        row["tipo_plano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])
        
        membros.append(membro)
    
    return membros

def get_all_active():
    
    atividades = []
    
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE ativo = true ORDER BY data ASC"
    result = run_sql(sql)
    
    for row in result:
        
        tipo_plano = plano.get_one(row["plano"])
        
        atividade = Atividade(row["nome"],
                                row["instrutor"],
                                row["data"],
                                row["duracao"],
                                row["capacidade"],
                                tipo_plano,
                                row["ativo"],
                                row["id"])
        
        atividades.append(atividade)
    
    return atividades

def get_all_inactive():
    
    atividades = []
    
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE ativo = false ORDER BY data ASC"
    result = run_sql(sql)
    
    for row in result:
        
        tipo_plano = plano.get_one(row["plano"])
        
        atividade = Atividade(row["nome"],
                                row["instrutor"],
                                row["data"],
                                row["duracao"],
                                row["capacidade"],
                                tipo_plano,
                                row["ativo"],
                                row["id"])
        
        atividades.append(atividade)
    
    return atividades


def get_one(id):
    
    sql = "SELECT * FROM webuser.TB_INSTRUTORES WHERE ativo = true AND id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]
    
    if result is not None:
        tipo_plano = plano.get_one(result["plano"])
        
        atividade = Atividade(result["nome"],
                                result["instrutor"],
                                result["data"],
                                result["duracao"],
                                result["capacidade"],
                                tipo_plano,
                                result["ativo"],
                                result["id"])
    return atividade

def new(atividade):
    
    sql = "INSERT INTO webuser.TB_ATIVIDADES (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) VALUES (%s, %s, %s, %s, %s, %s, %s,) RETURNING *;"
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.tipo_plano, atividade.ativo]

    result = run_sql(sql, values)
    
    atividade.id = result[0]["id"]
    
    return atividade

def delete_one(id):
    
    sql = "DELETE FROM webuser.TB_ATIVIDADES WHERE id = %s"
    value = [id]
    
    run_sql(sql, value)
    
def edit(atividade):
    
    sql = "UPDATE webuser.TB_ATIVIDADES SET (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) = (%s, %s, %s, %s, %s, %s, %s,) WHERE id = %s; "
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.tipo_plano, atividade.ativo]

    run_sql(sql, values)
    
 
