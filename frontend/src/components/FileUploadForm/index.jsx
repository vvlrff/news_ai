import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api";
import s from "./FileUploadForm.module.scss";

const FileUploadForm = () => {
    const [file, setFile] = useState(null);
    const [fileName, setFileName] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [serverResponse, setServerResponse] = useState(null); // Состояние для хранения ответа сервера

    const navigate = useNavigate();

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        setFile(selectedFile);
        setFileName(selectedFile.name);
    };

    useEffect(() => {
        if (serverResponse) {
            navigate("/result", { state: { response: serverResponse } });
        }
    }, [serverResponse, navigate]);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append("file", file);

        try {
            setIsLoading(true);

            await api
                .post("/api/zagruzka", formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                })
                .then((response) => {
                    console.log(response.data);
                    setServerResponse(response.data); // Сохраняем ответ сервера в состояние
                })
                .catch((error) => {
                    console.log(error);
                });
            console.log("Файл успешно загружен");
        } catch (error) {
            console.error("Ошибка при загрузке файла:", error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className={s.form}>
            <input
                type="file"
                onChange={handleFileChange}
                className={s.input}
            />
            {fileName === "" ? (
                <p className={s.p}>
                    Перетащите свои файлы сюда или щелкните в этой области
                </p>
            ) : (
                <p className={s.p}>
                    Выбранный файл: {fileName}
                </p>
            )}

            {isLoading ? (
                <p className={s.p}>Идет обработка данных...</p>
            ) : (
                <>
                    <button
                        disabled={!file ? "disabled" : null}
                        type="submit"
                        className={s.button}
                    >
                        Загрузить файл
                    </button>
                </>
            )}
        </form>
    );
};

export default FileUploadForm;
