"""Modelo de teste do projeto (unittest, sem internet).

Copie para tests/test_<assunto>.py e adapte. Padrões:
- cliente TCE falso devolvendo CSV sintético (ver tests/test_service.py);
- diretório temporário para qualquer gravação;
- um teste por regra, nomeado pelo comportamento esperado;
- inclua o caso de FALHA, não só o de sucesso.
"""
import tempfile
import unittest

from src.persistencia.arquivos import ArquivoBrutoStore
from src.services.analise_service import AnaliseService


class ClienteFalso:
    """Substitui TCEClient. Preencha com CSVs mínimos que reproduzam o rótulo real."""

    def coletar_relatorio_csv(self, municipio_id, entidade_id, relatorio_id, ano, periodo_id=None):
        raise NotImplementedError("Devolva o CSV sintético do relatório pedido.")


class ModeloDeTeste(unittest.TestCase):
    def test_comportamento_esperado_em_linguagem_clara(self):
        with tempfile.TemporaryDirectory() as pasta:
            servico = AnaliseService(ClienteFalso, raw_store=ArquivoBrutoStore(pasta), salvar_brutos=True)
            self.assertIsNotNone(servico)  # substitua por asserts sobre o resultado

    def test_falha_de_um_ano_nao_apaga_os_demais(self):
        """Regra DEC-013: erro isolado por exercício, preservado em erros[]."""
        self.skipTest("Exemplo: implemente com um cliente que falha em um único ano.")

    def test_valor_conferido_no_bruto(self):
        """Valores numéricos devem ser recalculados à mão a partir do CSV bruto."""
        self.skipTest("Exemplo: DTP / RCL ajustada x 100 contra o percentual publicado.")


if __name__ == "__main__":
    unittest.main()
