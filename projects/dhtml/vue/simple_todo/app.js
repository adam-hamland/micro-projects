// This simple todo list using vue.js is largely derived from coding garden on YouTube 
// https://www.youtube.com/watch?v=-X2hP9pOVss


const app = new Vue({
    el: '#app',
    data: {
        title: "Hello friends",
        newTodo: "",
        todos: []
    },
    methods: {
        // Add todo list item function
        addTodo() {
            this.todos.push({
                title: this.newTodo,
                done: false
            });
            this.newTodo = ""
        },
        //Remove a single todo list item
        rm(todoToRm) {
            let indexOf = this.todos.indexOf(todoToRm);
            this.todos.splice(indexOf, 1);
        },
        //Mark all todo list items as done
        allDone() {
            this.todos.forEach(todo => {
                todo.done = true;
            });
        },
        //Remove all todo list items
        rmAll() {
            this.todos = []
        }
    }
});