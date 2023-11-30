# -*- coding: utf-8 -*-

import os
import random
from PIL import Image, ImageDraw, ImageFont
from sklearn.model_selection import train_test_split


class SyntheticImageGenerator:
    def __init__(self, output_dir: str, font_dir: str, background_dir: str,
                 num_images: int = 10, train_ratio: float = 0.7):
        """
        Inicializa o gerador de imagens sintéticas.

        :param output_dir: Diretório de saída para salvar as imagens geradas.
        :param font_dir: Diretório contendo arquivos de fonte (formato .ttf).
        :param background_dir: Diretório contendo arquivos de fundo (formato .png).
        :param num_images: Número total de imagens a serem geradas. Default:10
        :param train_ratio: Proporção de imagens a serem usadas para treinamento.Default:0.7
        """
        self.output_dir = output_dir
        self.font_dir = font_dir
        self.background_dir = background_dir
        self.num_images = num_images
        self.train_ratio = train_ratio

    def generate_images(self):
        """
        Gera imagens sintéticas divididas em conjuntos de treinamento e validação.
        """
        # Cria os diretórios necessários
        synthetic_dir = os.path.join(self.output_dir, 'sintetico')
        os.makedirs(synthetic_dir, exist_ok=True)

        train_dir = os.path.join(synthetic_dir, 'train')
        val_dir = os.path.join(synthetic_dir, 'val')

        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(val_dir, exist_ok=True)

        image_output_dir_train = os.path.join(train_dir, 'images')
        text_output_dir_train = os.path.join(train_dir, 'labels')

        image_output_dir_val = os.path.join(val_dir, 'images')
        text_output_dir_val = os.path.join(val_dir, 'labels')

        os.makedirs(image_output_dir_train, exist_ok=True)
        os.makedirs(text_output_dir_train, exist_ok=True)
        os.makedirs(image_output_dir_val, exist_ok=True)
        os.makedirs(text_output_dir_val, exist_ok=True)

        # Lista de arquivos de fonte e fundo
        font_files = [os.path.join(self.font_dir, file) for file in
                      os.listdir(self.font_dir) if file.endswith(('.ttf'))]

        background_files = [os.path.join(self.background_dir, file) for file in
                            os.listdir(self.background_dir) if
                            file.endswith(('.png'))]

        # Divide as imagens em conjuntos de treinamento e validação
        images_train, images_val = train_test_split(range(self.num_images),
                                                    train_size=self.train_ratio,
                                                    random_state=42)

        # Gera imagens de treinamento
        for i, image_idx in enumerate(images_train):
            self.generate_image(image_output_dir_train, text_output_dir_train, i + 1,
                                font_files, background_files)

        # Gera imagens de validação
        for i, image_idx in enumerate(images_val):
            self.generate_image(image_output_dir_val, text_output_dir_val, i + 1,
                                font_files, background_files)

    def generate_image(self, image_output_dir: str, text_output_dir: str, index: int,
                       font_files: list[str], background_files: list[str]):
        """
        Gera uma imagem sintética.

        :param image_output_dir: Diretório de saída para a imagem gerada.
        :param text_output_dir: Diretório de saída para o arquivo de texto associado à imagem.
        :param index: Índice da imagem.
        :param font_files: Lista de caminhos para arquivos de fonte.
        :param background_files: Lista de caminhos para arquivos de fundo.
        """
        width = random.randint(600, 800)
        height = random.randint(600, 800)
        num_lines = random.randint(5, 20)
        max_words_per_line = random.randint(1, 3)
        font_size = random.randint(15, 25)

        # Escolhe aleatoriamente um arquivo de fonte e fundo
        font_path = random.choice(font_files)
        background_path = random.choice(background_files)

        # Obtém os nomes do arquivo de fonte e fundo sem extensão
        font_name = os.path.splitext(os.path.basename(font_path))[0]
        background_name = os.path.splitext(os.path.basename(background_path))[0]

        image_filename = f'{index}_{background_name}_{font_name}.png'
        text_filename = f'{index}_{background_name}_{font_name}.txt'

        image_path = os.path.join(image_output_dir, image_filename)
        text_path = os.path.join(text_output_dir, text_filename)

        # Escolhe aleatoriamente um arquivo de fonte e fundo
        font_path = random.choice(font_files)
        background_path = random.choice(background_files)

        # Decide se a imagem terá linhas de caderno
        has_lines = random.choice(
            [True, False])

        # Gera a imagem sintética
        self.generate_synthetic_image(width, height, num_lines, max_words_per_line,
                                      image_path, text_path, font_path, background_path,
                                      font_size, has_lines)

    def generate_synthetic_image(self, width: int, height: int, num_lines: int,
                                 max_words_per_line: int,
                                 image_path: str, text_path: str, font_path: str,
                                 background_path: str,
                                 font_size: int, has_lines: bool = True) -> list[tuple[int, int, int, int]] | None:
        """
        Gera uma imagem sintética com texto.

        :param width: Largura da imagem.
        :param height: Altura da imagem.
        :param num_lines: Número de linhas de texto na imagem.
        :param max_words_per_line: Número máximo de palavras por linha.
        :param image_path: Caminho completo para salvar a imagem gerada.
        :param text_path: Caminho completo para salvar o arquivo de texto associado à imagem.
        :param font_path: Caminho do arquivo de fonte (.ttf).
        :param background_path: Caminho do arquivo de fundo (.png).
        :param font_size: Tamanho da fonte.
        :param has_lines: Indica se a imagem terá linhas de caderno. Padrão: True.
        :return: Lista de coordenadas das bounding boxes do texto ou None se has_lines for False.
        """
        # Abre a imagem de fundo e a redimensiona
        background = Image.open(background_path)
        background = background.resize((width, height))
        img = Image.new('RGB', (width, height), color='white')
        img.paste(background, (0, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=font_size)

        words = [
            'Produtos', 'kg', 'ml', 'produto1', 'alimentos', 'manteiga',
            'saco de lixo', 'caixa', 'papelão', 'formiga', 'biscoito', 'bolacha',
            'dhiushd', 'cfscaa', 'remédio', 'Queijo', 'Macarrão', 'Feijão', 'frutas',
            'tomate', 'requeijão', 'hidratante', 'churrasco', 'carne', 'chilito',
            'frango','uhuhsdsdgbsgdfgysgf', 'coisa', 'nada', 'pct',
            'Eletrônicos', 'Roupas', 'Alimentos', 'Brinquedos', 'Livros',
            'Calçados', 'Esportes', 'Decoração', 'Ferramentas', 'Jogos',
            'Automotivo', 'Bebidas', 'Beleza', 'Joias', 'Móveis',
            'Instrumentos', 'Musicais', 'Jardinagem', 'Papelaria', 'Fitness', 'Camping',
            'Pet Shop', 'Filmes', 'Informática', 'Eletrodomésticos', 'Brindes',
            'Viagens', 'Instrumentos', 'Culinários', 'Artesanato', 'Telefonia',
            'Acessórios', 'Saúde', 'Produtos', 'Orgânicos', 'Crianças', 'Hobbies',
            'Produtos', 'Sustentáveis','Casa', 'Jardim', 'Moda', 'Infantil',
            'Produtos', 'Escritório', 'Moda Praia', 'Artigos', 'Festas',
            'Colecionáveis', 'Produtos','Regionais', 'Gourmet', 'Antiguidades',
            'Tecnologia', 'Maquiagem', 'Personalizados'
                 ]

        # Configurações de margens e coordenadas máximas do texto
        margin_top = 100
        margin_right = 80
        bottom_margin = 50
        max_text_y = height - margin_top - bottom_margin
        left_margin = 150
        max_text_x = width - margin_right - left_margin

        if has_lines:
            # Configurações adicionais para linhas de caderno
            line_spacing = 15
            line_coordinates = []

            # Gera linhas de texto
            for idx in range(num_lines):
                line = ' '.join(
                    random.sample(words, random.randint(1, max_words_per_line)))
                text_y = idx * line_spacing + margin_top
                line_y = text_y + line_spacing

                # Verifica se a linha ultrapassa os limites da imagem
                if text_y + line_spacing > max_text_y:
                    break

                # Desenha a linha na imagem
                draw.line([(80, line_y), (width - 80, min(line_y, max_text_y))],
                          fill='gray', width=1)

                # Calcula a bounding box do texto e suas coordenadas
                text_bbox = draw.textbbox((40, 40), line, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                text_x = random.randint(100,
                                        min(int(width * 0.5), max_text_x))

                # Garante que a margem esquerda vai ser igual ou maior que o left_margin
                if text_x + text_width > max_text_x:
                    text_x = left_margin

                line_coordinates.append(
                    (text_x, text_y, text_x + text_width, text_y + text_height))
                draw.text((text_x, text_y), line, font=font, fill=(50, 50, 50))

            img.save(image_path)
            self.save_coordinates_to_txt(text_path, line_coordinates, width)
            return line_coordinates
        else:
            # Configurações para texto sem linhas de caderno
            text_coordinates = []

            # Gera linhas de texto
            for idx in range(num_lines):
                text = ' '.join(
                    random.sample(words, random.randint(1, max_words_per_line)))

                text_y = idx * font_size + margin_top
                left_margin = 100
                max_text_x = width - margin_right - left_margin

                # Calcula a bounding box do texto e suas coordenadas
                text_bbox = draw.textbbox((40, 40), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                text_x = random.randint(left_margin,
                                        min(int(width * 0.5), max_text_x))

                if text_x + text_width > max_text_x:
                    text_x = left_margin

                text_coordinates.append(
                    (text_x, text_y, text_x + text_width, text_y + text_height))
                draw.text((text_x, text_y), text, font=font, fill=(50, 50, 50))

            img.save(image_path)
            self.save_coordinates_to_txt(text_path, text_coordinates, width)
            return None

    def save_coordinates_to_txt(self, text_path: str,
                                text_coordinates: list[tuple[int, int, int, int]],
                                width: int):
        """
        Salva as coordenadas das bounding boxes em um arquivo de texto.

        :param text_path: Caminho completo para o arquivo de texto.
        :param text_coordinates: Lista de coordenadas das bounding boxes.
        :param width: Largura da imagem.
        """
        with open(text_path, 'w') as text_file:
            for coordinate in text_coordinates:
                # Normaliza as coordenadas pela largura da imagem
                normalized_coordinates = [coord / width for coord in coordinate]
                # Adiciona a classe 0 (ou qualquer valor desejado) no início da lista
                normalized_coordinates.insert(0, 0)

                # Escreve no arquivo
                text_file.write(", ".join(map(str, normalized_coordinates)) + "\n")