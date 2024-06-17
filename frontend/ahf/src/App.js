import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LoginPage from "./screens/accounts";
import DashBoard from "./screens/mlos";
import AbovebreakpointTable from "./screens/tables";
import "./App.css"
import ResetPassword from "./screens/accounts/reset";


const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage />,
  },
  {
    path: "/dashboard",
    element: <DashBoard />,
  },

  {
    path: "/resetpassword",
    element: <ResetPassword />
  },
  {
    path: "/abovebreakpoint",
    element: <AbovebreakpointTable />,
  },
]);

const App = () => {
  return (
    <div className="App">
         <RouterProvider router={router} />
    </div>
   
  );
};

export default App;
