import React, { useState } from "react";

import Child1 from "./Child1";
import Child2 from "./Child2";


export default function Parent(){

    const [name,setName] = useState("");

    return(<>

        <Child1 setName={setName}/>
        <Child2 name={name}/>
    
    </>);
}