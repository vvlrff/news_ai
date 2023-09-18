import { register } from "swiper/element/bundle";
import { useNavigate } from "react-router-dom";
import video from '../../assets/video/vid.mp4'
import s from "./HomePage.module.scss";

const HomePage = () => {
    register();
    const navigate = useNavigate();

    const onRedirect = () => {
      navigate('/upload')
    }

    return (
        <section className={s.homepage}>
            <div className={s.video}>
                <video autoPlay muted loop>
                    <source src={video} />
                </video>
            </div>
            <div className={s.content}>
                <swiper-container
                    autoplay
                    className={s.swiper}
                    pagination="true"
                    style={{
                        height: "100%",
                        "--swiper-pagination-color": "#7DFFF9",
                        "--swiper-pagination-bullet-inactive-color": "#999999",
                        "--swiper-pagination-bullet-inactive-opacity": "1",
                        "--swiper-pagination-bullet-size": "12px",
                        "--swiper-pagination-bullet-horizontal-gap": "10%",
                    }}
                >
                    <swiper-slide>
                        <h1 className={s.header}>
                            Excel в Новостной Сборник: Ваши Данные, Ваши
                            Новости!
                        </h1>
                        <p className={s.text}>
                            Добро пожаловать в наш уникальный веб-сервис,
                            который превращает ваши Excel-файлы в организованный
                            и информативный сборник новостей. Независимо от
                            того, в какой сфере вы работаете, наш сервис поможет
                            вам быстро и легко анализировать и систематизировать
                            ваши данные.
                        </p>
                    </swiper-slide>
                    <swiper-slide>
                        <h2 className={s.caption}>Как это работает:</h2>
                        <div className={s.text}>
                            <ul className={s.textList}>
                                <li>
                                    Загрузите ваш Excel-файл: Просто загрузите
                                    файл с данными в наш сервис.
                                </li>
                                <li>
                                    Автоматическая обработка: Наш мощный
                                    алгоритм автоматически анализирует данные и
                                    выделяет ключевую информацию.
                                </li>
                                <li>
                                    Сортировка по категориям: Мы организуем
                                    данные по категориям, создавая понятный
                                    сборник новостей.
                                </li>
                                <li>
                                    Готово к использованию: Ваш сборник новостей
                                    теперь готов к просмотру и анализу. Вы
                                    можете просматривать новости в удобном
                                    формате, быстро находя интересующую вас
                                    информацию.
                                </li>
                            </ul>
                        </div>
                    </swiper-slide>
                    <swiper-slide>
                        <h2 className={s.caption}>
                            Почему выбирают наш сервис:
                        </h2>
                        <div className={s.text}>
                            <ul className={s.textList}>
                                <li>
                                    Быстро и удобно: Забудьте о долгих и сложных
                                    процессах анализа данных. Наш сервис делает
                                    всю работу за вас.
                                </li>
                                <li>
                                    Точность и надежность: Наши алгоритмы
                                    гарантируют точное разделение данных по
                                    категориям.
                                </li>
                                <li>
                                    Многофункциональность: Независимо от вашей
                                    области деятельности, наш сервис подходит
                                    для анализа данных в различных контекстах.
                                </li>
                                <li>
                                    Экономия времени и ресурсов: Наш сервис
                                    позволяет вам быстро получить ценные выводы
                                    из ваших данных, экономя ваши ресурсы.
                                </li>
                            </ul>
                        </div>
                    </swiper-slide>
                </swiper-container>
                <button onClick={onRedirect} className={s.btn}>Начать</button>
            </div>
        </section>
    );
};

export default HomePage;
