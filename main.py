from functools import reduce

talabalar = [
    {"ism": "Ali",  "baho": 85, "yosh": 20},
    {"ism": "Vali", "baho": 62, "yosh": 22},
    {"ism": "Soli", "baho": 91, "yosh": 19},
    {"ism": "Zebo", "baho": 74, "yosh": 21},
    {"ism": "Kamol","baho": 55, "yosh": 23},
]

# filter — 70 dan yuqori
a_talabalar = list(filter(lambda t: t["baho"] >= 70, talabalar))

# map — har birining bahosini 5 ga oshir (bonus)
bonus = list(map(lambda t: {**t, "baho": t["baho"] + 5}, talabalar))

# sorted — bahoga ko'ra kamayish tartibida
tartiblangan = sorted(talabalar, key=lambda t: t["baho"], reverse=True)

# reduce — o'rtacha baho
jami = reduce(lambda acc, t: acc + t["baho"], talabalar, 0)
ortacha = jami / len(talabalar)

if __name__ == "__main__":
    print("A talabalar:", [t["ism"] for t in a_talabalar])
    print("Bonus baho :", [t["baho"] for t in bonus])
    print("Reyting    :", [t["ism"] for t in tartiblangan])
    print(f"O'rtacha   : {ortacha:.1f}")
