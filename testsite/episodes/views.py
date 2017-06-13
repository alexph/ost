from django.views.generic import DetailView
from episodes.models import Episode


class EpisodeDetail(DetailView):
    template_name = 'episodes/episode.html'
    queryset = Episode.objects.all()

    def get_reactions(self):
        return self.object.reactions.filter(deleted=False)

    def get_context_data(self, **kwargs):
        kwargs['reactions'] = self.get_reactions()
        return super().get_context_data(**kwargs)
