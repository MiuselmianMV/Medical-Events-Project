function localizeSelectors() {
    document.querySelectorAll(".selector").forEach(function (selector) {
        const availableBox = selector.querySelector(".selector-available");
        const chosenBox = selector.querySelector(".selector-chosen");

        if (availableBox) {
            const availableTitle = availableBox.querySelector("h2");
            const availableHelp = availableBox.querySelector(".helptext");
            const availableFilter = availableBox.querySelector("input[type='text']");
            const chooseAllBtn = availableBox.querySelector(".selector-chooseall");

            if (availableTitle) {
                availableTitle.textContent = "Доступні спеціальності";
            }

            if (availableHelp) {
                availableHelp.textContent = "Оберіть спеціальності та натисніть кнопку «Додати».";
            }

            if (availableFilter) {
                availableFilter.placeholder = "Фільтр";
            }

            if (chooseAllBtn) {
                chooseAllBtn.textContent = "Обрати всі спеціальності";
            }
        }

        if (chosenBox) {
            const chosenTitle = chosenBox.querySelector("h2");
            const chosenHelp = chosenBox.querySelector(".helptext");
            const chosenFilter = chosenBox.querySelector("input[type='text']");
            const clearAllBtn = chosenBox.querySelector(".selector-clearall");

            if (chosenTitle) {
                chosenTitle.textContent = "Обрані спеціальності";
            }

            if (chosenHelp) {
                chosenHelp.textContent = "Щоб прибрати спеціальності, виділіть їх і натисніть кнопку «Видалити».";
            }

            if (chosenFilter) {
                chosenFilter.placeholder = "Фільтр";
            }

            if (clearAllBtn) {
                clearAllBtn.textContent = "Прибрати всі спеціальності";
            }
        }
    });

    document.querySelectorAll(".related-widget-wrapper-link").forEach(function (link) {
        const title = link.getAttribute("title") || "";

        if (title.includes("Add another")) {
            link.setAttribute("title", "Додати нову картку");
        }
        if (title.includes("Change selected")) {
            link.setAttribute("title", "Редагувати вибрану картку");
        }
        if (title.includes("Delete selected")) {
            link.setAttribute("title", "Видалити вибрану картку");
        }
        if (title.includes("View selected")) {
            link.setAttribute("title", "Переглянути вибрану картку");
        }
    });
}

function localizeChangeListTexts() {
    document.querySelectorAll("h1").forEach(function (el) {
        const text = el.textContent.trim();

        if (text.startsWith("Select ") && text.endsWith(" to change")) {
            const modelName = text
                .replace("Select ", "")
                .replace(" to change", "");
            el.textContent = `Оберіть ${modelName} для редагування`;
        }
    });

    document.querySelectorAll("a, button, input[type='submit'], label, option").forEach(function (el) {
        const text = el.textContent ? el.textContent.trim() : "";
        const value = el.value ? el.value.trim() : "";

        if (text === "Search") el.textContent = "Пошук";
        if (value === "Search") el.value = "Пошук";

        if (text === "Run") el.textContent = "Виконати";
        if (value === "Run") el.value = "Виконати";

        if (text === "Action:") el.textContent = "Дія:";
    });

    document.querySelectorAll("input[type='search'], input[name='q']").forEach(function (input) {
        if (!input.placeholder || input.placeholder === "Search") {
            input.placeholder = "Пошук";
        }
        if (input.getAttribute("aria-label") === "Search") {
            input.setAttribute("aria-label", "Пошук");
        }
    });

    document.querySelectorAll(".action-counter, span.action-counter").forEach(function (el) {
        const text = el.textContent.trim();
        const match = text.match(/^(\d+)\s+of\s+(\d+)\s+selected$/i);

        if (match) {
            const selected = match[1];
            const total = match[2];
            el.textContent = `Вибрано ${selected} з ${total}`;
        }
    });

    document.querySelectorAll("select option").forEach(function (option) {
        const text = option.textContent.trim();

        if (text === "---------") return;
        if (text === "Delete selected cards") option.textContent = "Видалити вибрані картки";
        if (text === "Delete selected events") option.textContent = "Видалити вибрані події";
        if (text === "Delete selected specialties") option.textContent = "Видалити вибрані спеціальності";
        if (text === "Delete selected users") option.textContent = "Видалити вибраних користувачів";
        if (text === "Delete selected") option.textContent = "Видалити вибране";
    });
}

function simplifyActionsBar() {
    const select = document.querySelector(".actions select");
    const label = document.querySelector(".actions label");
    const counter = document.querySelector(".action-counter");

    if (!select) return;

    // скрываем label и select
    if (label) label.style.display = "none";
    select.style.display = "none";

    // меняем текст кнопки
    const button = document.querySelector(".actions button, .actions input[type='submit']");
    if (button) {
        if (button.tagName === "INPUT") {
            button.value = "Видалити вибране";
        } else {
            button.textContent = "Видалити вибране";
        }
    }

    // автоматически выбираем delete selected
    select.value = select.options[1]?.value || "";
}

function localizeAdminTexts() {


    document.querySelectorAll("a, button, input[type='submit']").forEach(function (el) {
        const value = el.value ? el.value.trim() : "";
        const text = el.textContent ? el.textContent.trim() : "";

        if (value === "Save") el.value = "Зберегти";
        if (value === "Save and add another") el.value = "Зберегти і додати ще";
        if (value === "Save and continue editing") el.value = "Зберегти і продовжити редагування";
        if (value === "Delete") el.value = "Видалити";
        if (value === "Close") el.value = "Закрити";

        if (text === "Add") el.textContent = "Додати";
        if (text === "Change") el.textContent = "Редагувати";
        if (text === "History") el.textContent = "Історія";
        if (text === "Delete") el.textContent = "Видалити";
        if (text === "View site") el.textContent = "Переглянути сайт";
        if (text === "Change password") el.textContent = "Змінити пароль";
        if (text === "Log out") el.textContent = "Вийти";
    });

    document.querySelectorAll(".object-tools a").forEach(function (link) {
        const text = link.textContent.trim();

        if (text === "History") {
            link.textContent = "Історія";
        }

        if (text === "Delete") {
            link.textContent = "Видалити";
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    localizeSelectors();
    localizeAdminTexts();
    localizeChangeListTexts();
    simplifyActionsBar();

    setTimeout(simplifyActionsBar, 150);
    setTimeout(simplifyActionsBar, 500);

    setTimeout(localizeSelectors, 150);
    setTimeout(localizeSelectors, 500);

    setTimeout(localizeAdminTexts, 150);
    setTimeout(localizeAdminTexts, 500);

    setTimeout(localizeChangeListTexts, 150);
    setTimeout(localizeChangeListTexts, 500);
});