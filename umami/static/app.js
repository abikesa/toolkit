let data = {};
let saveTimeout;

async function fetchData() {
    const res = await fetch("/api/layers");
    data = await res.json();
    document.getElementById("title").textContent = data.title || "Untitled";
    const layersDiv = document.getElementById("layers");
    layersDiv.innerHTML = "";

    data.layers.forEach((layer, idx) => {
        const div = document.createElement("div");
        div.className = "layer";

        div.innerHTML = `
            <h2><span class="symbol">${layer.symbol}</span>
            <input class="editable" value="${layer.name}" 
                   onchange="updateField(${idx}, 'name', this.value)" /></h2>
            <p>Theme: <input class="editable" value="${layer.theme}" 
                   onchange="updateField(${idx}, 'theme', this.value)" /></p>
            <p class="sn">Signal/Noise Ratio:
                <input type="number" value="${layer.signal}" 
                       onchange="updateField(${idx}, 'signal', this.value)" />
                /
                <input type="number" value="${layer.noise}" 
                       onchange="updateField(${idx}, 'noise', this.value)" />
            </p>
            <p><textarea class="editable" rows="2" cols="50"
                   onchange="updateField(${idx}, 'description', this.value)">${layer.description}</textarea></p>
        `;
        layersDiv.appendChild(div);
    });
}

function updateField(index, key, value) {
    if (key === "signal" || key === "noise") {
        value = parseInt(value);
        if (isNaN(value)) value = 0;
    }
    data.layers[index][key] = value;
    triggerAutosave();
}

function triggerAutosave() {
    if (saveTimeout) clearTimeout(saveTimeout);
    saveTimeout = setTimeout(saveData, 1000);  // 1 second debounce
}

async function saveData() {
    console.log("Autosaving...");
    const res = await fetch("/api/layers", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    if (!res.ok) {
        console.error("Auto-save failed");
    }
}

fetchData();
