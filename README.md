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
### Портфолио:
![Project Image](https://github.com/miavien/message-board/blob/1cf8e4f4940288fa3ceb95d3ee60fbd0ba8837c2/mmorpg/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0.jpg)
![Project Image](https://github.com/miavien/message-board/blob/1cf8e4f4940288fa3ceb95d3ee60fbd0ba8837c2/mmorpg/%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D1%8C.jpg)
