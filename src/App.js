import React from 'react';
import './app.css';
import Navbar from './components/Navbar/Navbar';
import Header from './components/Header/Header';
import Popular from './components/Popular/Popular';
import Offer from './components/Offers/Offer';
import About from './components/About/About';
import Blog from './components/Blog/Blog';
import Footer from './components/Footer/Footer';

export default function App() {
  return (
    <div>
        <Navbar />
        <Header />
        <Popular />
        <Offer />
        <About />
        <Blog />
        <Footer />
    </div>
  )
}
