movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]

def retrieve_rating():
    user_input = int(input("평점 몇 이상의 영화를 조회하시겠습니까?"))
    print("[평점",user_input," 이상 영화]")
    for movie in movies:
        if movie["rating"] > user_input:
            print("- ", movie["title"])

def total_movie_views():
    total_animation_views = 0
    for movie in movies:
        if movie["genre"] == "애니메이션":
            total_animation_views = total_animation_views + movie["views"]
    print("[애니메이션 장르의 누적조회수]")
    print(total_animation_views)

def retrieve_max_views_movie():
    max_views = 0
    max_title = ""
    for movie in movies:
        if movie["views"] > max_views:
            max_views = movie["views"]
            max_title = movie["title"]
    print("[최다 조회수의 영화]")
    print(max_title, ":", max_views)

def search_movie_by_title(keyword):
    searched_movie = []
    for movie in movies:
        if movie["title"].find(keyword) >= 0:
            searched_movie.append(movie)
    return searched_movie

def search_movie_by_genre(keyword):
    searched_movie = []
    for movie in movies:
        if movie["genre"] == keyword:
            searched_movie.append(movie)
    return searched_movie

def search_movie():
    keyword = input("검색할 영화를 입력하세요")
    searched_movies_by_title = search_movie_by_title(keyword)
    searched_movies_by_genre = search_movie_by_genre(keyword)
    print(keyword, "가 이름으로 검색", searched_movies_by_title)
    print("--------------------")
    print(keyword, "장르로 검색된 영화", searched_movies_by_genre)

while True:
    print("====================")
    print("1. 평점 기준 조회")
    print("2. 장르별 누적조회수 조회")
    print("3. 최다 조회수 영화 조회")
    print("4. 영화 검색하기")
    print("0. 종료하기")
    print("====================")

    choice = int(input("Enter your choice:"))

    if choice == 0:
        break
    elif choice == 1:
        retrieve_rating()
    elif choice == 2:
        total_movie_views()
    elif choice == 3:
       retrieve_max_views_movie()
    elif choice == 4:
        search_movie()
    else:
        print("잘못된 입력입니다!!.")



