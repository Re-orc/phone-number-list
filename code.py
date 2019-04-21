def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[0] in phone_book[i][0:len(phone_book[0])]:
            answer = False
            
    return answer
