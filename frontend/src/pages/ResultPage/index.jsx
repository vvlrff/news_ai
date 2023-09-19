import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import s from "./ResultPage.module.scss";

const ResultPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { state } = location;
    const [selectedId, setSelectedId] = useState(null);

    const submitData = (categoryData) => {
        navigate(`/result/${categoryData.category}`, { state: categoryData });
    };

    const ulAnim = {
        hidden: { opacity: 1, scale: 0 },
        visible: {
            opacity: 1,
            scale: 1,
            transition: {
                delayChildren: 0.1,
                staggerChildren: 0.2,
            },
        },
    };

    const liAnim = {
        hidden: { y: 70, opacity: 0 },
        visible: {
            y: 0,
            opacity: 1,
        },
    };

    return (
        <motion.section
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
        >
            <div className={s.container}>
                <h2 className={s.header}>Выберите Категорию</h2>

                <motion.ul
                    className={s.list}
                    variants={ulAnim}
                    initial="hidden"
                    animate="visible"
                >
                    {Object.entries(state.response).map(([key, value]) => (
                        <>
                            <motion.li
                                layoutId={key}
                                variants={liAnim}
                                className={s.card}
                                onClick={() =>
                                    submitData({
                                        category: key,
                                        data: value,
                                    })
                                }
                                key={key}
                            >
                                <p>{key}</p>
                                {/* <img className={s.img} src="" alt="bgimg" /> */}
                            </motion.li>
                        </>
                    ))}
                </motion.ul>
            </div>
        </motion.section>
    );
};

export default ResultPage;
