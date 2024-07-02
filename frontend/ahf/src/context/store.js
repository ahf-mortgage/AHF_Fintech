import { createStore, combineReducers } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage'; 
import authReducer from './reducers/reducers';
import _showModalReducer from './reducers/reducers';


const persistConfig = {
  key: 'root',
  storage
};

const rootReducer = combineReducers({
  auth :authReducer,
  modal:_showModalReducer

});


const persistedReducer = persistReducer(persistConfig, rootReducer);
const store = createStore(persistedReducer);
const persistor = persistStore(store);

export { store, persistor };