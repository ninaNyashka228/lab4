import string

positive_words = {'отличный', 'хороший', 'красивый', 'быстрый', 'удобный', 
                  'качественный', 'яркий', 'мощный', 'нравится', 'супер', 
                  'классный', 'идеальный', 'отлично', 'прекрасный'}

negative_words = {'плохой', 'медленный', 'ужасный', 'глючит', 'греется', 
                  'разряжается', 'ломается', 'тяжелый', 'неудобный', 'слабый', 
                  'минус', 'садится', 'ужасно', 'тормозит'}

neutral_words = {'экран', 'дюйм', 'дюйма', 'дюймов', 'батарея', 'камера', 
                 'память', 'гб', 'процессор', 'вес', 'цвет', 'размер', 
                 'телефон', 'смартфон', 'корпус'}

def remove_punctuation(text):
    """Функция для удаления знаков препинания"""
    punct = string.punctuation + '«»—–'
    return text.translate(str.maketrans('', '', punct))

def analyze_review(review_text):
    """Функция обработки и классификации отзыва"""
    print(f"Отзыв: {review_text}\n")
    
    text = review_text.lower()
    text = remove_punctuation(text)
    words = text.split()
    
    pos_found = []
    neg_found = []
    neu_found = []
    
    for word in words:
        if word in positive_words and word not in pos_found:
            pos_found.append(word)
        elif word in negative_words and word not in neg_found:
            neg_found.append(word)
        elif word in neutral_words and word not in neu_found:
            neu_found.append(word)
            
    if len(pos_found) == 0 and len(neg_found) == 0:
        overall_rating = "Нейтральный отзыв"
    elif len(pos_found) > len(neg_found):
        overall_rating = "Положительный отзыв"
    elif len(neg_found) > len(pos_found):
        overall_rating = "Отрицательный отзыв"
    else:
        overall_rating = "Смешанный отзыв"

    print(f"Положительные характеристики: {', '.join(pos_found) if pos_found else 'не найдены'}")
    print(f"Отрицательные характеристики: {', '.join(neg_found) if neg_found else 'не найдены'}")
    print(f"Нейтральные характеристики: {', '.join(neu_found) if neu_found else 'не найдены'}")
    print(f"Общая оценка: {overall_rating}")

reviews = [
    "Отличный смартфон, очень красивый и быстрый. Камера супер, экран яркий.",
    "Ужасный телефон. Батарея разряжается очень быстро, греется, медленный.",
    "Телефон хороший, экран 6.5 дюйма. Но батарея слабая, быстро садится.",
    "Купил смартфон. Цвет черный, память 128 гб, вес 200 грамм.",
    "Камера отличная, но телефон тяжелый и неудобный. Процессор мощный."
]

for i, review in enumerate(reviews, 1):
    print(f"Обработка отзыва №{i}")
    analyze_review(review)