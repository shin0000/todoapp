import React, { useState, useEffect } from 'react'
import List from './List'
import Form from './Form'
import axios from 'axios'

const App1 = () => {
    const [todos, setTodos] = useState([{ "id": 1, "title": "aaa", "body": "aaa" }, { "id": 2, "title": "www", "body": "www" }]);

    const addTodo = (todo) => {
        todo["id"] = todos.length + 1
        setTodos([...todos, todo])
    }

    useEffect(() => {
        axios.get('/api1/todos/')
            .then(res => { setTodos(res.data) })
    }, [])

    const getTodo = () => {
        axios.get('/api1/todos/')
            .then(res => { setTodos(res.data) })
    }

    const postTodo = (todo) => {
        axios.post('/api1/todos/', todo)
            .then(res => console.log(res));
        axios.get('/api1/todos/')
            .then(res => { setTodos(res.data) });
    }

    return (
        <div>
            <List todos={todos} />
            <Form addTodo={addTodo} postTodo={postTodo} />
        </div>
    )
}

export default App1

