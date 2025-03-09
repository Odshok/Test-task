import gitlab

print("start")

gl = gitlab.Gitlab(url='http://192.168.2.74', private_token='glpat-nhEboMgFHSPrvYP8FcZT')

gl.auth()

# create a new user
user_data = {'email': 'email@example.com', 'username': 'bus', 'name': 'bus', 'password': '00superpass'}
user = gl.users.create(user_data)
print("Вся информация о новом пользователе: " + user)



print("Пользователь:" + user_data['email'] + " " + user_data['username'] )