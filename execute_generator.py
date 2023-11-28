import os
from synthetic_image_generator import SyntheticImageGenerator

# Diretórios de fontes e backgrounds
font_dirs = 'fonts'
background_dirs = 'backgrounds'

# Número de imagens a serem geradas
num_images = 10

# Diretório de saída (o diretório atual, neste exemplo)
output_dir = os.getcwd()

# Criar uma instância da classe SyntheticImageGenerator
synthetic_generator = SyntheticImageGenerator(output_dir, font_dirs, background_dirs, num_images)

# Gerar imagens sintéticas
synthetic_generator.generate_images()
