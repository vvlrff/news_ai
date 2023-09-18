import { useLocation } from "react-router-dom";
import s from "./ResultPage.module.scss"


const ResultPage = () => {
  const location = useLocation();
  const objectIndex = 0;
  const { state } = location;

  console.log("state.response[objectIndex]", state.response[objectIndex]);
  console.log("state.response", state.response);

  return (
    <div className={s.container}>
      ResultPage
      {
        Object.entries(state.response[objectIndex])
          .map(([key, value]) => (
            <div key={key}>
              <div className='card-spec'>
                {key}: {Object.entries(value).map(([keyValue, valueValue]) => (
                  <div key={keyValue}>
                    <div className='card-spec'>
                      {keyValue}: {valueValue}
                    </div >
                  </div>))}
              </div >
            </div>
          ))
      }
      {/* {state.response.map((question, index) => (
        <div className={s.container} key={index}>
          <h3
            className={s.title}
          >Вопрос: {question.question}</h3>
          <ul className={s.resultList}>
            {question.answer.map((answer, answerIndex) => (
              <li className={s.resultItem} key={answerIndex}>
                <h4 className={s.itemTheme}>
                  Тема: {answer.cluster}
                </h4>
                <p className={s.count}>
                  Количество ответов: {answer.count}
                </p>
                <ul className={s.answerList}>
                  Ответы:
                  {answer.cluster_answers.map(
                    (clusterAnswer, clusterAnswerIndex) => (
                      <li
                        className={s.answers}
                        key={clusterAnswerIndex}
                      >
                        {clusterAnswer}
                      </li>
                    )
                  )}
                </ul>
              </li>
            ))}
          </ul>
          <button
            className={s.buttonDownload}
            onClick={() => getExcel(question.question_id)}>
            Скачать файл ResultPage {question.question_id}{" "}
          </button>
        </div>
      ))} */}
    </div>
  )
}

export default ResultPage

