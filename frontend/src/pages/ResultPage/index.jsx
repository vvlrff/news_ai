import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import s from "./ResultPage.module.scss"


const ResultPage = () => {
  const [serverResponse, setServerResponse] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();
  const { state } = location;

  console.log("location", location)

  

  const submitData = () => {
    
  }

  return (
    <div className={s.container}>
      ResultPage
      {
        Object.entries(state.response[0])
          .map(([key, value]) => (
            <>
              <button onClick={submitData} key={key} >
                Категория: {key}
              </button>
              {/* {Object.entries(value).map(([keyValue, valueValue]) => (
                  <div key={keyValue}>
                    <div className='card-spec'>
                      {keyValue}: {valueValue}
                    </div >
                  </div>
                ))} */}
            </>
          ))
      }
    </div>
  )
}

export default ResultPage

