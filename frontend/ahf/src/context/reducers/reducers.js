const initialState = {
  refreshToken: "",
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_REFRESH_TOKEN':
      return { ...state, refreshToken: action.payload };
    default:
      return state;
  }
};

export default authReducer;
