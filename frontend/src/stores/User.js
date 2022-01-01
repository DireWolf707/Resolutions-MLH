import { writable } from "svelte/store";


const user = writable(
    {
        token : ""
    }
)

export default user;