from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(username='t1', password='p1')
        test_user_1.save()

        test_post = Post.objects.create(
            author=test_user_1,
            title='post title',
            body='post body'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.username, 't1')
        self.assertEqual(post.title, 'post title')
        self.assertEqual(post.body, 'post body')
