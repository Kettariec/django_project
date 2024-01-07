from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog
from pytils.translit import slugify


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image', 'date_of_creation',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image', 'date_of_creation',)
    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


def toggle_activity(request, pk):
    dog_item = get_object_or_404(Blog, pk=pk)
    if dog_item.is_published:
        dog_item.is_published = False
    else:
        dog_item.is_published = True
    dog_item.save()
    return redirect(reverse('blog:list'))