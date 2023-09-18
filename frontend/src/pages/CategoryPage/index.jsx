import React from 'react'
import { useLocation } from 'react-router-dom'

const CategoryPage = () => {
    const location = useLocation();
    const { state } = location;

    console.log(state)

    return (
        <div>
            {state.category}
            {Object.entries(state.data).map(([key, value]) => (
                <div key={key}>
                    <div className='card-spec'>
                        {key}: {value}
                    </div >
                </div>
            ))}
        </div>
    )
}

export default CategoryPage