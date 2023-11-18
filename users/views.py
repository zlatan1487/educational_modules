import random
from django.shortcuts import redirect, reverse
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from users.models import User
from users.form import UserRegisterForm, UserForm
from django.contrib import messages
from smtplib import SMTPException


class LoginView(BaseLoginView):
    """
        Представление для входа пользователя в систему.
    """
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Профиль'
    }


class LogoutView(BaseLogoutView):
    """
        Представление для выхода пользователя из системы.
    """
    pass


class RegisterView(CreateView):
    """
        Представление для регистрации нового пользователя.
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form):
        try:
            new_user = form.save()
            send_mail(
                subject='Поздравляем с регистрацией!',
                message='Вы зарегистрировались на нашей платформе.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
            messages.success(self.request, 'Регистрация прошла успешно! '
                                           'Пожалуйста, войдите.')
            return super().form_valid(form)

        except SMTPException as e:
            # Обработка исключения при ошибке отправки почты
            messages.error(self.request, f'Ошибка при отправке '
                                         f'почты: {str(e)}')
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при регистрации. '
                                     'Проверьте правильность '
                                     'введенных данных.')
        return super().form_invalid(form)


class UserUpdateView(UpdateView):
    """
        Представление для обновления профиля пользователя.
    """
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    extra_context = {
        'title': 'Изменить профиль'
    }

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    """
        Генерация нового пароля, отправка его на почту
         пользователю и сохранение его хэша в базе данных.
    :param request:
    :return:
    """
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('education_modules:education_list'))
