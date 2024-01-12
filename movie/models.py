from django.db import models
from rest_framework import response


class Director(models.Model):
    name = models.CharField
    if response.status_code == 200:
        directors_data = response.json()

        for director in directors_data:
            director_name = director["name"]
            movies_count = len(director["movies"])

            print(f"Режиссер: {director_name}, Количество фильмов: {movies_count}")
    else:
        print(f"Ошибка при запросе: {response.status_code}")


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    duration = models.IntegerField
    director = models.ForeignKey


STAR_CHOICES = (
    (i, '* ' * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    rating = models.IntegerField(choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    if response.status_code == 200:
        movies_reviews_data = response.json()

        total_reviews = 0
        total_rating = 0

        for movie_review in movies_reviews_data:
            movie_title = movie_review["title"]
            reviews = movie_review.get("reviews", [])
            average_rating = sum(review["rating"] for review in reviews) / len(reviews) if reviews else 0

            print(f"Фильм: {movie_title}")
            print("Отзывы:")
            for review in reviews:
                print(f" - {review['text']}, Рейтинг: {review['rating']}")

            print(f"Средний рейтинг: {average_rating}\n")

            total_reviews += len(reviews)
            total_rating += sum(review["rating"] for review in reviews)

        if total_reviews > 0:
            average_overall_rating = total_rating / total_reviews
            print(f"Общий средний рейтинг по всем фильмам: {average_overall_rating}")
        else:
            print("Нет отзывов для расчета среднего рейтинга.")
    else:
        print(f"Ошибка при запросе: {response.status_code}")
