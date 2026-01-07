import React, { useRef } from "react";

/**
 * A simple React component that demonstrates focusing an input field using useRef.
 * When the "Focus Input" button is clicked, the cursor moves inside the input automatically.
 * 
 * @component
 * @example
 * return <FocusInputExample />;
 */
export default function FocusInputExample() {
    /**
     * A ref object pointing to the input DOM element.
     * @type {React.MutableRefObject<HTMLInputElement | null>}
     */
    const inputRef = useRef(null);

    /**
     * Focuses the input element when the button is clicked.
     * Uses the ref's current property to access the DOM node.
     *
     * @function
     * @returns {void}
     */
    const handleFocus = () => {
        if (inputRef.current) {
            inputRef.current.focus();
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>useRef Input Focus Example</h2>

            {/** Input field with attached ref */}
            <input
                type="text"
                placeholder="Type something..."
                ref={inputRef}
                style={{ padding: "5px", marginRight: "10px" }}
            />

            {/** Button that triggers focus */}
            <button onClick={handleFocus} style={{ padding: "5px 10px" }}>
                Focus Input
            </button>
        </div>
    );
}
