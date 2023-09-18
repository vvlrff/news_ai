import { Route, createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';
import Layout from "./components/Layout";
import HomePage from './pages/HomePage';
import NotFoundPage from './pages/NotFoundPage';
import ResultPage from './pages/ResultPage';
import FileUploadPage from './pages/FileUploadPage';
import CategoryPage from './pages/CategoryPage';

const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />} >
    <Route index element={<HomePage />} />
    <Route path='upload' element={<FileUploadPage />} />
    <Route path='result' element={<ResultPage />} />
    <Route path='result/:category' element={<CategoryPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
))

function App() {
  return (
      <RouterProvider router={router} />
  )
}

export default App;
