# def add_two_nums(num1: int, num2: int) -> int:
#     return num1 + num2

# print(__name__)

# if __name__=="__main__":
#     print(f"5+18={add_two_nums(5,18)}")
#     print('This line should not run if you import add_two_numbers')

# import requests
# def download(url):
#     result = requests.get(url=url)
#     return result.ok

# url_list = [
#     'https://google.com',
#     'https://hossein.codes',
#     #'https://exa---mple.com'
# ]

# # result = list(map(download, url_list))
# # print(result)

# for website in url_list:
#     print(download(website))

# x = 5
# x= 2

# class Myclass:
    
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, m):
#         self.__x = m

# c = Myclass()
# c.x =5 
# print(c.x)


def myfunc(x:int)->None:
    print(x+x)
    return 0

a:str= '5'
myfunc(a)