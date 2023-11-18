from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from education_modules.forms import ReviewForm, EducationModuleForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, \
                                 ListView, \
                                 DetailView, \
                                 UpdateView, \
                                 DeleteView
from education_modules.models import EducationalModule, Review


class EducationCreateView(CreateView):
    """
        Определение представления для создания нового образовательного модуля
    """
    model = EducationalModule
    form_class = EducationModuleForm
    template_name = 'education_modules/education_form.html'
    success_url = reverse_lazy('education_modules:education_list')


class EducationsListView(ListView):
    """
    Представление для отображения списка образовательных модулей
    """
    template_name = 'education_modules/education.html'
    context_object_name = 'education_list'

    extra_context = {
        'title': 'Список модулей',
    }

    def get_queryset(self):
        return EducationalModule.objects.select_related('owner').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module_id = self.kwargs.get('module_id', None)

        if module_id:
            selected_module = get_object_or_404(
                EducationalModule.objects.select_related(
                    'owner', 'reviews'), id=module_id)
            context.update({
                'selected_module': selected_module,
                'reviews': selected_module.reviews.all(),
            })

        return context


class EducationsDetailView(DetailView, FormView):
    """
        Представление для отображения деталей
        образовательного модуля и добавления отзыва
    """
    template_name = 'education_modules/education_detail.html'

    model = EducationalModule
    form_class = ReviewForm

    extra_context = {
        'title': 'Модуль',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context

    def form_valid(self, form):
        education_module = self.get_object()
        author = self.request.user
        text = form.cleaned_data['text']

        Review.objects.create(
            author=author,
            text=text,
            educational_module=education_module
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('education_modules:education_detail',
                            kwargs={'pk': self.kwargs['pk']})


class EducationEditView(UpdateView):
    """
        Представление для редактирования образовательного модуля
    """
    model = EducationalModule
    form_class = EducationModuleForm
    template_name = 'education_modules/education_form.html'
    success_url = reverse_lazy('education_modules:education_list')


class EducationDeleteView(DeleteView):
    """
        Представление для удаления образовательного модуля
    """
    model = EducationalModule
    success_url = reverse_lazy('education_modules:education_list')
    template_name = 'education_modules/education_confirm_delete.html'


def delete_review(request, review_id):
    """
        Представление для удаления отзыва
    """
    review = get_object_or_404(Review, id=review_id)
    review.delete()

    return redirect(reverse('education_modules:education_detail',
                            kwargs={'pk': review.educational_module.pk}))
