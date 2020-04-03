from Service.Service import Service


def main():
    easy = ["input/50p_easy_01_tsp.txt", "input/50p_hard_01_tsp.txt", "input/50p_medium_01_tsp.txt"]
    medium = "input/100p_fricker26.txt"
    hard = "input/150p_eil51.txt"

    files = ["input/easy_01_tsp.txt", "input/medium_01_tsp.txt", "input/hard_01_tsp.txt"]

    serv = Service(files[1])
    serv.solve()


main()
