import { useLocation, useNavigate } from "react-router-dom";
import s from "./ResultPage.module.scss";

const ResultPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { state } = location;

    const submitData = (categoryData) => {
        navigate(`/result/${categoryData.category}`, { state: categoryData });
    };

    return (
        <section>
            <div className={s.container}>
                <h2 className={s.header}>Выберите Категорию</h2>
                <ul className={s.list}>
                    {Object.entries(state.response[0]).map(([key, value]) => (
                        <>
                            <li
                                className={s.card}
                                onClick={() =>
                                    submitData({ category: key, data: value })
                                }
                                key={key}
                            >
                                <p>{key}</p>
                                {/* <img className={s.img} src="" alt="bgimg" /> */}
                            </li>
                        </>
                    ))}
                </ul>
            </div>
        </section>
    );
};

export default ResultPage;
