import React from 'react';
import './about.scss';
import { MdAirportShuttle, MdLandscape, MdPerson} from 'react-icons/md';
import video from '../../Images/video.mp4';

export default function About() {
  return (
    <section className="about section">
        <div className="section-container">
            <h3 className="title">
                Why Travel With Us?
            </h3>
            <div className="main-container container grid">
                <div className="single-item">
                    <MdAirportShuttle className='icon' />
                    <h3>Tours Completed</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident, voluptates?</p>
                </div>
                <div className="single-item">
                    <MdPerson className='icon'/>
                    <h3>Customer Satisfaction</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident, voluptates?</p>
                </div>
                <div className="single-item">
                    <MdLandscape className='icon'/>
                    <h3>Great Experience</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident, voluptates?</p>
                </div>
            </div>
            <div className="video-card container">
                <div className="card-content grid">
                    <div className="card-text">
                        <h2>Wonderful Experiences</h2>
                        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Praesentium provident error omnis nulla laudantium corrupti!</p>
                    </div>
                    <div className="card-video">
                        <video src={video} autoPlay loop muted type="video/mp4"></video>
                    </div>
                </div>
            </div>
        </div>
    </section>
  )
}
