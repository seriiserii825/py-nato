def lesson():
    facebook_posts = [
            {"Likes": 21, "Comments": 2},
            {"Likes": 13, "Comments": 2},
            {"Likes": 33, "Comments": 8},
            { "Comments": 1},
            { "Comments": 1},
            {"Likes": 3, "Comments": 1},
            ]
    total_likes = 0
    for post in facebook_posts:
        try:
            total_likes += post["Likes"]
        except KeyError as error_message:
            print(f"Key doesn't exists: {error_message}")
        else:
            print(f"Post processed successfully")
    print(f"Total likes: {total_likes}")
