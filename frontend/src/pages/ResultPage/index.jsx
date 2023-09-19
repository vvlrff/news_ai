import { useLocation, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import s from "./ResultPage.module.scss";

const ResultPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { state } = location;

    const submitData = (categoryData) => {
        navigate(`/result/${categoryData.category}`, { state: categoryData });
    };

    const container = {
        hidden: { opacity: 1, scale: 0 },
        visible: {
            opacity: 1,
            scale: 1,
            transition: {
                delayChildren: 0.3,
                staggerChildren: 0.2,
            },
        },
    };

    const item = {
        hidden: { y: 20, opacity: 0 },
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
                    variants={container}
                    initial="hidden"
                    animate="visible"
                >
                    {Object.entries(state.response).map(([key, value]) => (
                        <>
                            <motion.li
                                variants={item}
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
