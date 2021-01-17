import React, { useState } from 'react'
import ListTodo from './ListTodo'

const List = (props) => {

    return (
        <div>
            <p>List</p>
            <ul>
                {props.todos.map(todo => (
                    // <li key={todo.id}>
                    //     <p>=====</p>
                    //     <p>{todo.id}: {todo.title}</p>
                    //     <p>{todo.body}</p>
                    //     <p>created_at: {todo.created_at}</p>
                    //     <p>updated_at: {todo.updated_at}</p>
                    //     <button onClick={() => setEid(todo.id)}>Edit</button>
                    //     <button onClick={() => { props.deleteTodo(todo.id) }}>Delete</button>
                    //     <ListTodo eid={eid} todo={todo} />
                    //     <p>=====</p>
                    // </li>
                    <ListTodo key={todo.id} deleteTodo={props.deleteTodo} putTodo={props.putTodo} todo={todo} />
                ))}
            </ul>
        </div>
    )
}

export default List
