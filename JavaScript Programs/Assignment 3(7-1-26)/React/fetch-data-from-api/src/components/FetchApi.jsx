import React, { useState } from "react";
import { useEffect } from "react";



export default function FetchApi() {
    const [tempApiData,settempApiData]=useState([]);
    const fetchData = async function(){
        const res = await fetch("https://jsonplaceholder.typicode.com/users")

        const tempData = await res.json();

        settempApiData([...tempApiData, ...tempData]);


        

        // console.log(tempApiData)
    }   

    useEffect(()=>{
        fetchData();
    },[])

    return(

        <>
            <ul>
                {tempApiData.map((user)=>(
                    <li key={user.id}>
                        <strong>{user.name}</strong>
                    </li>
                ))}
            </ul>
        </>

    ); 
}