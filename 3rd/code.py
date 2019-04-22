import numpy

birth = 2002

iterations = 0
while True:
    iterations += 1
    numbers = numpy.random.randint(0, 400, size=(4, 4))

    middle = numbers[1:-1, 1:-1]
    allsum = sum(sum(numbers))
    middlesum = sum(sum(middle))
    bordersum = allsum - middlesum

    if bordersum == birth:
        print(f"sum of border values ({bordersum}) are equal to my birth year {birth}")
        print(f"calculating this took {iterations} iteration(s)")
        break