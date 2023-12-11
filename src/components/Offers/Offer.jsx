import React from 'react';
import './offer.scss';
import { MdAirportShuttle, MdBathtub, MdKingBed, MdLocationOn } from 'react-icons/md';
import { FaWifi } from 'react-icons/fa';
import { BsArrowRightShort } from 'react-icons/bs';
import Maletsunyane from '../../Images/maletsunyale.jpg';
import Katse from '../../Images/katse-dam.jpg';
import Kome from '../../Images/kome-caves.jpg';

const Offers = [
    {
        id: 1,
        image: Maletsunyane,
        title: 'Maletsunyane Falls',
        location: 'Semonkong',
        grade: 'Natural Occurrence',
        price: 'M2000.00'
      },
      {
        id: 2,
        image: Katse,
        title: 'Katse Dam',
        location: 'Thaba-Tseka',
        grade: 'Man-Made Structure',
        price: 'M2500.00'
      },
      {
        id: 3,
        image: Kome,
        title: 'Kome Caves',
        location: 'Berea',
        grade: 'Cultural Site',
        price: 'M2800.00'
      }
]

export default function Offer() {
  return (
    <section className="offer container section">
        <div className="section-container">
            <div className="section-intro">
                <div className="section-title">
                    <h2>Tour Prices</h2>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, expedita!</p>
                </div>
            </div>
            <div className="main-container grid">
                {
                    Offers.map(({id, image, price, location, title})=>{
                        return(<div className="single-offer" key={id}>
                        <div className="destination-image">
                            <img src={image} alt="" />
                            <span className="discount">
                                20% Off
                            </span>
                        </div>
                        <div className="offer-body">
                            <div className="price flex">
                                <h4>{price}</h4>
                                <span className="status">
                                    Now Touring
                                </span>
                            </div>
                            <div className="amenities flex">
                                <div className="single-amenity flex">
                                    <MdKingBed className='icon'/>
                                    <small>1 Bed</small>
                                </div>
                                <div className="single-amenity flex">
                                    <MdBathtub className='icon'/>
                                    <small>1 Bathroom</small>
                                </div>
                                <div className="single-amenity flex">
                                    <FaWifi className='icon'/>
                                    <small>Free Wifi</small>
                                </div>
                                <div className="single-amenity flex">
                                    <MdAirportShuttle className='icon'/>
                                    <small>Shuttle</small>
                                </div>
                            </div>
                            <div className="location flex">
                                <MdLocationOn className='icon' />
                                <small>{title}, {location}</small>
                            </div>
                            <button className="btn flex">
                                View Details
                                <BsArrowRightShort className='icon'/>
                            </button>
                        </div>
                    </div>)
                    })
                }
            </div>
        </div>
    </section>
  )
}
