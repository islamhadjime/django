from django.shortcuts import render, get_object_or_404
from .models import *

def post_list(request):

    return render(request, 'game/index.html')


def post_game(request):
    game = Game.objects.all()
    return render(request, 'game/game.html',{"game":game})

def post_script(request):
    script = Script.objects.all()
    return render(request, 'game/script.html',{"script":script})


#====================URL=================================
def script(request,pk):
    script_one = get_object_or_404(Script, pk=pk)
    return render(request,'game/script/script_one.html',{'script_one':script_one})

# def game(request,pk):
#     game_one = get_object_or_404(Game, pk=pk)
#     return render(request,'game/game_path/new_game.html' ,{'game_one':game_one})
