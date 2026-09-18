from django.shortcuts import render


def home(request):
    train = {
        "train_no": "12951",
        "train_name": "Mumbai Rajdhani Express",
        "source": "Mumbai Central",
        "destination": "New Delhi",
        "departure": "17:00",
        "arrival": "08:35",
    }
    return render(request, "home.html", {"train": train})


def train_search(request):
    trains = [
        {
            "train_no": "12951",
            "train_name": "Mumbai Rajdhani Express",
            "source": "Mumbai Central",
            "destination": "New Delhi",
            "departure": "17:00",
            "arrival": "08:35",
        },
        {
            "train_no": "12002",
            "train_name": "Bhopal Shatabdi Express",
            "source": "New Delhi",
            "destination": "Bhopal",
            "departure": "06:00",
            "arrival": "14:00",
        },
        {
            "train_no": "12301",
            "train_name": "Howrah Rajdhani Express",
            "source": "New Delhi",
            "destination": "Howrah",
            "departure": "16:55",
            "arrival": "10:00",
        },
    ]
    return render(request, "trains.html", {"trains": trains})


def passenger_details(request):
    passenger = {
        "name": "Aditi",
        "age": 20,
        "gender": "Female",
        "coach": "B1",
        "berth": "Side Lower",
    }
    return render(request, "passenger.html", {"passenger": passenger})


def booking_confirmation(request):
    passenger_name = "Aditi"
    train = {
        "train_no": "12951",
        "train_name": "Mumbai Rajdhani Express",
        "source": "Mumbai Central",
        "destination": "New Delhi",
    }
    passenger = {
        "coach": "B1",
        "berth": "Side Lower",
    }
    context = {
        "passenger_name": passenger_name,
        "train": train,
        "passenger": passenger,
    }
    return render(request, "confirmation.html", context)


