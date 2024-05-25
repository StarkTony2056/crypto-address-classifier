document
    .getElementById("addressForm")
    .addEventListener("submit", async function (event) {
        event.preventDefault();

        const addressInput = document.getElementById("address").value;
        const resultDiv = document.getElementById("result");
        resultDiv.textContent = "Classifying...";

        try {
            const response = await fetch("http://127.0.0.1:5000/classify", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ address: addressInput }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            resultDiv.textContent = `Cryptocurrency Type: ${data.cryptocurrency}`;
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
        }
    });
