import React, { useState, useEffect } from 'react'
import List from './List'
import Form from './Form'
import Header from './Header'
import axios from 'axios'

const App1 = () => {
    const [todos, setTodos] = useState([]);
    // const [todos, setTodos] = useState([{ "id": 1, "title": "aaa", "body": "aaa" }, { "id": 2, "title": "www", "body": "www" }]);

    const addTodo = (todo) => {
        todo["id"] = todos.length + 1
        setTodos([...todos, todo])
    }

    useEffect(() => {
        axios.get('/api1/todos/')
            .then(res => { setTodos(res.data) });
    }, [])

    const getTodo = () => {
        axios.get('/api1/todos/')
            .then(res => { setTodos(res.data) });
    }

    const postTodo = (todo) => {
        axios.post('/api1/todos/', todo)
            .then(res => setTodos([...todos, res.data]));
    }

    const deleteTodo = (id) => {
        axios.delete(`/api1/todos/${id}/`)
            .then(res => setTodos(todos.filter(todo => todo.id !== id)));
    }

    const putTodo = (etodo) => {
        const id = etodo.id;
        axios.put(`/api1/todos/${id}/`, etodo)
            .then(res => setTodos(todos.map(todo => todo.id === id ? res.data : todo)));
    }

    return (
        <div>
            <Header getTodo={getTodo} />
            <List todos={todos} deleteTodo={deleteTodo} putTodo={putTodo} />
            <Form addTodo={addTodo} postTodo={postTodo} />
        </div>
    )
}

export default App1

