document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById("mgnregaChart").getContext("2d");
    let chart;

    function renderChart(data) {
        const labels = data.map(item => item.Month || "Unknown");
        const values = data.map(item => item["Persondays Generated (in lakhs)"] || 0);

        if (chart) chart.destroy();

        chart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Persondays Generated (in lakhs)",
                    data: values,
                    backgroundColor: "#66bb6a"
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: "top" },
                    title: { display: true, text: "District Performance in MGNREGA" }
                }
            }
        });
    }

    // Initial data load
    renderChart(window.initialData || []);

    // Filter button
    document.getElementById("filterBtn").addEventListener("click", () => {
        const district = document.getElementById("district").value;
        if (!district) return alert("Please select a district.");

        fetch("/filter", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `district=${district}`
        })
        .then(res => res.json())
        .then(data => renderChart(data))
        .catch(err => console.error(err));
    });
});
