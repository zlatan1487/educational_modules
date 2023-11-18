from django.test import TestCase
from django.urls import reverse
from users.models import User
from education_modules.models import EducationalModule, Review
from education_modules.forms import EducationModuleForm, ReviewForm


class EducationModuleViewsTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя и образовательный модуль для тестов
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword')
        self.client.login(
            username='testuser@example.com',
            password='testpassword')
        self.education_module = EducationalModule.objects.create(
            order_number=1,
            title='Test Module',
            description='Test Description',
            owner=self.user
        )
        # Создаем отзыв для образовательного модуля
        self.review = Review.objects.create(
            text='Test Review',
            author=self.user,
            educational_module=self.education_module
        )

    def test_education_create_view(self):
        # Тестирование создания нового образовательного модуля
        self.client.login(username='testuser',
                          password='testpassword')
        response = self.client.post(
            reverse('education_modules:create_education'),
            {
                'order_number': 2,
                'title': 'New Test Module',
                'description': 'New Test Description',
                'owner': self.user.id
            })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(EducationalModule.objects.count(), 2)

    def test_educations_list_view(self):
        # Тестирование отображения списка образовательных модулей
        response = self.client.get(reverse('education_modules:education_list'))
        self.assertEqual(response.status_code, 200)

        education_list_values = response.context[
                'education_list'].values_list(
                'title', flat=True)

        expected_values = ['Test Module']
        self.assertListEqual(list(education_list_values), expected_values)

    def test_educations_detail_view(self):
        # Тестирование отображения деталей образовательного модуля
        response = self.client.get(
            reverse('education_modules:education_detail',
                    kwargs={'pk': self.education_module.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.education_module)

    def test_education_create_form_valid(self):
        # Тестирование валидности формы создания образовательного модуля
        form_data = {
            'order_number': 2,
            'title': 'New Test Module',
            'description': 'New Test Description',
            'owner': self.user.id
        }
        form = EducationModuleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_valid(self):
        # Тестирование валидности формы отзыва
        form_data = {
            'text': 'New Test Review',
            'author': self.user.id,
            'educational_module': self.education_module.id
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())
