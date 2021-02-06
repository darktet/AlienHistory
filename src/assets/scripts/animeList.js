let username = "Dark_Vash";
// let username = "Bk-201kun";
let page = 0;
var request = new XMLHttpRequest();
let animeId = {};
let urlCORS = "https://cors-anywhere.herokuapp.com/";
let url = "https://myanimelist.net/ajaxtb.php?keepThis=true&detailedaid=35203";


let parseData = () => {
  request.open(
    "GET",
    `https://api.jikan.moe/v3/user/${username}/animelist/all/${page}`
  );

  request.onload = () => {
    if (request.status == 200) {
      let animeData = JSON.parse(request.response).anime;
      console.log(animeData);
      for (i = 0; i < animeData.length; i++) {
        // console.log(animeData[i].mal_id) end_date start_date total_episodes url image_url /6 watched_episodes
        let srealNumber = i;
        itemes = document.getElementById('itemes');
        let animeDIV = document.createElement('div');
        animeDIV.className = 'animeList';
        animeDIV.innerHTML = `<div class="innerDivNO text">${srealNumber+1}</div>
                            <img class=animeDP src=${animeData[i].image_url}>
                            <a class="animeName text" href=${animeData[i].url} target="_blank">${animeData[i].title}</a>
                            <div class="watchedEP text">${animeData[i].watched_episodes}</div>`;

        // let innerDivNO = document.createElement('div');
        // innerDivNO.className = 'innerDivNO';
        // innerDivNO.textContent = srealNumber+1;

        // let animeDP = document.createElement('img');
        // animeDP.className = 'animeImage';
        // animeDP.src = animeData[i].image_url;

        // let animeName = document.createElement('a');
        // animeData.className = "animeName";
        // animeName.innerText = "src=" + animeData[i].url + ">" + animeData[i].title;

        // let srealNumber = i;
        // let innerDivNO = document.createElement('div');
        // innerDivNO.className = 'innerDivNO';
        // innerDivNO.textContent = srealNumber+1;

        // let srealNumber = i;
        // let innerDivNO = document.createElement('div');
        // innerDivNO.className = 'innerDivNO';
        // innerDivNO.textContent = srealNumber+1;


        itemes.append(animeDIV);
      }
      // console.log(animeData[i].titel);
    } else {
      console.error("error");
    }
  };
  request.send();
}
parseData();
