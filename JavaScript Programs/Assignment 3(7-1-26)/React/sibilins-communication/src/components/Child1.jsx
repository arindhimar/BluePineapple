import React from "react";


export default function Child1({setName}) {
    return (
        <input
            type="text"
            onChange={(e) => setName(e.target.value)}
        />
    );
}