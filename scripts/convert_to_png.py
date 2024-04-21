def convert_to_png(location):
    """
    Autor: Rui Sousa

    **Função para converter imagens em PNG e organizar o data set para exportação.**

    Esta função oferece duas formas de utilização:

    **1. Jupyter Notebook:**
        - Utilize comandos mágicos para navegar até o diretório das imagens a serem convertidas.
        - Execute a função `convert_to_png`
        - Seguir o notebook `img_convert.ipynb` para este efeito.

    **2. Script Python:**
        - Execute o script diretamente no terminal no diretório das imagens a serem processadas.
        - Executar usando `python caminho\para\o\script\convert_to_png.py`

    **Funcionalidades:**

    - Converte todos os formatos de imagem no diretório para PNG.
    - Copia todos os arquivos PNG para a pasta "output".

    **Objetivo:**

    Organizar o data set em formato PNG para facilitar a exportação.

    **Exemplos de Uso:**

    ```python
    # No Jupyter Notebook:
    %cd /caminho/para/imagens
    convert_to_png()

    # No Terminal:
    python convert_to_png.py
    ```

    **Observações:**

    - A pasta "output" será criada automaticamente se não existir.
    - Arquivos PNG já existentes na pasta "output" serão copiados sem conversão.
    - Erros durante a conversão ou cópia de arquivos serão registrados no console.
    """

    from PIL import Image
    import os
    import shutil

    if not os.path.exists('output'):
        os.makedirs('output')

    for file in os.listdir('./'):
        if not file.endswith('.png') and not os.path.isdir(file):
            fname = os.path.splitext(file)[0] + '.png'
            print(f'convertendo {file}')
            with Image.open(file) as tif:
                tif.save(f'output/{fname}', format='PNG')
        elif file.endswith('.png'):
            try:
                print(f'copiando {file}')
                shutil.copy(file, f'output/{file}')
            except Exception as e:
                print(f'erro ao copiar {file}')

if __name__ == '__main__':
    convert_to_png()
