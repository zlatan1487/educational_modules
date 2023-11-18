from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserViewsTestCase(TestCase):
    def setUp(self):
        # Создаем экземпляр клиента для тестирования
        self.client = Client()
        # Создаем тестового пользователя
        self.user = get_user_model().objects.create_user(
            password='testpassword',
            email='test@example.com'
        )

    def test_login_view(self):
        # Проверяем, что страница входа возвращает
        # код 200 и использует правильный шаблон
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        # Проверяем, что страница выхода возвращает код 302
        # (перенаправление)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_view(self):
        # Проверяем, что страница регистрации
        # возвращает код 200 и использует правильный шаблон
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_form_valid(self):
        # Проверяем, что успешная отправка
        # формы регистрации возвращает код 200
        data = {
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(reverse('users:register'), data)
        self.assertEqual(response.status_code, 200)

    def test_user_update_view(self):
        # Входим в систему тестовым пользователем
        self.client.login(email='test@example.com', password='testpassword')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_form.html')

    def test_generate_new_password_view(self):
        # Входим в систему тестовым пользователем
        self.client.login(email='test@example.com', password='testpassword')
        # Проверяем, что страница смены пароля возвращает код 302
        # (перенаправление) после генерации нового пароля
        response = self.client.get(reverse('users:generate_new_password'))
        self.assertEqual(response.status_code, 302)
