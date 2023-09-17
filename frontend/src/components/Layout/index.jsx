import { Outlet } from 'react-router-dom'
import Navbar from '../Navbar'
import s from "./Layout.module.scss"


const Layout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  )
}

export default Layout