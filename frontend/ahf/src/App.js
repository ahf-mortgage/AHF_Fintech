import { createHashRouter, Route, RouterProvider, Routes } from "react-router-dom";
import LoginPage from "./screens/accounts";
import DashBoard from "./screens/MLO";



const App = () => {
  const router = createHashRouter([
    {
      path: "/",
      element: <LoginPage />,
    },
    {
      path: "dashboard",
      element: <DashBoard />,
    },
  ]);

  return (
    <RouterProvider router={router}>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="dashboard/" element={<DashBoard />} />
      </Routes>
    </RouterProvider>
  );
};

export default App;
