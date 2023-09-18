import React from "react";
import { Link } from "react-router-dom";
import s from "./Navbar.module.scss";

const Navbar = () => {
    return (
        <>
            <nav className={s.nav}>
                <div className={s.container}>
                    <div className={s.left}></div>
                    <div className={s.linkContainer}>
                        <Link to="/">HomePage</Link>
                        <Link to="/data">DataPage</Link>
                    </div>
                </div>
            </nav>
        </>
    );
};

export default Navbar;
