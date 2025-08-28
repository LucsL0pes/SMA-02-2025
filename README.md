# SMA-02-2025

Este repositório contém um simulador simples de filas desenvolvido como parte da disciplina de Simulação.

## Uso

Execute o script Python para realizar as simulações das filas G/G/1/5 e G/G/2/5 usando 100.000 números aleatórios gerados pelo método congruente linear:

```bash
python3 queue_simulator.py
```

O resultado será apresentado no terminal, incluindo o tempo total de simulação, o número de clientes perdidos e a distribuição de probabilidade dos estados da fila para cada cenário.

## Resultados

Os resultados abaixo foram gerados executando o comando acima.

### G/G/1/5
- Tempo total de simulação: 186855.4943
- Clientes perdidos: 6583
- Probabilidades dos estados (0 a 5 clientes no sistema):
  - 0: 0.000011
  - 1: 0.000192
  - 2: 0.001486
  - 3: 0.043868
  - 4: 0.527517
  - 5: 0.426926

### G/G/2/5
- Tempo total de simulação: 175032.6715
- Clientes perdidos: 0
- Probabilidades dos estados (0 a 5 clientes no sistema):
  - 0: 0.063087
  - 1: 0.729917
  - 2: 0.206328
  - 3: 0.000668
  - 4: 0.000000
  - 5: 0.000000
