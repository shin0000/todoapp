import React, { useState } from 'react'

const Form = (props) => {
    const [todo, setTodo] = useState({ "id": 0, "title": "", "body": "" })
    return (
        <div>
            <p>Edited</p>
            <p>title: {todo.title}</p>
            <p>body: {todo.body}</p>
            <p>Form</p>
            <p>title: <input type='text' value={todo.title} onChange={(e) => setTodo({ ...todo, "title": e.target.value })} /></p>
            <p>body: <input type='text' value={todo.body} onChange={(e) => setTodo({ ...todo, "body": e.target.value })} /></p>
            <button onClick={() => { props.postTodo(todo); setTodo({ "id": 0, "title": "", "body": "" }); }}>addTodo</button>
        </div>
    )
}

export default Form
