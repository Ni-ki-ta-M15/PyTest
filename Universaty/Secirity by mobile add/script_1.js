function getTargetTime() {
  const targetInput = prompt("Будь ласка, введіть час для відліку у форматі hh.mm.ss:"); // Запитуємо в користувача час для відліку
  const targetTimeParts = targetInput.split("."); // Розбиваємо введений час на години, хвилини і секунди
  const targetDate = new Date(); // Створюємо новий об'єкт дати
  targetDate.setHours(targetTimeParts[0], targetTimeParts[1], targetTimeParts[2]); // Встановлюємо години, хвилини і секунди для цільової дати

  function updateCountdown() {
    const currentTime = new Date(); // Отримуємо поточний час
    const difference = targetDate - currentTime; // Розраховуємо різницю між цільовим часом і поточним часом

    const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)); // Розраховуємо кількість годин до цільового часу
    const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((difference % (1000 * 60)) / 1000);

    document.getElementById("hours").innerText = hours; // Відображаємо кількість годин на сторінці
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    if (difference < 0) {
      clearInterval(interval); // Зупиняємо відлік
      document.getElementById("timer").innerText = " Почалось! 🕑";
    }
  }

  const interval = setInterval(updateCountdown, 1000); // Запускаємо функцію updateCountdown кожну секунду
}
