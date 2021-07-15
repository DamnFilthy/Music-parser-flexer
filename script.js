async function fetchMusic() {
    const musicArea = document.getElementById('music');
    let response = await fetch("musicdata.json");
    let data = await response.json();
    data = JSON.stringify(data);
    data = JSON.parse(data);
    const myMusic = [];
    for (idx in data) {
        console.log(data[idx].name)
        musicArea.insertAdjacentHTML("afterbegin", `
        <div classs="col" id="song"> 
            <div>
                <img src="${data[idx].img_link}" alt="song img" />
            </div>
            <div>
                <div class="artist"> ${data[idx].name} - ${data[idx].song_name} </div>
                    <audio controls src="${data[idx].mp3_link}">
                    Your browser does not support the
                    <code>audio</code> element.
                    </audio>
                </div>
        </div>
        `);
    }
}
fetchMusic();

