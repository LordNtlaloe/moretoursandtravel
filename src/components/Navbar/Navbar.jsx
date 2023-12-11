import React, { useState } from 'react';
import './navbar.scss';
import logo from '../../Images/logo.png';
import {AiFillCloseCircle} from 'react-icons/ai';
import {TbGridDots} from 'react-icons/tb';

export default function Navbar() {
    const [active, setActive] = useState('navbar')
    const [transparency, setTransparency] = useState('header')
    const showNav = () => {
        setActive('navbar active-nav')
    }
    const closeNav = () =>{
        setActive('navbar')
    }

    const addBackground = () => {
        if(window.scrollY >= 10){
            setTransparency('header active-header')
        }
        else{
            setTransparency('header')           
        }
    } 
    window.addEventListener('scroll', addBackground)
    return (
        <section className="navbar-section">
            <div className={transparency}>
                <div className="nav-logo">
                    <a href="/" className="logo">
                        <img src={logo} alt="" className='logo'/>
                    </a>
                </div>
                <div className={active}>
                    <ul className="nav-list flex">
                        <li className="nav-item">
                            <a href="/" className="nav-link">Home</a>
                        </li>
                        <li className="nav-item">
                            <a href="#destinations" className="nav-link">Destinations</a>
                        </li>
                        <li className="nav-item">
                            <a href="#pricing" className="nav-link">Pricing</a>
                        </li>
                        <li className="nav-item">
                            <a href="#popular" className="nav-link">Popular Places</a>
                        </li>
                        <li className="nav-item">
                            <a href="#more" className="nav-link">More</a>
                        </li>
                        <div className="header-btn flex">
                            <button className="btn login-btn">
                                <a href="#login">Login</a>
                            </button>
                            <button className="btn">
                                <a href="#login">Register</a>
                            </button>
                        </div>
                    </ul>
                    <div onClick={closeNav} className="close-nav">
                        <AiFillCloseCircle className="icon" />
                    </div>
                </div>
                <div onClick={showNav} className="toggle-nav">
                    <TbGridDots className="icon"/>
                </div>
            </div>
        </section>
    )
}
