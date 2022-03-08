// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

// function wipeOut(){
//     // $("#message").fadeOut("slow")
//     alert("howdy!")
// }
// setTimeout(wipeOut,3000)

//Automatically fade out messages
// setTimeout(function() {
//     $("#message").fadeOut('slow')
// }, 3000);

function myRemoval() {
    document.getElementById("message").remove();
}

setTimeout(myRemoval, 3000);
//Automatically fade out messages
// setTimeout(function() {
//     $(document.getElementById("message")).fadeOut('slow')
// }, 3000);

// setTimeout(() => {
//     $('#message').fadeOut('slow')
// }, 3000)
