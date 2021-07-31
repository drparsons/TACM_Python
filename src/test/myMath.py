class myMath:
    def add(self, num1, num2):
        return int(num1 + num2)


class myMath2:
    def add(num1, num2):
        return int(num1 + num2)

if __name__ == "__main__":
    print(myMath2.add(1,1))
    m = myMath()
    print(m.add(2, 2))