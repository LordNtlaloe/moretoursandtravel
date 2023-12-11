import React from 'react';
import './popular.scss';
import { BsArrowLeftShort, BsDot } from 'react-icons/bs';
import { BsArrowRightShort } from 'react-icons/bs';
import Maletsunyane from '../../Images/maletsunyale.jpg';
import Katse from '../../Images/katse-dam.jpg';
import Kome from '../../Images/kome-caves.jpg';

export default function Popular() {

  const Data = [
    {
      id: 1,
      image: Maletsunyane,
      title: 'Maletsunyane Falls',
      location: 'Semonkong',
      grade: 'Natural Occurrence'
    },
    {
      id: 2,
      image: Katse,
      title: 'Katse Dam',
      location: 'Thaba-Tseka',
      grade: 'Man-Made Structure'
    },
    {
      id: 3,
      image: Kome,
      title: 'Kome Caves',
      location: 'Berea',
      grade: 'Cultural Site'
    }
  ]

  return (
    <section className="popular section container">
      <div className="section-container">
        <div className="section-header flex">
          <div className="text-div">
            <h2 className="section-title">Popular Destinations</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, mollitia!</p>
          </div>
          <div className="icons-div flex">
            <BsArrowLeftShort className='icon left-icon'/>
            <BsArrowRightShort className='icon right-icon'/>
          </div>
        </div>
        <div className="main-container grid">
          {
            Data.map(({id, image, title, location,grade}) =>{
              return(
                <div className="single-destination" key={id}>
                  <div className="destination-image">
                    <img src={image} alt="" />
                    <div className="overlay-info">
                      <h3>{title}</h3>
                      <p>{location}</p>
                      <BsArrowRightShort className='icon left-icon'/>
                    </div>
                  </div>
                  <div className="destination-footer">
                    <div className="number">0{id}</div>
                    <div className="destination-text flex">
                      <h6>{title}</h6>
                      <span className='flex'>
                        <span className="dot">
                          <BsDot className='icon'/>
                        </span>
                      </span>
                    </div>
                  </div>
                </div>
              )
            })
          }
      </div>
    </div>
  </section>
  )
}
