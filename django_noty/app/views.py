from django.contrib import messages
from django.views import View


class NotyMessageView(View):
    template_name = 'noty.html'

    def get(self, request):
        messages.success(request, 'Hello World from noty !!!')
        return render(request, self.template_name)