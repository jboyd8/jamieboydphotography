// select the div with typewriter app id
let app = document.getElementById('typewriter-app');

// Create a new instance of the Typewirter app and keep it looping
let typewriter = new Typewriter(app, {
    loop:true
});

// Add contect to the typewriter and attributes
typewriter.typeString('Jamie Boyd Photography')
    .pauseFor(3000)
    .deleteAll()
    .start()
