const navigation = document.querySelector("nav");
const header = document.querySelector("header");
const navigationLinks = document.querySelectorAll("nav a");
const projectsSection = document.querySelector("#projects");
const menuToggle = document.querySelector("#menu-toggle");
const topButton = document.querySelector("#top-button");
const githubUsername = "Logan-kim-the-philosopher";
const projectList = document.querySelector("#project-list");
const projectsStatus = document.querySelector("#projects-status");
const projectFilter = document.querySelector("#project-filter");
const languageFilter = document.querySelector("#language-filter");
let allRepositories = [];

const typingText = document.querySelector("#typing-text");

if (typingText) {
  const text = typingText.dataset.text;
  let index = 0;

  typingText.textContent = "";

  const typeNextCharacter = () => {
    if (index >= text.length) return;

    typingText.textContent += text[index];
    index += 1;
    setTimeout(typeNextCharacter, 80);
  };

  typeNextCharacter();
}

console.log(navigation.tagName);
console.log(navigationLinks.length);
console.log(projectsSection.tagName, projectsSection.id);

navigationLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();
    link.classList.toggle("active");
    console.log(`${link.textContent} 메뉴 active 상태: ${link.classList.contains("active")}`);

    const target = document.querySelector(link.getAttribute("href"));
    target.scrollIntoView({ behavior: "smooth" });
  });
});

menuToggle.addEventListener("click", () => {
  const isOpen = navigation.classList.toggle("active");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

window.addEventListener("scroll", () => {
  const isScrolled = window.scrollY >= 60;
  const passedHero = window.scrollY >= 300;

  navigation.classList.toggle("scrolled", isScrolled);
  header.classList.toggle("scrolled", isScrolled);
  document.body.classList.toggle("passed-hero", passedHero);

  console.log(`scrolled: ${isScrolled}, passedHero: ${passedHero}`);
});

topButton.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

const sections = document.querySelectorAll("main section");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 },
);

sections.forEach((section) => {
  observer.observe(section);
});

const themeToggle = document.querySelector("#theme-toggle");

const systemTheme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
const savedTheme = localStorage.getItem("theme") || systemTheme;
document.documentElement.dataset.theme = savedTheme;

themeToggle.addEventListener("click", () => {
  const isDark = document.documentElement.dataset.theme === "dark";
  const nextTheme = isDark ? "light" : "dark";

  document.documentElement.dataset.theme = nextTheme;
  localStorage.setItem("theme", nextTheme);
});

const contactForm = document.querySelector("#contact form");
const formStatus = document.querySelector("#form-status");

contactForm.addEventListener("submit", (event) => {
  const formData = new FormData(contactForm);
  const name = formData.get("name").trim();
  const email = formData.get("email").trim();
  const message = formData.get("message").trim();

  if (!name || !email || !message) {
    event.preventDefault();
    formStatus.textContent = "모든 필드를 입력해주세요.";
    return;
  }

  if (!email.includes("@")) {
    event.preventDefault();
    formStatus.textContent = "올바른 이메일을 입력해주세요.";
    return;
  }
});

const emailInput = document.querySelector("#email");

emailInput.addEventListener("input", () => {
  if (emailInput.value && !emailInput.value.includes("@")) {
    formStatus.textContent = "이메일 형식을 확인해주세요.";
    return;
  }

  formStatus.textContent = "";
});

async function fetchRepositories() {
  const apiUrl = `https://api.github.com/users/${githubUsername}/repos`;

  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`GitHub API 응답 오류: ${response.status}`);
    }

    const repositories = await response.json();
    console.log("GitHub 저장소를 불러왔습니다.", repositories.length);
    return { status: "success", repositories };
  } catch (error) {
    console.error("GitHub 저장소를 불러오지 못했습니다.", error);
    return { status: "error", repositories: [], message: error.message };
  }
}

function renderRepositories(result) {
  const { status, repositories, message } = result;

  if (status === "error") {
    projectsStatus.textContent = `GitHub 저장소를 불러오지 못했습니다. ${message}`;
    projectList.innerHTML = '<button id="projects-retry" type="button">다시 시도</button>';
    document.querySelector("#projects-retry").addEventListener("click", loadRepositories);
    return;
  }

  if (!repositories.length) {
    projectsStatus.textContent = "표시할 GitHub 저장소가 없습니다.";
    projectList.innerHTML = "";
    return;
  }

  projectsStatus.textContent = `${repositories.length}개의 GitHub 저장소를 불러왔습니다.`;
  projectList.innerHTML = repositories
    .map((repository) => {
      const description = repository.description || "설명이 등록되지 않은 저장소입니다.";

      return `
        <article>
          <h3>${repository.name}</h3>
          <p>${description}</p>
          <a href="${repository.html_url}">저장소 보기</a>
        </article>
      `;
    })
    .join("");
}

function filterRepositories() {
  const keyword = projectFilter.value.trim().toLowerCase();
  const language = languageFilter.value;
  const filteredRepositories = allRepositories.filter((repository) =>
    repository.name.toLowerCase().includes(keyword) &&
    (!language || repository.language === language),
  );

  renderRepositories({ status: "success", repositories: filteredRepositories });
}

projectFilter.addEventListener("input", filterRepositories);
languageFilter.addEventListener("change", filterRepositories);

async function loadRepositories() {
  projectsStatus.textContent = "GitHub 저장소를 불러오는 중입니다.";
  projectList.innerHTML = "";

  const result = await fetchRepositories();

  if (result.status === "success") {
    allRepositories = result.repositories;
  }

  renderRepositories(result);
}

loadRepositories();
