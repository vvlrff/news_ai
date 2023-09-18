import React from 'react'
import { useParams } from 'react-router-dom'

const CategoryPage = () => {

    const { category } = useParams()

    console.log(category)
    return (
        <div>CategoryPage</div>
    )
}

export default CategoryPage