import shutil
from pathlib import Path

import torch


def main(test_folder: Path, results_folder: Path):
    for img_path in test_folder.glob("*.jpg"):
        # проверяем доступность cuda,
        # чтобы в случае необходимости использовать gpu
        print("CUDA is available: ", torch.cuda.is_available())

        # Вот здесь надо вставить ваш лучший код
        # для трансформации одного изображения,
        # которое находется по адресу img_path.
        # Пока что просто копируем изображение в папку с результатами
        shutil.copy(img_path, results_folder)


if __name__ == "__main__":
    test_folder = Path("/test")
    results_folder = Path("/results")
    main(test_folder, results_folder)
