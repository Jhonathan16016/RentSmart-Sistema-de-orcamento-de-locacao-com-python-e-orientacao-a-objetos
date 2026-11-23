
#RentSmart

### Sistema de elaboração de orçamentos de locação de imóveis

---

## Sobre o projeto

O RentSmart é um sistema desenvolvido em Python com o objetivo de auxiliar a R.M. Imóveis no processo de elaboração de orçamentos de locação. O projeto busca automatizar os cálculos dos aluguéis, tornando o processo mais rápido, organizado e reduzindo a possibilidade de erros.

O programa permite calcular valores de diferentes tipos de imóveis, considerando adicionais, descontos e taxas contratuais. Também gera um arquivo CSV com uma projeção financeira dos primeiros 12 meses de locação.

## Funcionalidades

- Seleção entre casa, apartamento e estúdio.
- Cálculo automático do aluguel-base.
- Cálculo de adicionais relacionados aos quartos.
- Cálculo dos valores de garagem.
- Aplicação de descontos conforme as regras de negócio.
- Parcelamento da taxa contratual em até 5 vezes.
- Exibição de um resumo detalhado do orçamento.
- Geração de arquivo CSV com projeção financeira de 12 meses.
- Validação das informações fornecidas pelo usuário.

## Regras de negócio

### Valores dos imóveis

Tipo de imóvel / Aluguel-base 
Casa: R$ 900,00 
Apartamento:  R$ 700,00 
Estúdio: R$ 1.200,00 

### Adicionais e descontos

Regra / Valor

Segundo quarto em casa + R$ 250,00 
Segundo quarto em apartamento + R$ 200,00 
Vaga em casa ou apartamento + R$ 300,00 
Pacote inicial de 2 vagas no estúdio - R$ 250,00 
Cada vaga adicional no estúdio + R$ 60,00 
Desconto em apartamento sem crianças - 5% 

### Taxa contratual

- Valor fixo de R$ 2.000,00.
- Parcelamento em até 5 vezes.

##  ecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- Arquivos CSV

## Estrutura do projeto

```text
RentSmart/
│
├── sistema.py
├── imoveis.py
└── README.md
```

- **sistema.py:** responsável pelo menu principal, recebimento das informações e interação com o usuário.
- **imoveis.py:** contém as classes responsáveis pelos cálculos dos imóveis, parcelamento da taxa contratual e geração do CSV.

## Como executar o projeto

**Pré-requisito:** ter o Python instalado no computador.

1. Clone ou baixe o repositório.
2. Abra a pasta do projeto no terminal ou no VS Code.
3. Execute o comando:

```bash
python sistema.py
```

4. Siga as opções apresentadas no menu para realizar um orçamento.

## Geração do arquivo CSV

Após a elaboração do orçamento, o sistema gera automaticamente um arquivo CSV contendo a projeção financeira dos primeiros 12 meses de locação.

O arquivo apresenta informações separadas, como aluguel-base, adicionais, garagem, descontos, taxa contratual e total previsto para cada mês.

## Objetivo acadêmico

O RentSmart foi desenvolvido como projeto acadêmico com o propósito de aplicar conhecimentos de lógica de programação, Python e Programação Orientada a Objetos na resolução de um problema prático.

---

**RentSmart - R.M. Imóveis**
