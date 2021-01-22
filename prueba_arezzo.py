
import base64
from difflib import SequenceMatcher
from typing import List, Union

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    

    answer = []
    for text in texts[1:]:
        answer.append(text.description)


    return answer


def get_text_by_key(text_to_search: str, text_list: List[str]) -> dict:
        """ Getting texts with similarity based on text_to_search from text_list.

        Args:
            text_to_search: Text to search.
            Coming from data server config.
            text_list (List[str]): Annotations obtained by google vision api.

        Returns:
            dict: returns probability that has match with text_to_search.
        """        
        text_found = { 'probability': 0.0 }
        
        for text in text_list:
            probability = SequenceMatcher(None, text_to_search, text[0:len(text_to_search)]).quick_ratio()
            if probability > 0.5:
                return { 'probability': probability }
        return text_found


# data = get_text_by_key('07900208000963-S35767567-1*1',['S3576756f'])
# data = get_text_by_key('S35767567-1*1',['S3576756f'])

# data = get_text_by_key('S3576756f',['07900208000963-S35767567-1*1'])
# data = get_text_by_key('07900208000297-A09015793-1*1',['S3576756f'])
# data = get_text_by_key('A09015793-1*1',['S3576756f'])

data = get_text_by_key('S35767567-1',['S3576756f'])
print(data)

data = get_text_by_key('A09015793-1',['A09015793'])
print(data)

data = get_text_by_key('07900208000106-A09009505-1*1',['A09009505-1'])
print(data)

# orders = [ 
#     {'order':'S35765679-1', 'service': 535395 },
#     {'order':'A09015793-1', 'service': 535396 },
#     {'order':'S35765117-1', 'service': 534201 },
#     {'order':'A08781752-1', 'service': 534301 },
# ]

# def detect_service( data_foto, orders):
#     for order in orders:
#         data = get_text_by_key(order.get('order'),data_foto)
#         if data['probability'] > 0.0:
#             print(f'Orden numero: {order["order"]} pertenece al servicio {order["service"]} con probabilidad {data["probability"]}')


# print('Ejercicio Foto manuscrita')
# data_foto = detect_text('./foto3.jpg')
# print(data_foto)
# detect_service(data_foto, orders )

# print('Ejercicio Foto impresa')
# data_foto = detect_text('./foto4.jpg')
# print(data_foto)
# detect_service(data_foto, orders )

# print('Ejercicio Foto manuscrita 2')
# data_foto = detect_text('./foto1.jpg')
# print(data_foto)
# detect_service(data_foto, orders )