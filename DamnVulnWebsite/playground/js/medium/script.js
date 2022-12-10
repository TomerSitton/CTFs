function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) 
    	t += e[n];
    console.log(t)
}
setTimeout(function() { do_elsesomething("XX") }, 300);

function do_elsesomething(e) {
    do_something(e + process.argv[2] + "XX")
}