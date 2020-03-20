import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apartment.settings")
django.setup()

from app.models import apartment, User, evaluation


Insert_apartment = [
    (1, 'Aparto, Glasgow West End', 'Minimum￡150/Week',
     'Glasgow West End provides a global study accommodation for glasgow students. Students from all over the world gather here and all kinds of possibilities alternate. No matter in the meeting area, study area or music room of the apartment, you have enough space and place to talk and communicate with the new friends you are about to meet. Stay in Glasgow West End and experience the western life with bohemian flavor. In your spare time, go shopping, visit various galleries, watch sports events or go',
     'The apartment building is equipped with a 24-hour electronic entrance guard system and video surveillance system, and provides you with property insurance to ensure your personal property and personal safety. The dormitory is also equipped with its own independent equipment maintenance team. Any problems with dormitory facilities can be reported directly to the front desk of the dormitory.',
     'The apartment provides you with Studio and ensuite room types. studio has independent bathroom, independent kitchen, microwave oven, stove, oven, refrigerator and other infrastructure facilities. Each room has high-speed WIFI, desk, chair and plenty of storage space for your item management. Glasgow West End has a conference area, a library, an entertainment centeEnvironment and transportation:r, a coffee shop, a gym, etc. to enrich your life in Glasgow.',
     '145 Kelvinhaugh St, Glasgow, G3 8PX', 5,
     'The apartment is close to  University of Glasgow, and the Gilmorehill Centre campus is about 19 minutes\' walk away. It is very convenient to go to school. The nearest railway station to the apartment is the Exhibition Centre, which takes about 12 minutes on foot. To the Garscube campus, you can walk about 11 minutes to the Exhibition Centre railway station, take about 8 minutes of train and walk another 10 minutes. On the way to school, you will also pass the Kevin Grove Art Museum, 8 minutes walk from the apartment. To go to Glasgow Calidoni Ann University, you need to walk about 34 minutes, or walk about 6 minutes to Derby Street Station, and take a bus about 11 minutes to reach the school.\r\n\r\n● Cafe: Lorne Hotel Glasgow\r\n● ATM: Nationwide\r\n● parking lot: hotel restaurant campanile glasgow secc-hydro',
     0, '2020-03-15 07:07:29.509293', '2020-03-15 07:07:29.509293',
     '[\'Aparto, Glasgow West End.jpeg\',\'GYM.jpg\',\'Playroom.jpeg\',\'Public area (2).jpeg\',\'Public area.jpeg\',\'reception.jpg\',\'Shared Apartments.jpg\',\'Toilet.jpg\',\'true Club Suites.jpeg\',\'Aparto, Glasgow West Endmap.jpg\']',
     'https://www.google.com/maps/place/aparto,+Glasgow+West+End/@55.8640301,-4.294904,17z/data=!3m1!4b1!4m5!3m4!1s0x488845d7081005ad:0x817dbb0b34ec784d!8m2!3d55.8640301!4d-4.2927153'),
    (2, 'Scotway House', 'Minimum￡146/Week',
     'Scotway House is a modern and distinctive student residence in Glasgow. It is conveniently located near the University of Glasgow. It takes about 15 minutes on foot and is close to the Clyde River. The apartment is ideal for learning and socializing. The interior is warm and comfortable and livable. The community has modern facilities and a beautiful environment.',
     'Gym, Recreation Room, Movie Room, Conference Room, Study Room, Laundry Room, ETC. The rent includes: WI-FI, Water, Electricity, Heating. Environment and transportation:Two supermarkets, the subway and the train.',
     '1.250 megabit high speed network 		2.24*7 apartment services and security',
     'Scotway House, 165 Castlebank St, Glasgow G11 6EU', 4, 'Two supermarkets, the subway and the train.', 0,
     '2020-03-15 16:09:09.876622', '2020-03-15 16:09:09.876622',
     '[\"Scotway House Balcony.jpg\",\"Scotway House Apartment A.jpg\",\"Scotway House Apartment B.jpg\",\"Scotway House GYM.jpg\",\"Scotway House Meeting Room.jpg\",\"Scotway House Playroom.jpg\",\"Scotway House Public Area.jpg\",\"Scotway House Toilet.jpg\",\"Scotway House MAP.png\"]',
     'https://www.google.com/maps/place/Scotway+House+Student+Accommodation+(BOHO)/@55.868998,-4.3104024,17z/data=!4m5!3m4!1s0x4888450fbffcd8c5:0x308f4ce9cd8a8ee0!8m2!3d55.8680469!4d-4.3083425?hl=en'),
    (3, 'Tramworks', 'Minimum￡155/Week',
     'Tramworks is a collection of excellent student flats in Glasgow by Unite Students, one of the UK\'s largest apartment companies, offering en-suite and studio. If you choose the en-suite type, you will need to share the kitchen with 4-5 people, the kitchen provides refrigerator, microwave oven, oven, stove, exhaust hood and other facilities. Tramworks has its own bathroom in each bedroom, complete with desk, Wardrobe, curtains, mirrors, cable outlets, and a large storage space under the bed for st',
     'Gym, Recreation Room, Movie Room, Conference Room, Study Room, Laundry Room, ETC. The rent includes: WI-FI, Water, Electricity, Heating.1.Near the city center, the University of Glasgow campus is a few minutes\'walk away 		2.24*7 apartment services and security',
     'WI-FI, Water, Electricity, Heating.', '107 Kelvinhaugh Street, Glasgow G3 8PX', 4,
     'Tramworks, near the Clyde River in Glasgow, is about an eight-minute walk from the flats to the river\'s edge, sainsbury\'s is just a few minutes\'walk away, and Argyle road, about five minutes\'walk away, offers convenience stores, restaurants and takeout. The Morrison hypermarket is located on Dumbarton Road, a 10-minute walk from the apartment, and a five-minute taxi ride for students to shop for supplies.',
     0, '2020-03-16 16:14:53.497216', '2020-03-16 16:14:53.497216',
     '[\"Tramworks.jpeg\",\"Tramworks bathroom.jpeg\",\"Tramworks common-room.jpeg\",\"Trameworks en-suit.jpeg\",\"Trameworks GYM.jpeg\",\"Trameworks public-kitchen.jpeg\",\"Trameworks reception.jpeg\",\"Trameworks studio.jpeg\",\"Trameworks study-room.jpeg\",\"Trameworks map.jpeg\"]',
     'https://www.google.com/maps/place/Tramworks/@55.864193,-4.2933732,17z/data=!3m1!4b1!4m5!3m4!1s0x488845d65f63b85f:0xe7ee1d14074bc0d2!8m2!3d55.86419!4d-4.2911845?hl=en'),
    (4, 'Vita Student Glasgow', 'Minimum￡190/Week',
     'Vita Student Glasgow is a premier student residence in Glasgow, designed to provide students with a high-quality living environment. The apartment is located in the heart of the West District, with all the surrounding living facilities and convenient transportation. It is close to the University of Glasgow and is an ideal residence for students of the school. The apartment offers high-end Studio room types, fully furnished, and can be directly moved in. The price of rooms in an apartment varies',
     'Gym, Recreation Room, Movie Room, Conference Room, Study Room, Laundry Room, ETC. 1.Offer weekday breakfast 		2.250 megabit high speed network 		3.24*7 apartment services and security',
     'WI-FI, Water, Electricity, Heating.', '21 Beith St, Glasgow G11 6BZ', 5,
     'Two supermarkets, the subway and the train.It\'s only ten minutes\' walk to the university of Glasgow', 0,
     '2020-03-16 16:18:08.274308', '2020-03-16 16:18:08.274308',
     '[\"Vita Student Glasgow Vita.jpg\",\"Vita Student Glasgow Apartment A.jpg\",\"Vita Student Glasgow Apattment B.jpg\",\"Vita Student Glasgow GYM.jpg\",\"Vita Student Glasgow Meeting room.jpg\",\"Vita Student Glasgow Playroom.jpg\",\"Vita Student Glasgow Toilet.jpg\",\"Vita Student Glasgow Vita Public kitchen.jpg\",\"Vita Student Glasgowmap.png\"]',
     'https://www.google.com/maps/place/Vita+Student+Glasgow/@55.869016,-4.3079844,17z/data=!3m1!4b1!4m5!3m4!1s0x488845db9dab9b09:0xf6c13214c2aa4ff9!8m2!3d55.869016!4d-4.3057957?hl=en'),
    (5, 'Woodside House', 'Minimum￡181/Week',
     'Woodside House Apartment is located in the west of Glasgow and is very close to the Gilmorehill Centre campus of Glasgow University. Although it is not close to the city center, it is only 2 minutes\' walk to Kelvinbridge subway station. It is very convenient to go to the city center, Glasgow Caledonia University and university of strathclyde. The Woodside House apartment is conveniently located with Tesco downstairs, several restaurants within a 2-or 3-minute walk, and a large park nearby. In ad',
     'In addition to the basic facilities, Woodside House Apartment is also equipped with a 24-hour monitoring system. Foreign personnel need to pass through multiple entrance guards to enter and leave without worrying about safety issues. The apartment is also equipped with a professional maintenance team and front desk service to help you solve your problems 24 hours a day.The apartment offers a variety of studio room types, with a total of 91 bedrooms. All rooms are individually designed, decorated',
     'WI-FI, Water, Electricity, Heating.', 'Woodside House,90 South Woodside Road,Glasgow, G20 6NL', 2,
     'Woodside House Apartment is located in the west of Glasgow and is very close to the Gilmorehill Centre campus of Glasgow University. Although it is not close to the city center, it is only 2 minutes\' walk to Kelvinbridge subway station. It is very convenient to go to the city center, Glasgow Caledonia University and university of strathclyde.\r\nThe Woodside House apartment is conveniently located with Tesco downstairs, several restaurants within a 2-or 3-minute walk, and a large park nearby. In addition, there are various famous scenic spots in the center of the city, such as art exhibition hall, large shopping malls, cinemas and supermarkets, as well as commercial streets such as George Square.',
     0, '2020-03-16 16:22:11.322812', '2020-03-16 16:22:11.322812',
     '[\"Woodside.jpg\",\"Woodside House Apartment A.jpg\",\"Woodside House Apartment B.jpg\",\"Woodside House Apartment C.jpg\",\"Woodside House cinema .jpg\",\"Woodside House GYM.jpg\",\"Woodside House Meeting room.jpg\",\"Woodside House Playroom.jpg\",\"Woodside House Public area.jpg\",\"Woodside House Public kitchen.jpg\",\"Woodside House.jpg\",\"Woodside House map.jpg\"]',
     'https://www.google.com/maps/place/Woodside+House+-+Fresh+Student+Living/@55.875628,-4.2794897,17z/data=!3m1!4b1!4m5!3m4!1s0x4888443232c243fb:0xe69d5d7a14ebc4a1!8m2!3d55.875628!4d-4.277301'),
]

Insert_evalution = [
    (1, 1, 4, 3, 2, 1, 'good ', '2020-03-16 15:29:52.506247', '2020-03-16 15:29:52.506247', '8nJ4bShNW8F7uf3HLWFikP'),
    (2, 1, 4, 4, 3, 5, 'test', '2020-03-16 15:31:26.116149', '2020-03-16 15:31:26.116149', '8nJ4bShNW8F7uf3HLWFikP'),
    (3, 1, 5, 5, 5, 5, 'goooood!!!!!',
     '2020-03-16 06:47:11.810483', '2020-03-16 06:47:11.810483', '8nJ4bShNW8F7uf3HLWFikP'),
    (4, 2, 5, 5, 5, 5, 'nice', '2020-03-16 02:26:50.961343', '2020-03-16 02:26:50.961343', '8nJ4bShNW8F7uf3HLWFikP'),
]

Insert_user = [
    ('8nJ4bShNW8F7uf3HLWFikP', 'DDT', '1@qq.com', 'e0cf678eee29810b837cbb60d041912c87b0e5f0fa5aaa2c3d1b3c009cd031fa', '145 Kelvinhaugh St, Glasgow, G3 8PX',
     '[\'1\', \'5\', \'2\', \'3\']'),
]

Insert_auth_user = [
    (1, 'pbkdf2_sha256$100000$vFPQtDKV1mnf$g2q0yVSkKx/iWE/cMmWSkkLHLC5+jKhDWgiDqgY1SV4=', '2020-03-15 16:00:04.082030',
     1, 'DDT', '', '', '1@google.com', 1, 1, '2020-02-25 06:48:30.982732'),
]


def registerUserData():
    print("Start Register User data")
    for user in Insert_user:
        print("Register User:", user)
        User.objects.get_or_create(uid=user[0], username=user[1], email=user[2], password=user[3], address=user[4]
                                   , favorite=user[5])
    print("Register User data OK!")


def registerApartmentData():
    print("Start Register Apartment data")
    for apart in Insert_apartment:
        print("Register apartment:", apart)
        apartment.objects.get_or_create(
            id=apart[0],
            name=apart[1],
            price=apart[2],
            information=apart[3],
            facilities=apart[4],
            rent_includes=apart[5],
            address=apart[6],
            score=apart[7],
            comments=apart[8],
            is_delete=apart[9],
            # create_time=apart[10],
            # update_time=apart[11],
            img=apart[12],
            address_link=apart[13]
        )
    print("Register Apartment data OK!")


def registerEvaluationData():
    print("Start Register Evaluation data")
    for eva in Insert_evalution:
        print("Register evalution:", eva)
        evaluation.objects.get_or_create(
            id=eva[0],
            apartment_id=eva[1],
            environment=eva[2],
            staff_service=eva[3],
            security=eva[4],
            cost_performance=eva[5],
            comment=eva[6],
            # create_time=eva[7],
            # update_time=eva[8],
            user_id=eva[9],
        )
    print("Register Evaluation data OK!")


# start run
def setup():
    # makemigrations cmd
    os.system("python manage.py makemigrations")
    # migrate cmd
    os.system("python manage.py migrate")
    # register data
    registerUserData()
    registerApartmentData()
    registerEvaluationData()


if __name__ == "__main__":
    setup()