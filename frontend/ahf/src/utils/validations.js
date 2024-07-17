import React from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

export const LoginSchema = Yup.object().shape({
  username: Yup.string()
    .min(5, 'Too Short!')
    .max(50, 'Too Long!')
    .required('Required'),
  password: Yup.string()
    .min(8, 'Password must at least 8 chars !')
    .max(50, 'Too Long!')
    .required('Required'),
 
});

