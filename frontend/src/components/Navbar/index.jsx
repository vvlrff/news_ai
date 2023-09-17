import React from 'react'
import { Link } from 'react-router-dom'
import s from "./Navbar.module.scss"

const Navbar = () => {
    return (
        <>
            <Link to='/'>
                HomePage
            </Link>
            <Link to='/data'>
                DataPage
            </Link>
        </>
    )
}

export default Navbar