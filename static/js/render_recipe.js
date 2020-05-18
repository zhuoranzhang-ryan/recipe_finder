function toggle() {
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var popup = document.getElementById('popup');
    popup.classList.toggle('active');
    console.log("toggling");
}

function show_recipe(recipe_id) {
    
    console.log(recipe_id);

    d3.json("data.json").then(data => {
        
    })

}