import React from 'react';
import './header.styles.scss';

import { ReactComponent as Logo} from '../../assets/algo1.jpg';

const Header = ({ currentUser }) => (
    <div className='header'>
        <Link className='logo-container' to='/'> 
            <Logo className='logo'/>
        </Link>
        <div className='options'>
            <Link className='option' to='/shop'>
                SHOP
            </Link>
            <Link className='option' to='/shop'>
                CONTACT
            </Link>
            { currentUser ? (
            <div className='option' onClick={() => auth.signOut()} >
               SIGN OUT
            </div>
            ) : (
            <Link className='option' to='/signin'> SIGNIN </Link>
            )}
        </div>
    </div>
)
export default Header;