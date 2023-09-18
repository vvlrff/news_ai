import { useLocation, useNavigate } from "react-router-dom";
import s from "./ResultPage.module.scss"


const ResultPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { state } = location;

  const submitData = (categoryData) => {
    navigate(`/result/${categoryData.category}`, { state: categoryData });
  };

  return (
    <div className={s.container}>
      ResultPage
      {state && state.response &&
        Object.entries(state.response).map(([key, value]) => (
          <button onClick={() => submitData({ category: key, data: value })} key={key}>
            Категория: {key}
          </button>
        ))
      }
    </div>
  )

}

export default ResultPage


