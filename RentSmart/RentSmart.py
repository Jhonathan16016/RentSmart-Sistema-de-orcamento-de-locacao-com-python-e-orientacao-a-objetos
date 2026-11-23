from imoveis import imovel,orcamento
import os
import csv

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('RentSmart'.center(30, '='))
    print('')
    print('Selecione um imóvel para orçamento ')
    print('Cada imóvel tem uma taxa contratutal de R$ 2000,00')
    print(""" 
    1- Casa
    2- Apartamento
    3- Estúdio
    4- Sair
    """)
    imo=input('Opção: ')
    if imo == '1':
        tipo_imo = 'casa'
        print('Deseja o imóvel com dois quartos? S(SIM) / N(NÃO) - (1 QUARTO)')
        quartos = input('Opção: ').upper()
        if quartos == 'S':
            quartos_quanti = 2
        elif quartos == 'N':
            quartos_quanti = 0
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')   
            continue 
        meu_imovel = imovel(tipo_imo,quartos_quanti)
        print('Deseja uma vaga para o imóvel? (S)SIM / (N)NÃO')
        vagas = input('Opção: ').upper()
        if vagas == 'S':
            vagas_quanti = 1
        elif vagas == 'N':
            vagas_quanti = 0
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue      
        try:    
            parcelas = int(input("Em quantas vezes deseja pagar a taxa contratual de R$2000,00? (1 a 5): "))
            if parcelas <1 or parcelas >5:
                print('Quantidade inválida')
                input('Clique enter para retornar...')
                continue
        except ValueError:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        meu_orcamento = orcamento(meu_imovel, parcelas)
        valor_garagem = meu_imovel.cal_garagem(vagas_quanti)
        valor_final = meu_imovel.cal_total(vagas_quanti,False)
        aluguel = meu_imovel.cal_alu()
        add_quartos = meu_imovel.cal_add_quartos()
        tem_crianca = False
        desconto = meu_imovel.cal_desconto(
        aluguel + add_quartos + valor_garagem, tem_crianca
        )
        print('')
        print('RESUMO DO ORÇAMENTO'.center(30, '='))
        print("Aluguel mensal (base): R$", meu_imovel.cal_alu())
        print("Adicional dos quartos: R$", meu_imovel.cal_add_quartos())
        print("Valor da vaga: R$",meu_imovel.cal_garagem(vagas_quanti))
        print("Taxa contratual: R$", meu_orcamento.taxa_contra)
        print("Quantidade de parcelas:", meu_orcamento.parcelas)
        print("Valor de cada parcela: R$", round(meu_orcamento.cal_parcelas(),2))
        print("Aluguel mensal final: R$", valor_final)
        print('')
        meu_orcamento.gerar_csv(aluguel, add_quartos, valor_garagem, desconto)
        input('Clique enter para retornar...')
    elif imo == '2':
        tipo_imo = 'apartamento'
        print('Deseja o imóvel com dois quartos? S(SIM) / N(NÃO) - (1 QUARTO)')
        quartos = input('Opção: ').upper()
        if quartos == 'S':
            quartos_quanti = 2
        elif quartos == 'N':
            quartos_quanti = 0
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue    
        meu_imovel = imovel(tipo_imo,quartos_quanti)
        print('Deseja uma vaga para o imóvel? (S)SIM / (N)NÃO')
        vagas = input('Opção: ').upper()
        if vagas == 'S':
                   vagas_quanti = 1
        elif vagas == 'N':
                   vagas_quanti = 0
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        print('Possui crianças? (S)SIM / (N)NÃO')
        criancas = input('Opção: ').upper()
        if criancas == 'S':
            tem_crianca = True
        elif criancas == 'N':
            tem_crianca = False
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        try:    
            parcelas = int(input("Em quantas vezes deseja pagar a taxa contratual de R$2000,00? (1 a 5): "))
            if parcelas <1 or parcelas >5:
                print('Quantidade inválida')
                input('Clique enter para retornar...')
                continue
        except ValueError:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        meu_orcamento = orcamento(meu_imovel, parcelas)
        valor_garagem = meu_imovel.cal_garagem(vagas_quanti)
        valor_final = meu_imovel.cal_total(vagas_quanti,tem_crianca)
        aluguel = meu_imovel.cal_alu()
        add_quartos = meu_imovel.cal_add_quartos()
        desconto = meu_imovel.cal_desconto(
        aluguel + add_quartos + valor_garagem, tem_crianca
        )
        print('')
        print('RESUMO DO ORÇAMENTO'.center(30, '='))
        print("Aluguel mensal (base): R$", meu_imovel.cal_alu())
        print("Adicional dos quartos: R$", meu_imovel.cal_add_quartos())
        print("Valor da vaga: R$",meu_imovel.cal_garagem(vagas_quanti))
        print("Taxa contratual: R$", meu_orcamento.taxa_contra)
        print("Quantidade de parcelas:", meu_orcamento.parcelas)
        print("Valor de cada parcela: R$", round(meu_orcamento.cal_parcelas(),2))
        print("Desconto: R$", round(desconto, 2))
        print("Aluguel mensal final: R$", valor_final)
        print('')
        meu_orcamento.gerar_csv(aluguel, add_quartos, valor_garagem, desconto)
        input('Clique enter para retornar...')
    elif imo == '3':
        tipo_imo = 'estudio'
        meu_imovel = imovel(tipo_imo,0)
        print('Deseja uma vaga para o imóvel? (S)SIM / (N)NÃO')
        vagas = input('Opção: ').upper()
        if vagas == 'S':
            vaga = input('Deseja vagas adicionais? S(SIM) / N(NÃO)').upper()
            if vaga == 'S':
                print('Cada vaga adicional sai por R$ 60,00 ')
                try:
                    add= int(input('Quantas vagas adicionais?: '))
                    if add <0:
                        print('Quantidade inválida')
                        input('Clique enter para retornar...')
                        continue
                    vagas_quanti= 2 + add
                except ValueError:
                    print('Opção inválida')
                    input('Clique enter para retornar...')
                    continue
            elif vaga == 'N':
                vagas_quanti = 2
            else:
                print('Opção inválida')
                input('Clique enter para retornar...')
                continue
        elif vagas == 'N':
            vagas_quanti = 0
        else:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        try:    
            parcelas = int(input("Em quantas vezes deseja pagar a taxa contratual de R$2000,00? (1 a 5): "))
            if parcelas <1 or parcelas >5:
                print('Quantidade inválida')
                input('Clique enter para retornar...')
                continue
        except ValueError:
            print('Opção inválida')
            input('Clique enter para retornar...')
            continue
        meu_orcamento = orcamento(meu_imovel, parcelas)
        aluguel = meu_imovel.cal_alu()
        add_quartos = meu_imovel.cal_add_quartos()
        valor_garagem = meu_imovel.cal_garagem(vagas_quanti)
        desconto = 0
        valor_final = meu_imovel.cal_total(vagas_quanti,False)
        print('')
        print('RESUMO DO ORÇAMENTO'.center(30, '='))
        print("Aluguel mensal (base): R$", meu_imovel.cal_alu())
        print("Valor da vaga: R$",meu_imovel.cal_garagem(vagas_quanti))
        print("Taxa contratual: R$", meu_orcamento.taxa_contra)
        print("Quantidade de parcelas:", meu_orcamento.parcelas)
        print("Valor de cada parcela: R$", round(meu_orcamento.cal_parcelas(), 2))
        print("Aluguel mensal final: R$", valor_final)
        print('')
        meu_orcamento.gerar_csv(aluguel, add_quartos, valor_garagem, desconto)
        input('Clique enter para retornar...')
    elif imo =='4':
        break
    else:
        print('Opção inválida')
        input('Clique enter para retornar...')

