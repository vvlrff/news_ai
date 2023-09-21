import React from "react";
import { Link } from "react-router-dom";
import s from "./Navbar.module.scss";

const Navbar = () => {
    return (
        <>
            <nav className={s.nav}>
                <div className={s.container}>
                    <div className={s.left}>
                        <p className={s.text}>NaturaLP</p>
                        <img
                            src="https://thumb.tildacdn.com/tild3237-3232-4266-a362-333130353936/-/resize/104x/-/format/webp/_____2__1.png"
                            alt=""
                        />
                    </div>
                    <div className={s.linkContainer}>
                        <Link to="/">На главную</Link>
                        <Link to="/upload">Загрузить файл</Link>
                    </div>
                </div>
            </nav>
        </>
    );
};

export default Navbar;
