if __name__ == '__main__':
    while True:
        # key: English word
        # value: Korean meaning
        dictionary = {'apple': '사과', 'banana': '바나나', 'peach': '복숭아', 'cherry': '체리'}
        word = input('영어 단어를 입력하시요 : ')
        if word in dictionary: # if the word is in the dictionary
            # print the meaning of it
            print(dictionary[word])
        else: # if the word is not in the dictionary
            # save the word and the meaning of it
            dictionary[word] = input('한글 뜻을 입력하시오 : ')
        print(dictionary) # print the dictionary