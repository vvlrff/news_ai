import React from "react";
import { useLocation } from "react-router-dom";
import s from "./TestCategoryPage.module.scss";
import { motion } from "framer-motion";

const TestCategoryPage = () => {
    const location = useLocation();
    const { state } = location;
    
    const list = state.data["Сообщения без дубликатов"];

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
                {state.data["Общее количество"] > 0 ? (
                    list.map((item, index) => {
                        return (
                            <div className={s.card} key={index}>
                                {item}
                            </div>
                        );
                    })
                ) : (
                    <div className={s.card}>Ничего не найдено</div>
                )}
            </div>
        </motion.section>
    );
};

export default TestCategoryPage;
