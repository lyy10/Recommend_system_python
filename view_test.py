#
# 用户命令行交互界面
# June,19 2018 By Lyy
import sys
sys.path.append('./recommend/')
sys.path.append('./spider/')
import interface
def print_main():
    print('    Hello, Welcome to recommend system')
    print('\n\n    Copyright by Lyy')
    print('\n1. get recommend movies\n2. watch movies I have watched\n3. quit')
    print('\n请输入相关选项')

def print_moviedetail(movie):
    print('电影ID: ', movie.Mid)
    print('电影名字: ', movie.Name)
    print('电影平均分: ', movie.average_score)
    print('发布日期: ', movie.release_data)
if __name__=='__main__':
    sign = 3
    while sign:
        user_id = input('请输入用户ID:')
        password = input('请输入密码:')
        u_id = interface.accessCheck(user_id, password)
        if u_id:
            break
        print('您的账号和密码不匹配，请重试')
        sign -= 1
    if sign == 0:
        print('对不起，请下次再试')
        sys.exit()
    user_id = u_id
    while 1:
        print_main()
        print('您的用户ID为:',user_id)
        user_in = input()
        if user_in is '1':
            user = interface.get_recommend_movie(int(user_id))
            for l in range(len(user.movies)):
                print_moviedetail(user.movies[l])
                conmand = input('默认回车显示显示下一条,输入 q 退出:')
                if conmand is 'q':
                    break
        elif user_in is '2':
            user = interface.getUserHaveWatch(int(user_id))
            for l in range(len(user.movies)):
                print_moviedetail(user.movies[l])
                conmand = input('默认回车显示显示下一条,输入 q 退出:')
                if conmand is 'q':
                    break
        elif user_in is '3':
            sys.exit()

