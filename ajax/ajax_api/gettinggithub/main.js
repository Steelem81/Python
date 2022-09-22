
async function getGithubUser() {
    let user = document.querySelector('#github-user').value
    console.log(user)
    var response = await fetch(`https://api.github.com/users/${user}`)
    var coderData = await response.json()
    console.log(coderData)

    let name = coderData.login
    let avatarUrl = coderData.avatar_url
    
    document.querySelector('#user_data').innerHTML += 
    `<div id='user_data'><h2>${name}</h2><img src='${avatarUrl}'></img></div>`
}
document.querySelector('#get_user').addEventListener('click', getGithubUser)