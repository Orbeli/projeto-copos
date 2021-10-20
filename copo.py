import cv2, glob, math, ctypes

media_vazio, media_cheio = [], []
threshold = 205
entrada = "cheio4.png"

def trata_img(path_img):
    """
    Converte uma imagem em cinza,
    depois converte esta imagem em binario
    """
    img = cv2.imread(path_img)
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_binaria = cv2.threshold(img_cinza, threshold, 255, cv2.THRESH_BINARY)[1]

    return img_binaria

def get_img_mean_values(path):
    """
    Percorre um diretorio com imagens de mesma extensao,
    e salva o valor da media (mean)
    das imagens binarias em uma lista
    """
    for file in glob.glob(path):
        img = trata_img(file)

        if 'vazio' in file:
            media_vazio.append(img.mean())
        else:
            media_cheio.append(img.mean())

def get_img_entrada_mean():
    """
    Retorna a media (mean) da imagem de entrada,
    depois de converter a imagem em cinza e transformar em binaria
    """
    img = trata_img("copos/" + entrada)

    return img.mean()

def verificar_copo():
    """
    Recupera a maior media (mean) arredondada dos copos cheios e
    verifica a imagem de entrada, retornando o estado do copo.
    """
    mean_max_cheio = int(math.ceil(max(media_cheio)))

    if get_img_entrada_mean() < mean_max_cheio:
        print("Copo Cheio")
        ctypes.windll.user32.MessageBoxW(0, "Copo Cheio", "Estado do copo", 1)
    else:
        print("Copo Vazio")
        ctypes.windll.user32.MessageBoxW(0, "Copo Vazio", "Estado do copo", 1)

    # Mostra a imagem escolhida ao usuario
    img = cv2.imread("copos/" + entrada)
    cv2.imshow("copo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

get_img_mean_values("copos/*.png")
get_img_mean_values("copos/*.jpg")
verificar_copo()
