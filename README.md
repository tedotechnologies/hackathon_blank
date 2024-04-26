# hackathon_blank

## Описание

Этот репозиторий создан для задачи хакатона по созданию инструмента трансормации изображения в стиль ТеДо.

## Подготовка системы
1. `curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list`
2. `sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit`
3. `sudo nvidia-ctk runtime configure --runtime=docker`
4. `sudo systemctl restart docker`

## Прежде чем начать разработку

Убедитесь, что у вас корректно выполняются следующие команды из корня репозитория:

```bash
docker build -t img_name .  # замените <team_name> на название вашей команды написанное латиницей и без пробелов
docker run --runtime=nvidia --gpus all -v ./test:/test -v ./results:/results img_name  # замените <team_name> на название вашей команды написанное латиницей и без пробелов
```

Результатом выполнения этих не сложных действий будет создание трех новых изображений в папке `results`.
В нашем случае это всего лишь изображения, которые были в папке `test`.
В вашем решении это должны быть изображения, которые максимально близки к стилю ТеДо.

Успехов в разработке!

## Прежде чем отрпавить решение

Пожалуйста убедитесь, что ваше решение корректно работает на вашем компьютере.
И не поленитесь еще раз запустить команды из предыдущего пункта.
Самостоятельно оцените качество полученных изображений.

PS: В ходе проверки решений, конечно же изображения будут заменены на новые.
