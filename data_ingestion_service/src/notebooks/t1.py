import pycld2 as cld2


text = "Bonjour le monde! Ceci est une phrase en français. හල වර්ගය. நான் உன்னை காதலி்கிறேன்"

extract_sentences = {}

is_reliable, text_bytes_found, details, vectors = cld2.detect(text, returnVectors=True)

print(f'is_reliable: {is_reliable}')
print(f'text_bytes_found: {text_bytes_found}')
print(f'details: {details}')
print(f'vectors: {vectors}')

# Correct extraction using byte slicing
text_bytes = text.encode('utf-8')
for offset, length, lang_name, lang_code in vectors:
    segment_bytes = text_bytes[offset:offset + length]
    segment = segment_bytes.decode('utf-8')
    print(f'\nLanguage: {lang_name} ({lang_code})')
    print(f'Segment: {segment}')

    extract_sentences[segment] = {
        "language": lang_name,
        "language_code": lang_code,
    }

