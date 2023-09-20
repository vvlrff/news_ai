# Используем образ Node.js
FROM node:14

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости для фронтенда
COPY frontend/package.json frontend/package-lock.json /app/

# Устанавливаем зависимости
RUN npm install

# Копируем код фронтенда
COPY frontend/ /app/

# Указываем, что приложение должно быть запущено на порту 3000
EXPOSE 3000

# Запускаем npm start при запуске контейнера
CMD ["npm", "start"]