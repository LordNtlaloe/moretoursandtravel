import React from 'react';
import './blog.scss';
import { BsArrowRightShort } from 'react-icons/bs'
import img1 from '../../Images/dannii-coughlan-tk4OYV3L8Ts-unsplash.jpg'
export default function Blog() {

    const posts = [
        {
            id : 1,
            image: img1,
            details: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, laboriosam earum fuga accusamus alias, repudiandae consequatur ab deleniti placeat consectetur nihil, tenetur dolor aliquam nostrum. Optio explicabo ipsam sunt tempore?',
            title: 'Lorem ipsum dolor sit amet.'
        },
        {
            id : 2,
            image: img1,
            details: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, laboriosam earum fuga accusamus alias, repudiandae consequatur ab deleniti placeat consectetur nihil, tenetur dolor aliquam nostrum. Optio explicabo ipsam sunt tempore?',
            title: 'Lorem ipsum dolor sit amet.'
        },
        {
            id : 3,
            image: img1,
            details: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, laboriosam earum fuga accusamus alias, repudiandae consequatur ab deleniti placeat consectetur nihil, tenetur dolor aliquam nostrum. Optio explicabo ipsam sunt tempore?',
            title: 'Lorem ipsum dolor sit amet.'
        },
        {
            id : 4,
            image: img1,
            details: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, laboriosam earum fuga accusamus alias, repudiandae consequatur ab deleniti placeat consectetur nihil, tenetur dolor aliquam nostrum. Optio explicabo ipsam sunt tempore?',
            title: 'Lorem ipsum dolor sit amet.'
        },
        {
            id : 5,
            image: img1,
            details: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, laboriosam earum fuga accusamus alias, repudiandae consequatur ab deleniti placeat consectetur nihil, tenetur dolor aliquam nostrum. Optio explicabo ipsam sunt tempore?',
            title: 'Lorem ipsum dolor sit amet.'
        },
    ]
    return (
    <section className="section blog container">
        <div className="section-container">
            <div className="section-intro">
                <h2 className="section-title">
                    Our Blog
                </h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam iusto, exercitationem quibusdam eaque reiciendis laborum.</p>    
            </div>
            <div className="main-container grid">
                {
                    posts.map(({id, image, details, title}) => {
                        return(
                            <div className="single-post grid" key={id}>
                                <div className="image-div">
                                    <img src={image} alt="" />
                                </div>
                                <div className="post-details">
                                    <h3>{title}</h3>
                                    <p>{details}</p>
                                </div>
                                <a href="/" className="flex">
                                    Read More
                                    <BsArrowRightShort className='icon'/>
                                </a>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    </section>
  )
}
