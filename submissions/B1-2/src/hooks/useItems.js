import {useContext} from 'react';
import {Store} from '../lib/store.js';
export default function useItems(){return useContext(Store)}
