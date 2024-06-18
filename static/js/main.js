document.addEventListener("DOMContentLoaded", () => {
  const profileButtonData = document.getElementById("js-profile-button");
  profileButtonData.addEventListener("click", (e) => {
    document.getElementById("js-profile-menu").classList.toggle("open-menu");
  });
});
