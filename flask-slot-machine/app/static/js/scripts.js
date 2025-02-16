document.addEventListener("DOMContentLoaded", function () {
  const spinButton = document.getElementById("spin-button");
  const resultDisplay = document.getElementById("result-display");
  const betInput = document.getElementById("bet-input");
  const linesInput = document.getElementById("lines-input");
  const slotsContainer = document.getElementById("slots-container");

  spinButton.addEventListener("click", function () {
    const bet = parseFloat(betInput.value);
    const lines = parseInt(linesInput.value);

    if (isNaN(bet) || isNaN(lines) || bet <= 0 || lines <= 0) {
      alert("Please enter valid bet and lines.");
      return;
    }

    fetch("/spin", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ bet: bet, lines: lines }),
    })
      .then((response) => response.json())
      .then((data) => {
        updateSlots(data.slots);
        resultDisplay.innerText = `You won $${data.winnings}.`;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  function updateSlots(slots) {
    slotsContainer.innerHTML = "";
    slots.forEach((row) => {
      const rowDiv = document.createElement("div");
      rowDiv.className = "slot-row";
      row.forEach((symbol) => {
        const symbolDiv = document.createElement("div");
        symbolDiv.className = "slot-symbol";
        symbolDiv.innerText = symbol;
        rowDiv.appendChild(symbolDiv);
      });
      slotsContainer.appendChild(rowDiv);
    });
  }
});
