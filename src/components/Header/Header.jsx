import React from 'react';
import './header.scss';

export default function Header() {
  return (
    <section className="home">
        <div className="section-container container">
            <div className="home-text">
                <h1 className="title">Visit The Best Destinations In Lesotho With Us</h1>
                <p className="subtitle">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                <button className="btn">
                    <a href="#explore">Explore More</a>
                </button>
            </div>
            <div className="grid">
                <form action="" className='home-card grid'>
                    <div className="location-div">
                        <label htmlFor="location">Location:</label>
                        <input type="text" name="" id="" placeholder="Your Destination"/>
                    </div>
                    <div className="price-div">
                        <label htmlFor="location">Price:</label>
                        <input type="text" name="" id="" placeholder="$500 - $1000"/>
                    </div>
                    <button className="btn" type="submit">Search</button>
                </form>
            </div>
        </div>
    </section>
  )
}
