import React from "react";
import { useLocation } from "react-router-dom";
import s from "./CategoryPage.module.scss";

const CategoryPage = () => {
    const location = useLocation();
    const { state } = location;

    console.log(state);

    return (
        <section>
            <div className={s.container}>
                <p className={s.title}>{state.category}</p>
                {Object.entries(state.data).map(([key, value]) => (
                    <div key={key} className={s.card}>
                        <div className={s.cardInfo}>
                            {key}: {value}
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
};

export default CategoryPage;
