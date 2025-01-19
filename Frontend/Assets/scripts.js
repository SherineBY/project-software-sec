document.addEventListener('DOMContentLoaded', () => {
    console.log('Challenge Platform Loaded!');
});

function togglePanel() {
    const panel = document.getElementById("result-panel");
    panel.style.display = panel.style.display === "none" ? "block" : "none";
}
