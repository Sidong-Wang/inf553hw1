from pyspark import SparkContext

import json

def map_a(res):
    return ('review_count', 1)


def count_a(a,b):
    return a+b\

def map_b(res, y):
    pass


def main(argv):
    sc = SparkContext(appName="inf553hw1")
    with open(argv[1], 'r') as load_f:
        load_dict = json.load(load_f)

    rdd = sc.parallelize(load_dict)

    rdd_a = rdd.map(map_a).reduceByKey(count_a)



if __name__ == '__main__':
    sys.exit(main(sys.argv))