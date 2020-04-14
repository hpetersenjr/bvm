var root = document.body

/*
m.render(root, [
    m("main", [
        m("h1", {class: "title"}, "My first app"),
        m("button", "A button"),
        m("div" , {id: "aws2"}, [
	        m("p","Click the AWS icon"),
	        m("div" , {id: "aws"},m("i" , {class:"fab fa-aws"})),
	    ])
    ])
])
*/

var count = 0 // added a variable

var Hello = {
    view: function() {
        return m("main", [
            m("h1", {class: "title"}, "Test app"),
            // changed the next line
            m("button", {onclick: increment}, count + " clicks"),
        ])
    }
}

var increment = function() {
    m.request({
        method: "PUT",
        url: "//rem-rest-api.herokuapp.com/api/tutorial/1",
        body: {count: count + 1},
        withCredentials: true,
    })
    .then(function(data) {
        count = parseInt(data.count)
    })
}

m.mount(root, Hello)

var Splash = {
    view: function() {
        return m("a", {href: "#!/hello"}, "Enter!")
    }
}

m.route(root, "/splash", {
    "/splash": Splash,
    "/hello": Hello,
})