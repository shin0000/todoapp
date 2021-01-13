import React from 'react'

const List = (props) => {
    return (
        <div>
            <p>List</p>
            <ul>
                {props.todos.map(todo => (
                    <li key={todo.id}>
                        <p>=====</p>
                        <p>{todo.id}: {todo.title}</p>
                        <p>{todo.body}</p>
                        <p>created_at: {todo.created_at}</p>
                        <p>updated_at: {todo.updated_at}</p>
                        <p>=====</p>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default List
