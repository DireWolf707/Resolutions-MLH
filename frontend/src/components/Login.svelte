<script>
    import user from "../stores/User";
	import tab from "../stores/Tab";
    let username="";
    let password="";

    const login = () => {
        fetch('http://127.0.0.1:8000/auth/token/login/', {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                "password": password,
                "username": username
            }
        )}).then(res => res.json()).then((data) => {
            if (data.auth_token) {
                user.set({
                    token : data.auth_token
                });
                tab.set("home");
            } else {
                console.log(data)
            }
        });
    }
</script>

<form class="w-1/3 mx-auto body-font bg-gray-100 p-8 rounded-xl" on:submit|preventDefault="{login}">
    <h2 class="text-gray-900 text-lg font-medium title-font mb-5">Login In</h2>
    <div class="relative mb-4">
        <label for="username" class="leading-7 text-sm text-gray-600">Username</label>
        <input type="text" id="username" name="username" bind:value="{username}"
        class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
    </div>
    <div class="relative mb-4">
        <label for="password" class="leading-7 text-sm text-gray-600">Password</label>
        <input type="password" id="password" name="password" bind:value="{password}"
        class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
    </div>
    <button class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg w-full">login</button>
</form>