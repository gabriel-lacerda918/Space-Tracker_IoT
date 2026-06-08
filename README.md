# SpaceDebris Monitor Pro

## Descrição da Solução

O Space Tracker é uma aplicação de Visão Computacional desenvolvida em Python que utiliza a webcam do computador para capturar vídeo em tempo real e realizar a detecção de objetos através do modelo YOLOv8.

Após detectar os objetos presentes na imagem, o sistema estima a distância entre o objeto e a câmera utilizando técnicas de processamento de imagem e parâmetros de calibração previamente definidos.

A solução simula aplicações utilizadas em sistemas de monitoramento espacial, observação terrestre por satélites e identificação de detritos espaciais, permitindo a análise visual automática de elementos presentes no ambiente.

---

## Bibliotecas Utilizadas

- OpenCV
- NumPy
- Ultralytics (YOLOv8)

---

## Estrutura do Projeto

```text
SpaceDebrisMonitor_Pro/
│
├── src/
│   └── main.py
│
├── requirements.txt
│
└── README.md
```

---

## Instalação das Dependências

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd SpaceDebrisMonitor_Pro
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute o sistema através do comando:

```bash
python src/main.py
```

Ao iniciar, a webcam será ativada automaticamente.

Para encerrar a aplicação, pressione:

```text
Q
```

---

## Funcionalidades

- Captura de vídeo em tempo real;
- Detecção automática de objetos utilizando YOLOv8;
- Identificação da classe do objeto detectado;
- Estimativa da distância entre objeto e câmera;
- Exibição das informações diretamente na tela;
- Aplicação prática de Visão Computacional utilizando webcam.

---

## Integrantes

- Gabriel Machado Lacerda – RM 556714 - 3ESPW - FIAP

---

## Requisitos do Sistema

- Python 3.10 ou superior
- Webcam funcional
- Sistema Operacional Windows, Linux ou macOS
