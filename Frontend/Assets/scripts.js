document.addEventListener("DOMContentLoaded", () => {
    fetch('/challenges')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('challenges-container');
            const challenges = data.challenges;

            for (const [name, challenge] of Object.entries(challenges)) {
                const card = document.createElement('div');
                card.className = 'challenge-card';
                card.innerHTML = `
                    <h2>${name}</h2>
                    <p>${challenge.description}</p>
                    <button onclick="startChallenge('${name}')">Start</button>
                `;
                container.appendChild(card);
            }
        })
        .catch(error => console.error('Error fetching challenges:', error));
});

function startChallenge(name) {
    fetch(`/start_challenge/${name}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Error starting challenge:', error));
}
