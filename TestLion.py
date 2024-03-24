def main() :
    print('hello, world!')
    print('what the fox say')
    print('this is sub main branch')

    likeList = [[1,2,3,4,5],[0,6,7,8,9]]

    for i in likeList :
        for j in i :
            print(j+", ")

    print('finish')

if __name__ == '__main__' :
    main()