import csv
import os
from datetime import datetime

class imovel:
    def __init__(self,tipo,quartos):
        self.tipo = tipo
        self.quartos = quartos

    def cal_alu(self):
        if self.tipo=='apartamento':
            return 700
        elif self.tipo=='casa':
            return 900
        elif self.tipo =='estudio':
            return 1200

    def cal_add_quartos(self):
        if self.tipo == 'apartamento' and self.quartos == 2:
            return 200
        elif self.tipo == 'casa' and self.quartos == 2:
            return 250
        else:
            return 0

    def cal_garagem(self,vagas):
        if self.tipo == 'apartamento' or self.tipo =='casa':
            if vagas ==1:
                return 300
            else:
                return 0
        elif self.tipo == 'estudio':
            if vagas== 0:
                return 0
            elif vagas <= 2:
                return 250
            else:
                return 250 + (vagas - 2) *60

    def cal_desconto(self, valor_aluguel, tem_criancas):
        if self.tipo == 'apartamento' and tem_criancas == False:
            return valor_aluguel * 0.05
        else:
            return 0

    def cal_total(self, vagas, tem_criancas):
        aluguel= self.cal_alu()
        adicional_quartos= self.cal_add_quartos()
        adicional_garagem= self.cal_garagem(vagas)
        valor_aluguel = aluguel + adicional_quartos + adicional_garagem
        desconto = self.cal_desconto(valor_aluguel, tem_criancas)
        total= valor_aluguel - desconto
        return total

class orcamento:
    def __init__(self, imovel, parcelas):
        self.taxa_contra=2000
        self.imovel = imovel
        if parcelas >= 1 and parcelas <= 5:
            self.parcelas = parcelas
        else:
            self.parcelas =1
            print('Quantidade de parcelas inválida. Foi selecionado apenas 1 parcela.')

    def cal_parcelas(self):
        return self.taxa_contra / self.parcelas

    def gerar_csv(self, valor_aluguel, add_quartos, valor_garagem, desconto):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"RentSmart_Projecao12meses_{data_hora}.csv"
        caminho_completo = os.path.join(pasta_atual, nome_arquivo)
        contador = 1

        while os.path.exists(caminho_completo):
            nome_arquivo = f"RentSmart_Projecao12meses_{data_hora}_{contador}.csv"
            caminho_completo = os.path.join(pasta_atual, nome_arquivo)
            contador +=1

        with open(caminho_completo, 'x', newline='', encoding='utf-8-sig') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerow([
                'Mês',
                'Aluguel Base (R$)',
                'Adicional quartos (R$)',
                'Garagem (R$)',
                'Desconto (R$)',
                'Taxa contratual (R$)',
                'Total previsto (R$)'
            ])
            valor_parcela = round(self.cal_parcelas(), 2)
            for mes in range(1, 13):

                if mes < self.parcelas:
                    taxa_mes = valor_parcela

                elif mes == self.parcelas:
                    taxa_mes = round(
                        self.taxa_contra - valor_parcela * (self.parcelas - 1), 2
                    )

                else:
                    taxa_mes =0

                total = round(valor_aluguel + add_quartos + valor_garagem - desconto + taxa_mes, 2)
                escritor.writerow([
                    mes,
                    f"{valor_aluguel:.2f}",
                    f"{add_quartos:.2f}",
                    f"{valor_garagem:.2f}",
                    f"{desconto:.2f}",
                    f"{taxa_mes:.2f}",
                    f"{total:.2f}"
                ])
        print(f"\nArquivo '{caminho_completo}' gerado com sucesso!")