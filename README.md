# 🏷️ Label Sheet Maker

*Read this in [English](#english-version) | Leia em [Português](#versão-em-português)*

---

### 📋 Sobre o Projeto

Uma ferramenta simples e eficiente para gerar PDFs com múltiplas imagens/logos organizados em grade, otimizando o aproveitamento de folhas A4 para impressão de etiquetas.

**O problema:** Ajustar manualmente imagens em editores para imprimir múltiplas etiquetas por folha é demorado e frustrante.

**A solução:** Este script calcula automaticamente quantas imagens cabem em uma folha A4, considerando margens e espaçamento, e gera um PDF pronto para impressão.

### ✨ Funcionalidades

- ✅ Redimensiona imagens para tamanho específico (padrão: 4x4 cm)
- ✅ Calcula automaticamente o máximo de etiquetas por página
- ✅ Configura margens e espaçamentos personalizáveis
- ✅ Gera PDF otimizado para impressão
- ✅ Sem necessidade de upload para nuvem (roda local)

### 🚀 Como Usar

#### Requisitos

```bash
pip install reportlab Pillow
```

#### Uso Básico

1. Coloque sua imagem na pasta do projeto com o nome `image.png`
2. Execute o script:

```bash
python index.py
```

3. O PDF será gerado como `imagem_4x4.pdf`

#### Personalização

Edite a função `logo_pdf_generator()` para ajustar:

```python
logo_pdf_generator(
    imagem_path="your_logo.png",  # Caminho da sua imagem
    saida_pdf="labels.pdf"     # Nome do arquivo de saída
)
```

Para alterar dimensões, margens e espaçamento, edite as variáveis no código:

```python
img_w, img_h = 4 * cm, 4 * cm  # Tamanho da etiqueta
margin = 1 * cm                 # Margem da página
spacing = 0.5 * cm              # Espaçamento entre etiquetas
```

### 🎯 Casos de Uso

- Etiquetas para produtos
- Adesivos personalizados
- Logos para embalagens
- Tags para eventos
- Impressão de fotos em tamanho uniforme

### 🛠️ Tecnologias

- **Python 3.x**
- **ReportLab** - Geração de PDFs
- **Pillow (PIL)** - Processamento de imagens

### 📝 História do Projeto

Este projeto nasceu de uma necessidade real: otimizar a impressão de etiquetas para uma pequena fábrica de pipocas gourmet. O que antes levava tempo em ajustes manuais, agora leva segundos.

**A melhor parte da programação é ver ela facilitando a vida real.** 🍿

### 🤝 Contribuições

Sugestões, melhorias e pull requests são muito bem-vindos! Este é um projeto open source feito para a comunidade.

### 📄 Licença

MIT License - sinta-se livre para usar e modificar.

---

## English Version

### 📋 About the Project

A simple and efficient tool to generate PDFs with multiple images/logos organized in a grid, optimizing A4 sheet usage for label printing.

**The problem:** Manually adjusting images in editors to print multiple labels per sheet is time-consuming and frustrating.

**The solution:** This script automatically calculates how many images fit on an A4 sheet, considering margins and spacing, and generates a print-ready PDF.

### ✨ Features

- ✅ Resizes images to specific dimensions (default: 4x4 cm)
- ✅ Automatically calculates maximum labels per page
- ✅ Customizable margins and spacing
- ✅ Generates print-optimized PDF
- ✅ No cloud upload needed (runs locally)

### 🚀 How to Use

#### Requirements

```bash
pip install reportlab Pillow
```

#### Basic Usage

1. Place your image in the project folder named `image.png`
2. Run the script:

```bash
python index.py
```

3. The PDF will be generated as `imagem_4x4.pdf`

#### Customization

Edit the `logo_pdf_generator()` function to adjust:

```python
logo_pdf_generator(
    imagem_path="your_logo.png",  # Your image path
    saida_pdf="labels.pdf"         # Output file name
)
```

To change dimensions, margins, and spacing, edit the variables in the code:

```python
img_w, img_h = 4 * cm, 4 * cm  # Label size
margin = 1 * cm                 # Page margin
spacing = 0.5 * cm              # Spacing between labels
```

### 🎯 Use Cases

- Product labels
- Custom stickers
- Packaging logos
- Event tags
- Uniform-sized photo printing

### 🛠️ Technologies

- **Python 3.x**
- **ReportLab** - PDF generation
- **Pillow (PIL)** - Image processing

### 📝 Project Story

This project was born from a real need: optimizing label printing for a small gourmet popcorn factory. What used to take time in manual adjustments now takes seconds.

**The best part of programming is seeing it make real life easier.** 🍿

### 🤝 Contributing

Suggestions, improvements, and pull requests are very welcome! This is an open source project made for the community.

### 📄 License

MIT License - feel free to use and modify.

---

**Made with ❤️ to solve real problems**