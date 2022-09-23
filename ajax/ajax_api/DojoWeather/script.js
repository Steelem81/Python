var cities = document.querySelectorAll(".cities > li");
// var temps = document.querySelectorAll(".high, .low");

// console.log(temps)


var apiKey = 'afe55612e6ed86960c1b316188f243b3'

async function getWeather(city){
    console.log(`api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`)
    var request = await fetch(`api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`)
    var response = await request.json()

    // let condition = response.list[0].weather[0].main
    // let description = response.list[0].weather[0].description
    // let high = response.list[0].temp.max
    // let low = response.list[0].temp.min
    // console.log(high, low, condition, description)
}


cities.forEach( item => {item.addEventListener("click", function(){
    // alert("Loading weather report for " + item.textContent);
    var city = item.textContent
    getWeather(city)
})})

function fToC(temp){
    if (!Number.isInteger(temp)){
        temp = parseInt(temp)
    } 
    newTemp = Math.round((temp-32)*(5/9))
    return newTemp
}

function cToF(temp){
    if(!Number.isInteger(temp)){
        temp = parseInt(temp)
    }
    newTemp = Math.round((temp *(9/5)) + 32)
    return newTemp
}

document.querySelector("#temp-choice").addEventListener("change", function(e){
    if (this.value == "F"){
        document.querySelectorAll(".high, .low").forEach( item => 
            item.childNodes[0].textContent = cToF(item.childNodes[0].textContent)
            )
        } else if (this.value == "C") {
            document.querySelectorAll(".high, .low").forEach( item => 
                item.childNodes[0].textContent = fToC(item.childNodes[0].textContent)
            )
        }
    }
)

document.querySelector(".accept").addEventListener("click", function() {
    this.parentNode.remove()
})