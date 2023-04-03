# Importa a classe
from user import User
from post import Post

# Criando objetos
app_user_one = User("torquati@gmail.com", "Osvaldo Torquati", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("two@gmail.com", "Fulano", "psw2", "Estagiary")
app_user_two.get_user_info()

# Alterando os valores
app_user_one.change_job_title("DevOps Full Stack")
app_user_one.get_user_info()

# Criando outra classe para manipular outras informações
new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
