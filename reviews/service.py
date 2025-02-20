from reviews.repository import ReviewRepository


class ReviewService:

    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        return self.review_repository.get_reviews()

    def create_review(self, movie, rating, comment):
        review = dict(
            movie=movie,
            rating=rating,
            comment=comment,
        )
        return self.review_repository.create_review(review)
