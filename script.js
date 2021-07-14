async function fetchMusic() {
    const musicArea = document.getElementById('music');
    let response = await fetch("musicdata.json");
    let data = await response.json();
    data = JSON.stringify(data);
    data = JSON.parse(data);
    const myMusic = [];
    for (element in data) {
        data[element] = data[element].split('"')
        myMusic.push(data[element][1])
        musicArea.insertAdjacentHTML("afterbegin", `
        <div class="song"> 
        <audio controls src="${data[element][1]}">
        Your browser does not support the
        <code>audio</code> element.
        </audio>
        </div>
        `);
    }
}
fetchMusic();

