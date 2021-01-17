import React from 'react'

const Header = (props) => {
    return (
        <div>
            <button onClick={() => props.getTodo()}>Update</button>
        </div>
    )
}

export default Header
