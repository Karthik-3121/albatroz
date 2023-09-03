from django.shortcuts import render
from chat.models import  Friends, Messages
from user.models import UserProfile

# Create your views here.

def getFriendsList(id):
    """
    Get the list of friends of the  user
    :param: user id
    :return: list of friends
    """
    try:
        user = UserProfile.objects.get(id=id)
        ids = list(user.friends_set.all())
        friends = []
        for id in ids:
            num = str(id)
            fr = UserProfile.objects.get(id=int(num))
            friends.append(fr)
        return friends
    except:
        return []


def getUserId(username):
    """
    Get the user id by the username
    :param username:
    :return: int
    """
    use = UserProfile.objects.get(username=username)
    id = use.id
    return id

def find_friends(request):
    users = list(UserProfile.objects.all())
    user_ls = []
    for user in users:
        if user.username != request.user.username:
            user_ls.append(user)
    return render(request, "find_friends.html", {'users': user_ls })


