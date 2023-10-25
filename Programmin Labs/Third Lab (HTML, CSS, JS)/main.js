// Добавление плавной прокрутки для якорных ссылок
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const target = document.getElementById(targetId);

        if (target) {
            window.scrollTo({
                top: target.getBoundingClientRect().top + window.scrollY,
                behavior: 'smooth'
            });
        }
    });
});

// Получаем ссылку на кнопку и секцию
const toggleButton = document.getElementById("toggleButton");
const portfolioHead = document.getElementById("portfolio_head");
const portfolioSection = document.getElementById("portfolio_section");

function changeBorderRadiusBottomLeft(radius) {
    portfolioHead.style.borderBottomLeftRadius = `${radius}px`;
  }
  function changeBorderRadiusBottomRight(radius) {
    portfolioHead.style.borderBottomRightRadius = `${radius}px`;
  }

toggleButton.addEventListener("click", function(){
    if (portfolioSection.style.display === "none") {
        portfolioSection.style.display = "block"; // Показываем секцию при клике
        changeBorderRadiusBottomLeft(0);
        changeBorderRadiusBottomRight(0);
        portfolioHead.classList.remove("spaced-contacts");
        toggleButton.textContent = "v";
        toggleButton.classList.add('hvr-grow')
      } else {
        portfolioSection.style.display = "none"; // Скрываем секцию при следующем клике
        portfolioHead.classList.add("spaced-contacts");
        changeBorderRadiusBottomLeft(10);
        changeBorderRadiusBottomRight(10);
        toggleButton.textContent = ">"
        toggleButton.classList.add('hvr-grow')
      }
});