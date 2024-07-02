import persistReducer from "redux-persist/es/persistReducer";
import storage from "redux-persist/lib/storage";

const initialState = {
  refreshToken: "",
  modal:false
};

const persistConfig = {
  key: 'root',
  storage
};

const authReducer1 = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_REFRESH_TOKEN':
      return { ...state, refreshToken: action.payload };
    default:
      return state;
  }
};


const showModalReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_SHOW_MODAL':
      return { ...state, showModal: action.payload };
    default:
      return state;
  }
};

const authReducer       = persistReducer(persistConfig, authReducer1);
const _showModalReducer = persistReducer(persistConfig, showModalReducer);

export default authReducer
  


