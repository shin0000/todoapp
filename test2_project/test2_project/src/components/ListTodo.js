import React, { useState } from 'react'

const ListTodo = (props) => {
    const [eclicked, setEclicked] = useState(false);
    const [etodo, setEtodo] = useState({ "id": props.todo.id, "title": props.todo.title, "body": props.todo.body });

    if (eclicked) {
        return (
            <div>
                <li key={props.key}>
                    <p>=====</p>
                    <p>{props.todo.id}: <input type='text' value={etodo.title} onChange={(e) => setEtodo({ ...etodo, "title": e.target.value })} /></p>
                    <p><input type='text' value={etodo.body} onChange={(e) => setEtodo({ ...etodo, "body": e.target.value })} /></p>
                    <p>created_at: {props.todo.created_at}</p>
                    <p>updated_at: {props.todo.updated_at}</p>
                    <button onClick={() => { setEclicked(!eclicked) }}>Undo</button>
                    <button onClick={() => { props.putTodo(etodo); setEtodo(etodo); setEclicked(!eclicked); }}>Put</button>
                    <p>=====</p>
                </li>
            </div >
        )
    } else {
        return (
            <div>
                <li key={props.key}>
                    <p>=====</p>
                    <p>{props.todo.id}: {props.todo.title}</p>
                    <p>{props.todo.body}</p>
                    <p>created_at: {props.todo.created_at}</p>
                    <p>updated_at: {props.todo.updated_at}</p>
                    <button onClick={() => setEclicked(!eclicked)}>Edit</button>
                    <button onClick={() => { props.deleteTodo(props.todo.id) }}>Delete</button>
                    <p>=====</p>
                </li>
            </div>
        )
    }
}

export default ListTodo
