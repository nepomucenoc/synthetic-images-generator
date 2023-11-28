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
        :param font_dir: Diretório contendo arquivos de fonte (.ttf, .otf).
        :param background_dir: Diretório contendo arquivos de fundo (.png, .jpg, .jpeg).
        :param num_images: Número total de imagens a serem geradas. Padrão: 10.
        :param train_ratio: Proporção de imagens a serem usadas para treinamento. Padrão: 0.7.
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

        font_files = [os.path.join(self.font_dir, file) for file in
                      os.listdir(self.font_dir) if file.endswith(('.ttf', '.otf'))]

        background_files = [os.path.join(self.background_dir, file) for file in
                            os.listdir(self.background_dir) if
                            file.endswith(('.png', '.jpg', '.jpeg'))]

        images_train, images_val = train_test_split(range(self.num_images),
                                                    train_size=self.train_ratio,
                                                    random_state=42)

        for i, image_idx in enumerate(images_train):
            self.generate_image(image_output_dir_train, text_output_dir_train, i + 1,
                                font_files, background_files)

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
        :param font_files: Lista de caminhos para arquivos de fonte (.ttf, .otf).
        :param background_files: Lista de caminhos para arquivos de fundo (.png, .jpg, .jpeg).
        """
        width = random.randint(800, 1200)
        height = random.randint(600, 900)
        num_lines = random.randint(5, 30)
        max_words_per_line = random.randint(1, 5)
        font_size = random.randint(15, 25)

        image_filename = f'imagem_sintetica_{index}.png'
        text_filename = f'imagem_sintetica_{index}.txt'

        image_path = os.path.join(image_output_dir, image_filename)
        text_path = os.path.join(text_output_dir, text_filename)

        font_path = random.choice(font_files)
        background_path = random.choice(background_files)

        has_lines = random.choice(
            [True, False])

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
        :param font_path: Caminho para o arquivo de fonte (.ttf, .otf).
        :param background_path: Caminho para o arquivo de fundo (.png, .jpg, .jpeg).
        :param font_size: Tamanho da fonte.
        :param has_lines: Indica se a imagem terá linhas de caderno. Padrão: True.
        :return: Lista de coordenadas das bounding boxes do texto ou None se has_lines for False.
        """
        background = Image.open(background_path)

        background = background.resize((width, height))

        img = Image.new('RGB', (width, height), color='white')

        img.paste(background, (0, 0))

        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font_path, size=font_size)

        words = ['Produtos', 'a serem', 'expostos', 'aqui', 'para', 'teste',
                 'uhuhsdsdgbsgdfgysgf']
        margin_top = 100
        margin_right = 80
        max_text_y = height - margin_top
        max_text_x = width - margin_right

        if has_lines:
            line_spacing = 15
            line_coordinates = []

            for idx in range(num_lines):
                line = ' '.join(
                    random.sample(words, random.randint(1, max_words_per_line)))

                text_y = idx * line_spacing + margin_top
                line_y = text_y + line_spacing

                if text_y + line_spacing > max_text_y:
                    break

                text_x = random.randint(100, min(int(width * 0.5), max_text_x))

                draw.line([(50, line_y), (width - 80, line_y)], fill='gray', width=1)

                text_width, text_height = draw.textbbox((0, 0), line, font=font)[2:]

                if text_x + text_width > max_text_x:
                    text_x = max_text_x - text_width

                line_coordinates.append(
                    (text_x, text_y, text_x + text_width, text_y + text_height))

                draw.text((text_x, text_y), line, font=font, fill=(50, 50, 50))

            img.save(image_path)

            self.save_coordinates_to_txt(text_path, line_coordinates)

            return line_coordinates
        else:
            text_coordinates = []

            for idx in range(num_lines):
                text = ' '.join(
                    random.sample(words, random.randint(1, max_words_per_line)))

                text_y = idx * font_size + margin_top
                text_x = random.randint(100, min(int(width * 0.5), max_text_x))

                if text_x > max_text_x:
                    text_x = max_text_x

                text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

                if text_x + text_width > max_text_x:
                    text_x = max_text_x - text_width

                text_coordinates.append(
                    (text_x, text_y, text_x + text_width, text_y + text_height))

                draw.text((text_x, text_y), text, font=font, fill=(50, 50, 50))

            img.save(image_path)

            self.save_coordinates_to_txt(text_path, text_coordinates)

            return None

    def save_coordinates_to_txt(self, text_path: str,
                                text_coordinates: list[tuple[int, int, int, int]]):
        """
        Salva as coordenadas das bounding boxes em um arquivo de texto.

        :param text_path: Caminho completo para o arquivo de texto.
        :param text_coordinates: Lista de coordenadas das bounding boxes.
        """
        with open(text_path, 'w') as text_file:
            for coordinate in text_coordinates:
                text_file.write(f"{coordinate[0]}, {coordinate[1]}, {coordinate[2]}, "
                                f"{coordinate[3]}\n")
