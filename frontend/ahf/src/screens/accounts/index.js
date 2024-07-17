
import { Button, Label, Card,ListGroup } from "flowbite-react";
import { useState } from "react";
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import { setRefreshToken } from "../../context/action";
import { useDispatch, useSelector } from "react-redux";
import HorizontalLine from '../../components/Line';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { FaGoogle, FaEye, FaEyeSlash } from "react-icons/fa";
import { Dots } from "react-activity";
import Dot from "../../components/activity";
import { LoginSchema } from "../../utils/validations";


const  LoginPage = ({ navigation }) => {
  const authToken = useSelector((state) => state.auth);
  const [showPassword, setShowPassword] = useState(false)
  const [loading, setLoading] = useState(false)
  const [errorMsg, setErrorMsg] = useState("")
  const [errorKey, setErrorKey] = useState("")
  const navigate = useNavigate();
  const dispatch = useDispatch();

  function toggleShowPassword() {
    setShowPassword(!showPassword)
  }

  const handleSubmit =  (values, { event })  => {
    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    };
    const data = {
      username: values.username,
      password: values.password
    };

    axios.post('http://127.0.0.1:8000/auth/jwt/create/', data, config)
      .then(response => {
        if (response != null) {
          const token = response.data.access
          dispatch(setRefreshToken(token));
          navigate("/dashboard")
          setLoading(false)
        }
        else {
          navigate("/")
        }

      })
      .catch(error => {
        console.log("error=", error)
      });
  }


  return (

    <div className="h-screen w-screen bg-[#F2F7FA]">
      <div className="flex justify-center items-center h-screen">
        <Card className="w-[546px] h-[550px] justify-center items-center">
          <p className="text-[#2A3135] text-[32px] font-['Roboto_Slab'] text-center">Sign into your account </p>
          <p className="text-red-500 font-['Roboto_Slab'] text-center">{errorKey} {errorMsg}</p>
          <Formik
            initialValues={{ username: '', password: '' }}
            validationSchema={LoginSchema}
            onSubmit={handleSubmit}
            >
            {({
              values,
              errors,
              touched,
              handleChange,
              handleBlur,
              handleSubmit,
              isSubmitting
            }) => (

              <Form className="flex flex-col gap-4">
                <div>
                  <div className="mb-2 block">
                    <Label htmlFor="username" value="Username" />
                  </div>
                  <Field
                    id="username"
                    type="text"
                    className="w-[369px] h-[38px]" placeholder="John" required
                    name="username"
                    onChange={handleChange}
                    onBlur={handleBlur}
                    value={values.username}

                  />
                  {errors.username && touched.username ? (
                  <div class="text-red-400">
                    {errors.username}</div>
                  ) : null}
                </div>
                <div>
                  <div className="mb-0 block">
                    <Label htmlFor="password" value="Password" />
                  </div>
                  <div>

                  </div>
                  <div className="">
                    <Field
                      id="password"
                      className="w-[369px] h-[38px]" type={showPassword ? 'text' : 'password'} required
                      name="password"
                      placeholder="**********************"
                      onChange={handleChange}
                      onBlur={handleBlur}
                      value={values.password}
                    />
                    {errors.password && touched.password ? (
                    <div class="text-red-400">
                      {errors.password}</div>
                    ) : null}
                    {
                      showPassword ? (
                        <FaEyeSlash
                          className="absolute inset-y-[48%] right-[15%] lg:right-[36%] flex items-center cursor-pointer"
                          onClick={
                            () => toggleShowPassword()
                          }
                        />
                      ) : (
                        <FaEye
                          className="absolute inset-y-[48%] right-[15%] lg:right-[36%] md:right-[10%] flex items-center cursor-pointer"
                          onClick={() => toggleShowPassword()}
                        />
                      )
                    }
                  </div>

                </div>
                <div className="flex items-center justify-end gap-2">
                  <ListGroup.Item href="/resetpassword" className="list-none text-[12px] text-[#194863] mt-[0px] h-[50px] text-center justify-center">
                    Forgot password ?
                  </ListGroup.Item>

                </div>
                {
                  isSubmitting ?
                    <div className="w-[369px] h-[38px] text-center">
                      <Dot />
                    </div>
                    :
                    <Button
                          type="submit"
                          className="w-[369px] h-[38px] text-center"
                        >
                          Sign in
                    </Button>
                }

                <div className="flex items-center">
                  <HorizontalLine width={125} color={'#FFFFFF'} className="" />
                  <p className="mx-4 w-[120px] h-[45px] text-center">Or continue with</p>
                  <HorizontalLine width={95} color={'#FFFFFF'} className="" />
                </div>

              </Form>

            )}
          </Formik>

          <div className="flex justify-between">

            <GoogleOAuthProvider clientId="<your_client_id>">
              Sign in with google
            </GoogleOAuthProvider>
            <FaGoogle />
          </div>
        </Card>
      </div>
    </div>
  );

}

export default LoginPage
