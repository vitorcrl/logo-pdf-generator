from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from PIL import Image

def logo_pdf_generator(imagem_path="your_logo.png", saida_pdf="labels.pdf"):
    img = Image.open(imagem_path)
    px_por_cm = 118
    nova_dim = (int(4 * px_por_cm), int(4 * px_por_cm))
    img_resized = img.resize(nova_dim)
    temp_img = "imagem.png"
    img_resized.save(temp_img)

    page_width, page_height = A4
    img_w, img_h = 4 * cm, 4 * cm
    margin = 1 * cm
    spacing = 0.5 * cm

    c = canvas.Canvas(saida_pdf, pagesize=A4)

    cols = int((page_width - 2 * margin + spacing) // (img_w + spacing))
    rows = int((page_height - 2 * margin + spacing) // (img_h + spacing))

    x_start = margin
    y_start = page_height - margin - img_h

    for row in range(rows):
        for col in range(cols):
            x = x_start + col * (img_w + spacing)
            y = y_start - row * (img_h + spacing)
            c.drawImage(temp_img, x, y, width=img_w, height=img_h)

    c.save()
    print(f"✅ PDF gerado com sucesso: {saida_pdf}")
    print(f"📄 {cols * rows} fotos 4x4 por página.")

if __name__ == "__main__":
    logo_pdf_generator()
