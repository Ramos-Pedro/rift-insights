# Rift Insights

## Navigation

- [Português](#português)
- [English](#english)

---

## Português

### Visão Geral

O Rift Insights é uma aplicação desenvolvida em Python que consome dados da API oficial da Riot Games para analisar o desempenho de jogadores em partidas ranqueadas de League of Legends.

O objetivo do projeto é transformar dados brutos de partidas em insights estratégicos, permitindo que jogadores compreendam melhor sua performance, identifiquem padrões de vitória e derrota e tomem decisões mais eficientes dentro do jogo.

---

### Problema

Jogadores de League of Legends frequentemente não possuem uma visão clara e consolidada sobre:

- Seu desempenho ao longo do tempo  
- Quais campeões apresentam melhores resultados  
- Quais matchups são mais desfavoráveis  
- Quais composições de time aumentam suas chances de vitória  

Ferramentas existentes fornecem estatísticas básicas, mas carecem de análises mais profundas e personalizadas.

---

### Solução Proposta

Desenvolver uma ferramenta capaz de:

- Coletar automaticamente dados de partidas via API  
- Processar e estruturar essas informações  
- Gerar análises avançadas sobre desempenho  
- Apresentar insights claros e acionáveis ao jogador  

---

### Funcionalidades

#### Coleta de Dados

- Consulta de jogador pelo nome de invocador (Summoner Name)  
- Coleta de partidas recentes  
- Extração de métricas como:
  - Gold por minuto  
  - Dano por minuto  
  - Vision score  
  - Campeões aliados e inimigos  
  - Resultado da partida (vitória/derrota)  

---

#### Análise de Performance

- Winrate geral e por campeão  
- KDA médio  
- Desempenho por rota (Top, Jungle, Mid, ADC, Support)  

---

#### Análise de Matchups (Inimigos)

- Identificação de campeões contra os quais o jogador possui menor taxa de vitória  
- Análise segmentada por rota  

---

#### Análise de Sinergia (Aliados)

- Identificação de campeões aliados que aumentam a taxa de vitória  
- Avaliação de composições mais eficientes  

---

#### Classificação de Campeões

Sistema próprio de categorização de campeões com base em estilo de jogo:

- Hyper Carry (late game)  
- Early Game (snowball)  
- Tank / Engage  
- Mago de controle  
- Mago de artilharia  
- AD Caster  

---

#### Análise de Estilo do Jogador

- Identificação do estilo de jogo predominante  
- Sugestão de classes de campeões mais eficientes para o jogador  

---

#### Análise de Sinergia por Classe

- Identificação de categorias de aliados que aumentam a taxa de vitória  

---

#### Análise de Fraquezas

- Identificação de classes de campeões que representam maior dificuldade  

---

#### Sistema de Tracking de PDL (Estimado)

- Monitoramento da variação de LP entre partidas  
- Cálculo estimado de ganho/perda de LP  
- Projeção de evolução de elo com base no desempenho atual  

---

### Arquitetura do Sistema
[ Riot API ]
↓
[ Data Collector ]
↓
[ Data Processor ]
↓
[ Analytics Engine ]
↓
[ Insight Generator ]
↓
[ Dashboard / Interface ]

---

### Limitações

- A API da Riot Games não fornece dados de PDL por partida (estimativas são calculadas)  
- Classificação de campeões é baseada em regras definidas manualmente  
- Identificação de matchups por rota pode exigir heurísticas  
  - A API não fornece diretamente o adversário de rota  
  - O sistema infere o oponente com base em campeões e roles  

---

### Próximos Passos

- Implementação de modelos preditivos (Machine Learning)  
- Expansão do sistema de classificação de campeões  
- Deploy em ambiente cloud  
- Interface mais interativa  

---
### Time

Pedro Ribeiro Ramos – Lead Developer  
Bruno Amin Galvão – Technical Advisor 

## English

### Overview

Rift Insights is a Python application that consumes data from the Riot Games official API to analyze player performance in ranked League of Legends matches.

The goal of this project is to transform raw match data into strategic insights, helping players better understand their performance, identify win/loss patterns, and make better in-game decisions.

---

### Problem

League of Legends players often lack a clear and consolidated view of:

- Their performance over time  
- Which champions yield better results  
- Which matchups are unfavorable  
- Which team compositions increase win probability  

Existing tools provide basic statistics but lack deeper and personalized analysis.

---

### Proposed Solution

Develop a tool capable of:

- Automatically collecting match data via API  
- Processing and structuring this data  
- Generating advanced performance analytics  
- Providing clear and actionable insights  

---

### Features

#### Data Collection

- Player lookup using Summoner Name  
- Retrieval of recent matches  
- Extraction of metrics such as:
  - Gold per minute  
  - Damage per minute  
  - Vision score  
  - Allied and enemy champions  
  - Match result (win/loss)  

---

#### Performance Analysis

- Overall and per-champion winrate  
- Average KDA  
- Performance by role (Top, Jungle, Mid, ADC, Support)  

---

#### Matchup Analysis (Enemies)

- Identification of champions against which the player has the lowest winrate  
- Role-based analysis  

---

#### Synergy Analysis (Allies)

- Identification of allied champions that increase winrate  
- Evaluation of effective team compositions  

---

#### Champion Classification

Custom system to categorize champions based on playstyle:

- Hyper Carry (late game)  
- Early Game (snowball)  
- Tank / Engage  
- Control Mage  
- Artillery Mage  
- AD Caster  

---

#### Player Playstyle Analysis

- Identification of the player's predominant playstyle  

---

#### Class-Based Synergy Analysis

- Identification of ally categories that improve winrate  

---

#### Weakness Analysis

- Identification of champion classes that pose greater difficulty  

---

#### Estimated LP Tracking System

- Tracking LP variation between matches  
- Estimation of LP gains/losses  
- Projection of rank progression based on current performance  

---

### System Architecture
[ Riot API ]
↓
[ Data Collector ]
↓
[ Data Processor ]
↓
[ Analytics Engine ]
↓
[ Insight Generator ]
↓
[ Dashboard / Interface ]

---

### Limitations

- The Riot Games API does not provide LP gain/loss per match (values are estimated)  
- Champion classification is based on manually defined rules  
- Matchup identification relies on heuristics  
  - The API does not provide lane opponents directly  
  - The system infers opponents based on champions and roles  

---

### Team

Pedro Ribeiro Ramos – Lead Developer  
Bruno Amin Galvão – Technical Advisor 

