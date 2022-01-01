import { writable } from "svelte/store";


const user = writable(
    {
        token : "",
        userID: -1
    }
)

export default user;