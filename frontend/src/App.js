import { Route, createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';
import Layout from "./components/Layout";
import HomePage from './pages/HomePage';
import NotFoundPage from './pages/NotFoundPage';
import DataPage from './pages/DataPage';

const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />} >
    <Route index element={<HomePage />} />
    <Route path='data' element={<DataPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
))

function App() {
  return (
      <RouterProvider router={router} />
  )
}

export default App;
