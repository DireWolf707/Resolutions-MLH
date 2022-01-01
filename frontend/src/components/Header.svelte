<script>
    import user from "../stores/User";
	import tab from "../stores/Tab";
    import { onDestroy } from 'svelte'

    let currTab;
    const unTab = tab.subscribe(tab => currTab=tab);

    let currUser;
    const unUser = user.subscribe(user => currUser=user);

    onDestroy(() => {
        unTab();
        unUser();
    });

    const logout = () => {
        fetch('http://127.0.0.1:8000/auth/token/logout/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `token ${currUser.token}`
            }
        }).then(()=>{
            user.set({token:""})
            tab.set("login");
        });
    }
</script>

<header class="text-gray-600 body-font mb-5 border-b-2">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <div class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
            <span class="ml-3 text-xl">Resolution</span>
        </div>
        <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
        {#if currUser.token}
            <button class="mr-5 hover:text-gray-900" on:click="{logout}">Logout</button>
        {:else}
            <button class="mr-5 hover:text-gray-900" on:click="{()=>tab.set("login")}">Login</button>
            <button class="mr-5 hover:text-gray-900" on:click="{()=>tab.set("signup")}">Signup</button>
        {/if} 
        </nav>
    </div>
</header>