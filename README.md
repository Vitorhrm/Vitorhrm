<div align="center">
  <img src="assets/hello.gif" width="900" alt="Olá, eu sou o Vitor. Java e Spring Boot, redes e automação, TCC e IoT em desenvolvimento.">
</div>

# Vitor Matias

**Backend Java · Automação de redes · Sistemas de Informação no IFMG**

Minha experiência em suporte e infraestrutura de telecomunicações inspira meus projetos. Uso Java e Spring Boot para explorar fluxos de atendimento e Python para automatizar tarefas de rede. No IFMG, desenvolvo um TCC sobre apoio à irrigação.

[![Explorar API Java](assets/api.svg)](https://github.com/Vitorhrm/spring-docker-app#api-de-chamados)
[![Abrir demo do Conexões SI](assets/demo.svg)](https://vitorhrm.github.io/SADtrab/)
[![LinkedIn](assets/linkedin.svg)](https://www.linkedin.com/in/vitor-hrm-matias/)

## Projetos em destaque

### ☕ API de chamados de suporte

API REST em **Java 17 e Spring Boot** com criação de chamados, regras de transição e histórico em memória. Os testes com MockMvc cobrem o fluxo HTTP, incluindo validação e transições inválidas.

[Ver API e exemplos](https://github.com/Vitorhrm/spring-docker-app#api-de-chamados) · [Executar com Docker](https://github.com/Vitorhrm/spring-docker-app#executar-com-docker) · [![Build e testes da API Java](https://github.com/Vitorhrm/spring-docker-app/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Vitorhrm/spring-docker-app/actions/workflows/ci.yml)

<details>
<summary>Experimente uma transição inválida</summary>

Crie um chamado e tente ir direto de `OPEN` para `RESOLVED`. A API deve retornar `409`. Em seguida, percorra `OPEN → IN_PROGRESS → RESOLVED` e confira o histórico.

</details>

### 🌱 AgroSense · TCC em desenvolvimento

Protótipo de apoio à irrigação com telemetria de uma estação **ESP32** e previsão do tempo por área. A validação das regras de recomendação de irrigação ainda está pendente.

[Ver arquitetura e andamento](https://github.com/Vitorhrm/Agrosense#arquitetura) · [Abrir versão web](https://agrosense-app.vercel.app/agro/)

<details>
<summary>Como a leitura chega ao aplicativo?</summary>

```mermaid
flowchart LR
    A[Estação ESP32] -->|LoRa| B[Receptor ESP32]
    B -->|HTTPS| C[API e banco]
    C --> D[Web e Android]
```

</details>

### 🐍 MAC-Fabricante

Automação em **Python** que identifica fabricantes pelo prefixo MAC/OUI em planilhas Excel. O cache local reaproveita resultados de consultas anteriores.

[Testar com a planilha de exemplo](https://github.com/Vitorhrm/MAC-Fabricante#experimentar-com-dados-fict%C3%ADcios)

## Mais projetos

- **Conexões SI** · Mapa interativo para explorar disciplinas e comparar caminhos de carreira em Sistemas de Informação. [Abrir demo](https://vitorhrm.github.io/SADtrab/) · [Ver código](https://github.com/Vitorhrm/SADtrab)
- **Mordix** · Protótipo acadêmico de delivery para Android com React Native, autenticação e catálogo demonstrativo. [Ver projeto](https://github.com/Vitorhrm/Mordix)

## Tecnologias

<p><img src="assets/stack.svg" width="480" alt="Java, Spring, Python, TypeScript, React, Docker, Git e Linux."></p>

## Atividade no GitHub

<details>
<summary>Ver estatísticas e linguagens</summary>

<p align="center">
  <img src="assets/stats.svg" width="49%" alt="Números públicos do perfil, atualizados diariamente.">
  <img src="assets/languages.svg" width="49%" alt="Distribuição por bytes de código em cinco projetos selecionados.">
</p>

Os cartões são atualizados diariamente com dados públicos do GitHub. O gráfico de linguagens usa o volume de código em cinco projetos selecionados.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pacman-contribution-graph-dark.svg">
  <img src="assets/pacman-contribution-graph.svg" width="900" alt="Pac-Man animado percorrendo minhas contribuições no GitHub.">
</picture>

## Contato

[LinkedIn](https://www.linkedin.com/in/vitor-hrm-matias/) · [E-mail](mailto:vitorhrm1@hotmail.com) · [Instagram](https://www.instagram.com/vitcs1/)

<sub>Ícones de <a href="https://github.com/tandpfun/skill-icons">Skill Icons</a>. Animação de <a href="https://github.com/abozanona/pacman-contribution-graph">Pacman Contribution Graph</a>.</sub>
