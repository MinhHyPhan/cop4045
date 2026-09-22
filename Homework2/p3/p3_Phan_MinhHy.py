import csv

#a)
def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Add a user with no friends; return False if the username exists."""
    try:
        if username in sn:
            return False
        sn[username] = (fullname, [])
        return True
    except Exception:
        print("Unable to add the user, dear manager.")
        raise
#b)
def add_friend(sn: dict, user1: str, user2: str) -> bool:
    try:
        if user1 not in sn or user2 not in sn or user1 == user2:
            return False

        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)
        return True
    except Exception:
        print("Unable to add the friendship, dear manager bud")
        raise
#c)
def get_friends(sn: dict, user1: str, distance: int) -> list[str]:
    try:
        if type(distance) != int or distance < 1:
            raise ValueError("Distance must be a positive integer.")
        if user1 not in sn:
            return []

        friends = []
        visited = [user1]
        current_users = [user1]

        for level in range(distance):
            next_users = []
            for username in current_users:
                for friend in sn[username][1]:
                    if friend not in visited:
                        visited.append(friend)
                        friends.append(friend)
                        next_users.append(friend)
            current_users = next_users
            if current_users == []:
                break

        return friends
    except Exception:
        print("Unable to find friends. Check the filename again, dear manager.")
        raise
#d)
def save_network(filename: str, sn: dict) -> None:
    try:
        with open(filename, "w", newline="", encoding="utf-8") as write_file:
            writer = csv.writer(write_file)
            for username in sn:
                fullname = sn[username][0]
                friends = sn[username][1]
                writer.writerow([username, fullname] + friends)
    except Exception:
        print("Unable to save the network. Might want to check that filename!")
        raise
#e)
def load_network(filename: str) -> dict:
    try:
        sn = {}
        with open(filename, "r", newline="", encoding="utf-8") as read_file:
            reader = csv.reader(read_file, strict=True)
            for row in reader:
                if len(row) < 2:
                    raise ValueError("Each CSV row needs a username and full name.")
                username = row[0]
                if username in sn:
                    raise ValueError("The CSV contains a repeated username.")
                sn[username] = (row[1], row[2:])
        return sn
    except Exception:
        print("Unable to load the network. Check the filename and CSV contents. GG")
        raise


def main():
    print("Name: Minh Hy Phan")
    print("Student ID: Z23766758")
    """Test adding users, friendships, distance searches, and CSV storage."""
    try:
        sn = {}

        # a) testing
        print("Add Alice:", add_user(sn, "alice", "Alice Smith"))
        print("Add Alice again:", add_user(sn, "alice", "Alice Smith"))
        add_user(sn, "maria", "Maria Cortez")
        add_user(sn, "joe", "Joseph Adams")
        add_user(sn, "eve", "Evelyn Cooper")
        add_user(sn, "david", "David Benson")

        # b) testing
        print("Link Alice and Maria:", add_friend(sn, "alice", "maria"))
        add_friend(sn, "maria", "joe")
        add_friend(sn, "maria", "david")
        add_friend(sn, "joe", "eve")
        print("Link an unknown user:", add_friend(sn, "alice", "unknown"))
        print("Repeat Alice and Maria link:", add_friend(sn, "alice", "maria"))

        # c) testing
        print("Alice, distance 1:", get_friends(sn, "alice", 1))
        print("Alice, distance 2:", get_friends(sn, "alice", 2))
        print("Alice, distance 3:", get_friends(sn, "alice", 3))
        print("Unknown user:", get_friends(sn, "unknown", 1))

        # d) and e) testing
        filename = "social_network.csv"
        save_network(filename, sn)
        loaded_network = load_network(filename)
        print("Loaded network:", loaded_network)
        print("Saved and loaded networks match:", loaded_network == sn)
    except Exception:
        print("The network tests could not finish. See the error details below.")
        raise

if __name__ == "__main__":
    main()