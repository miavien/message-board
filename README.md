# Проект "Доска объявлений"
Доска объявлений - интернет-портал для сообщества mmorpg-игры. Ресурс предназначен для публикации и просмотра объявлений игроков: поиска команды, обмена ресурсами, поиска гильдии и др.

## Функционал сайта:
- Главная страница, на которой отображаются все посты;
- добавление постов разрешено только зарегистрированным пользователям. С помощью редактора ***CKEditor*** реализована возможность в посты добавлять изображения, видео и расширенные возможности оформления текста;
- личная страница пользователя, на которой он может просматривать отклики-комментарии на собственные посты. Отклик можно принять или отклонить;
- можно подписаться на любимую категорию постов (Танк, ДД, Хил, Торговец и др.)

**Регистрация** пользователя происходит с указанием почты и отправки на неё индивидуального кода, который нужно ввести в окно для подтверждения запроса.

С помощью _Redis и Celery_ настроена отправка писем пользователю на почту в случаях:
- Появления нового поста в любимой категории;
- нового отклика на пост пользователя;
- о принятии отклика автором поста.

В проекте используется ***база данных***, работа с которой ведётся с помощью ORM-команд.

---
Портфолио:
