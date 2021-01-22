
import base64

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    # Con image context para el idioma    
    #image_ctx = vision.ImageContext( language_hints=["es"])
    #response = client.document_text_detection(image=image,image_context=image_ctx)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    #print(f'WORD BX {word.bounding_box}')
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        #print('\tSymbol: {} (confidence: {})'.format(
                        #    symbol.text, symbol.confidence))
                        a = 1

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#detect_document('./foto1.jpg')
#detect_document('./foto2.png')
detect_document('./foto4.jpg')
