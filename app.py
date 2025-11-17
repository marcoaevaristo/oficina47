from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuração do WhatsApp - ALTERE AQUI O SEU NÚMERO
# Formato: código do país + DDD + número (sem espaços, parênteses ou hífens)
# Exemplo: 5511999999999 (Brasil: 55, São Paulo: 11, número: 999999999)
WHATSAPP_NUMBER = '5535997500438'  # Telefone: (35) 99750-0438
PHONE_NUMBER = '(35) 99750-0438'

# Lista de produtos com suas imagens
def get_products():
    """Retorna lista de produtos baseada nas imagens disponíveis"""
    image_dir = 'imagem'
    products = []
    
    # Mapeamento de imagens para torradores de café com capacidades
    product_mapping = {
        '0099718b-e8be-4ee6-877d-1b81b7d2f59a.jpg': {
            'name': 'Torrador de Café 05kg',
            'description': 'Torrador com capacidade de 05kg, ideal para pequenas torrefações e cafeterias',
            'capacity': '05kg'
        },
        '0c1c3b27-5492-4431-881f-bb36e123e9e4.jpg': {
            'name': 'Torrador de Café 10kg',
            'description': 'Torrador com capacidade de 10kg, perfeito para produção média',
            'capacity': '10kg'
        },
        '1a4c1f20-dd17-47ce-b4b2-dc040e4a3808.jpg': {
            'name': 'Torrador de Café 15kg',
            'description': 'Torrador com capacidade de 15kg, para produção em maior escala',
            'capacity': '15kg'
        },
        '2153a45a-05dc-425e-9b4d-0a2f75ed20d4.jpg': {
            'name': 'Torrador de Café 05kg',
            'description': 'Torrador com capacidade de 05kg, ideal para pequenas torrefações e cafeterias',
            'capacity': '05kg'
        },
        '31f35aed-e1ee-4f70-b8cd-21b62a3e69d5.jpg': {
            'name': 'Torrador de Café 10kg',
            'description': 'Torrador com capacidade de 10kg, perfeito para produção média',
            'capacity': '10kg'
        },
        '800490f6-574e-41f7-afed-47ec55f46963.jpg': {
            'name': 'Torrador de Café 15kg',
            'description': 'Torrador com capacidade de 15kg, para produção em maior escala',
            'capacity': '15kg'
        },
        '9bcfb236-dcaa-42a5-b2f0-1e9d1079a0ed.jpg': {
            'name': 'Torrador de Café 05kg',
            'description': 'Torrador com capacidade de 05kg, ideal para pequenas torrefações e cafeterias',
            'capacity': '05kg'
        },
        'a24fa03f-32e1-488d-8f4e-633aeabac673.jpg': {
            'name': 'Torrador de Café 10kg',
            'description': 'Torrador com capacidade de 10kg, perfeito para produção média',
            'capacity': '10kg'
        },
        'a3dd159e-c955-42e7-91c6-6c027e7bd97c.jpg': {
            'name': 'Torrador de Café 15kg',
            'description': 'Torrador com capacidade de 15kg, para produção em maior escala',
            'capacity': '15kg'
        }
    }
    
    # Adiciona produtos baseados nas imagens disponíveis
    if os.path.exists(image_dir):
        for filename in os.listdir(image_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')) and filename != 'logomarca.jpg':
                # Remove duplicatas (arquivos com (1) no nome)
                if '(1)' not in filename:
                    product_info = product_mapping.get(filename, {
                        'name': 'Torrador de Café',
                        'description': 'Torrador de café de alta qualidade',
                        'capacity': '05kg'
                    })
                    products.append({
                        'id': len(products) + 1,
                        'image': f'{image_dir}/{filename}',
                        'name': product_info['name'],
                        'description': product_info['description'],
                        'capacity': product_info.get('capacity', '05kg')
                    })
    
    # Limita a 4 produtos (2 colunas x 2 linhas) - pega os primeiros 4
    products = products[:4]
    
    return products

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products, whatsapp_number=WHATSAPP_NUMBER, phone_number=PHONE_NUMBER)

@app.route('/imagem/<path:filename>')
def serve_image(filename):
    """Serve imagens da pasta imagem"""
    return send_from_directory('imagem', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

