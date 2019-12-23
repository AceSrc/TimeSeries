import hotsax
import wat
import bruteforce
def work(filename):
    with open(filename, 'r') as fd:
        s = [float(line.split(',')[1]) for line in fd]
        bruteforce_result = bruteforce.BRUTEFORCE().calc(s, 128)
        wat_result = wat.WAT().calc(s, 7) # 128 = 2 ** 7, so order=7
        hotsax_result1 = hotsax.HOTSAX().calc(s, 128, 64)
        hotsax_result2 = hotsax.HOTSAX().calc(s, 128, 32)
        hotsax_result3 = hotsax.HOTSAX().calc(s, 128, 16)

        print(bruteforce_result)
        print(wat_result)
        print(hotsax_result1)
        print(hotsax_result2)
        print(hotsax_result3)
        print("")

if __name__ == '__main__':
    work('speed_t4013.csv')
    work('speed_7578.csv')
    work('speed_6005.csv')