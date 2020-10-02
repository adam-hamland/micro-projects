<template>
  <div class="hello container-fluid">
    <h1>{{ msg }}</h1>
        <form @submit.prevent="addTodo">
            <label for="newTodo">New Item</label>
            <input v-model="newTodo" type="text" name="newTodo" id="newTodo" value="">
            <button type="submit" name="button" class="btn btn-primary">Add</button>
        </form>
        <button @click="allDone" type="button" name="button" class="btn btn-secondary">Mark all as done</button>
        <ul>
            <li v-for="todo in todos" :key="todo">
                <input type="checkbox" v-model="todo.done" class="todoEl">
                <p :class="{done: todo.done}" class="todoEl">{{todo.title}}</p> 
                <button @click="rm(todo)" class="btn btn-secondary todoDelete">Delete</button>
            </li>
        </ul>
       
        <button @click="rmAll" type="button" name="button" class="btn btn-danger">Delete all</button>
  </div>
    
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      title: "Hello friends",
      newTodo: "",
      todos: []
    }
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
    },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
}
li {
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 50vw;
  max-width: 700px;
  position: relative;
  height: 50px;
}
form {
  margin: 1rem;
}

form input, label, button {
  vertical-align:middle;
  margin: .5rem;
}

li input, p, button {
  vertical-align:middle;
  margin: .5rem;
  
}

.todoEl {
  display: inline-grid;
  margin-right: 1rem;
}

.todoDelete {
  position: absolute;
  right: 0;
}

.done {
  text-decoration: line-through;
}

.container-fluid {
  display: grid;
  place-items: center
}
</style>
