import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import s from "./ResultPage.module.scss";
import api from "../../api";
import PieGraph from "../../components/PieGraph";

const ResultPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { state } = location;
    const [loading, setLoading] = useState(false);

    console.log(state.response);

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
        hidden: { y: 75, opacity: 0 },
        visible: {
            y: 0,
            opacity: 1,
        },
    };
    const getExcel_sema = () => {
        setLoading(true);
        api
            .post(`/api/vigruzka`, null, {
                responseType: "blob", // Указываем, что ожидаем blob (бинарные данные) в ответе
            })
            .then((res) => {
                if (res.status === 200) {
                    // Создаем ссылку на blob и имитируем клик на ней для скачивания файла
                    const url = window.URL.createObjectURL(
                        new Blob([res.data])
                    );
                    const link = document.createElement("a");
                    link.href = url;
                    link.setAttribute("download", "answer" + ".xlsx"); // Установите желаемое имя файла
                    document.body.appendChild(link);
                    link.click();
                    link.remove();
                    window.URL.revokeObjectURL(url); // Очистите ресурсы
                    setLoading(false);
                }
            })
            .catch((err) => {
                alert(err);
                setLoading(false);
            });
    };
    const getExcel_for_chek = () => {
        setLoading(true);
        api
            .post(`/api/vigruzka_for_chek`, null, {
                responseType: "blob", // Указываем, что ожидаем blob (бинарные данные) в ответе
            })
            .then((res) => {
                if (res.status === 200) {
                    // Создаем ссылку на blob и имитируем клик на ней для скачивания файла
                    const url = window.URL.createObjectURL(
                        new Blob([res.data])
                    );
                    const link = document.createElement("a");
                    link.href = url;
                    link.setAttribute(
                        "download",
                        "NaturaLP_ANSWER_FOR_CHECKING" + ".xlsx"
                    ); // Установите желаемое имя файла
                    document.body.appendChild(link);
                    link.click();
                    link.remove();
                    window.URL.revokeObjectURL(url); // Очистите ресурсы
                    setLoading(false);
                }
            })
            .catch((err) => {
                alert(err);
                setLoading(false);
            });
    };

    return (
        <motion.section
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
        >
            <div className={s.container}>
                <div className={s.upperContainer}>
                    <h2 className={s.header}>Выберите Категорию</h2>
                    <div className={s.buttonContainer}>
                        <button
                            className={s.downloadBtn}
                            onClick={() => getExcel_sema()}
                        >
                            Скачать xslx для анализа
                        </button>
                        <button
                            className={s.downloadBtn}
                            onClick={() => getExcel_for_chek()}
                        >
                            Скачать xslx для проверки
                        </button>
                    </div>
                </div>

                <PieGraph data={state.response}></PieGraph>

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
                            </motion.li>
                        </>
                    ))}
                </motion.ul>
            </div>
        </motion.section>
    );
};

export default ResultPage;
