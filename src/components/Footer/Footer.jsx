import React from 'react';
import './footer.scss';
import logo from '../../Images/logo.png';
import {ImFacebook} from 'react-icons/im';
import {BsTwitter} from 'react-icons/bs';
import { AiFillInstagram } from 'react-icons/ai';

export default function Footer() {
  return (
    <div className='footer'>
      <div className="section-container container grid">
        <div className="logo-div">
          <div className="footer-logo">
            <a href="/" className="logo flex">
              <img src={logo} alt="" className='icon'/>
            </a>
          </div>
          <div className="socials flex">
            <ImFacebook className='icon'/>
            <BsTwitter className='icon'/>
            <AiFillInstagram className='icon'/>
          </div>
        </div>
        <div className="footer-links">
          <span className="link-title">
            Information
          </span>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/">Explore</a></li>
            <li><a href="/">Travel</a></li>
            <li><a href="/">Blog</a></li>
            <li><a href="/">Terms & Conditions</a></li>
          </ul>
        </div>
        <div className="footer-links">
          <span className="link-title">
            Contact Us
          </span>
          <span className="phone">+266 6363 6363</span>
          <span className="email">moretours@mail.com</span>
        </div>
      </div>
    </div>
  )
}
