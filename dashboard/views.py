from django.db.models import Q, Avg, Max, Count
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

from dashboard.models import Player, Game, Score


def index(request):

    leaders = Player.objects\
        .annotate(avg_rating=Avg('score_player__score'), times_played=Count('score_player__id'))\
        .filter(
            times_played__gt=2)\
        .order_by('-avg_rating')[:10]

    return render(request, 'index.html', {'leaders': leaders})

def details(request):
    username = request.GET.get('user', '')

    try:
        player = Player.objects.get(name=username)
        number_of_wins = Game.objects.filter(Winner__name=username).count()
        number_of_losses = Game.objects.exclude(Winner__name=username)\
            .filter(Q(Score1__Player__name=username) | Q(Score2__Player__name=username))\
            .count()

        average_score = Score.objects.filter(Player__name=username).aggregate(Avg('score'))['score__avg']
        average_score = average_score is None and 0.0 or average_score

        highest_score = Score.objects.filter(Player__name=username).aggregate(max_score=Max('score'))['max_score']

        games_with_high_score = Game.objects\
            .filter(Q(Score1__Player__name=username) | Q(Score2__Player__name=username))\
            .filter(Q(Score1__score=highest_score) | Q(Score2__score=highest_score))


    except Player.DoesNotExist:
        raise Http404("Player does not exist")
    return render(
        request,
        'details.html',
        {
            'player': player,
            'number_of_wins': number_of_wins,
            'number_of_losses': number_of_losses,
            'average_score': average_score,
            'highest_score': highest_score,
            'games_with_high_score': games_with_high_score,
        }
    )
