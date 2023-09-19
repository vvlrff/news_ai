import React from "react";
import { useLocation } from "react-router-dom";
import s from "./CategoryPage.module.scss";
import { motion } from "framer-motion";

const CategoryPage = () => {
    const location = useLocation();
    const { state } = location;

    console.log(state);

    return (
        <motion.section
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{
                type: "spring",
                stiffness: 260,
                damping: 50,
            }}
        >
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
        </motion.section>
    );
};

export default CategoryPage;
