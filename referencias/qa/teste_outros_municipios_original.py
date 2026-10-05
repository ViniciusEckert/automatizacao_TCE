"""QA exploratório: testa o importador e o comparador salarial com estruturas
de OUTROS municípios (não Cafezal do Sul), para verificar se o sistema
generaliza ou se está implicitamente amarrado ao formato de Cafezal.
"""
import sys, traceback
sys.path.insert(0, "/home/claude/projeto/projeto_jornada_magisterio")

from src.salarial.documento_service import extrair_tabela_salarial_texto
from src.salarial.analise_service import analisar_tabela_salarial


def caso(nome, funcao):
    print(f"\n=== {nome} ===")
    try:
        resultado = funcao()
        print("OK ->", resultado if not isinstance(resultado, dict) else "sucesso (dict retornado)")
        return resultado
    except Exception as e:
        print(f"FALHOU: {type(e).__name__}: {e}")
        return None


# ---------------------------------------------------------------
# CASO 1 — Município que usa "Nível I, II, III..." (numeração romana),
# muito comum no Paraná, em vez de letras A, B, C (usado por Cafezal).
# ---------------------------------------------------------------
TEXTO_ROMANOS = """
Anexo Único da LC 010/2024
Nível I - Ensino Médio Magistério 2.400,00 2.448,00 2.496,96
Nível II - Licenciatura Curta 2.640,00 2.692,80 2.746,66
Nível III - Licenciatura Plena 3.000,00 3.060,00 3.121,20
Percentual entre classes = 2,00%
Nível II = Nível I acrescido de 10,00%
Nível III = Nível I acrescido de 25,00%
"""

def caso1():
    return extrair_tabela_salarial_texto(TEXTO_ROMANOS, "anexo_outro_municipio.docx")

caso("1) Níveis em algarismos romanos (Nível I/II/III)", caso1)


# ---------------------------------------------------------------
# CASO 2 — Município cuja lei descreve a progressão com outra redação
# ("interstício"), semanticamente idêntica, mas texto diferente.
# ---------------------------------------------------------------
TEXTO_INTERSTICIO = """
Lei Municipal 1.234/2023 - Plano de Carreira do Magistério
Nível A - Professor 2.400,00 2.520,00 2.646,00
Nível B - Professor Licenciado 2.640,00 2.772,00 2.910,60
Interstício de 5% entre classes.
Nível B corresponde ao Nível A acrescido de 10%.
"""

def caso2():
    return extrair_tabela_salarial_texto(TEXTO_INTERSTICIO, "anexo_interssticio.docx")

caso("2) Progressão descrita como 'interstício' em vez de 'Percentual entre classes ='", caso2)


# ---------------------------------------------------------------
# CASO 3 — Tabela estruturada (JSON) de um município real cuja lei usa
# progressão NÃO uniforme entre classes (comum: primeiros interstícios
# menores, depois maiores). A tabela é matematicamente consistente com
# a própria lei, mas o sistema assume progressão uniforme.
# ---------------------------------------------------------------
def caso3():
    dados = {
        "municipio": "Município Exemplo B",
        "uf": "PR",
        "ano": 2026,
        "lei": "LC 020/2026",
        "arquivo_fonte": "anexo_b.pdf",
        "jornada_semanal": 20,
        "piso_nacional_40h": "5130.63",
        "progressao_classes_percentual": "5.00",  # só é possível declarar UM valor
        "modo_arredondamento": "truncar",
        "niveis": [
            {
                "codigo": "A",
                "descricao": "Magistério",
                "acrescimo_percentual": 0,
                # progressão real da lei: 5%, 5%, 10%, 10% (não uniforme)
                "valores": ["2565.31", "2693.57", "2828.24", "3111.06", "3422.16"],
            }
        ],
    }
    return analisar_tabela_salarial(dados)

resultado3 = caso("3) Progressão não uniforme entre classes (5%,5%,10%,10%) mas válida pela lei do município", caso3)
if resultado3:
    print("divergencias_estrutura encontradas:", resultado3["resumo"]["divergencias_estrutura"])
    print(resultado3["inconsistencias_estrutura"])


# ---------------------------------------------------------------
# CASO 4 — Município cujo acréscimo vertical é dado por valor fixo em R$
# (não percentual), estrutura comum em planos de carreira mais antigos.
# ---------------------------------------------------------------
def caso4():
    dados = {
        "municipio": "Município Exemplo C",
        "uf": "PR",
        "ano": 2026,
        "lei": "LC 005/2020",
        "arquivo_fonte": "anexo_c.pdf",
        "jornada_semanal": 20,
        "piso_nacional_40h": "5130.63",
        "progressao_classes_percentual": "2.00",
        "modo_arredondamento": "truncar",
        "niveis": [
            {"codigo": "A", "descricao": "Nível A", "acrescimo_percentual": 0,
             "valores": ["2565.31", "2616.61", "2668.94"]},
            {"codigo": "B", "descricao": "Nível B (A + R$ 300,00 fixos)", "acrescimo_percentual": 0,
             # acréscimo é um valor fixo em R$, não percentual -> usuário não tem como
             # representar isso no campo acrescimo_percentual
             "valores": ["2865.31", "2922.61", "2981.06"]},
        ],
    }
    return analisar_tabela_salarial(dados)

resultado4 = caso("4) Acréscimo vertical fixo em R$ (não percentual) declarado como acrescimo_percentual=0", caso4)
if resultado4:
    print("divergencias_estrutura encontradas:", resultado4["resumo"]["divergencias_estrutura"])
    print(resultado4["inconsistencias_estrutura"][:2])
