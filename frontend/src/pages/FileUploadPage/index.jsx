import React from 'react'
import s from "./FileUploadPage.module.scss"
import FileUploadForm from '../../components/FileUploadForm'

const FileUploadPage = () => {
  return (
    <div className={s.container}>
        <FileUploadForm />
    </div>
  )
}

export default FileUploadPage