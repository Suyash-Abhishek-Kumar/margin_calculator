async function margin() {
    let conducted = document.getElementById("conducted").value;
    let absent = document.getElementById("absent").value;

    if (conducted === "" || absent === "") {
        document.getElementById("result").innerText = "Please enter both values.";
        return;
    }

    let response = await fetch("https://margin-calculator-2.onrender.com", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ conducted, absent })
    });

    let data = await response.json();
    document.getElementById("result").innerText = data.result;
}