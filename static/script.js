document
    .getElementById("interviewForm")
    .addEventListener("submit", async function (e) {

        e.preventDefault();

        const result = document.getElementById("result");

        result.innerHTML = "<h3>Generating questions...</h3>";

        const data = {
            role: document.getElementById("role").value,
            company: document.getElementById("company").value,
            experience: document.getElementById("experience").value,
            difficulty: document.getElementById("difficulty").value,
            question_count: Number(document.getElementById("question_count").value),
            question_type: document.getElementById("question_type").value
        };

        try {

            const response = await fetch("/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const resultData = await response.json();

            result.innerHTML = "";

            if (!resultData.success) {
                result.innerHTML = "<h3>Something went wrong.</h3>";
                return;
            }

            resultData.questions.forEach(question => {

                result.innerHTML += `
                    <div class="question">
                        ${question}
                    </div>
                `;

            });

        }

        catch (error) {

            result.innerHTML =
                "<h3>Unable to connect to server.</h3>";

        }

    });