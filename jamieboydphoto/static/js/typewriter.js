let app = document.getElementById('typewriter-app');

let typewriter = new Typewriter(app, {
    loop:true
});

typewriter.typeString('Jamie Boyd Photography')
    .pauseFor(3000)
    .deleteAll()
    .start()
