<script>
	import tab from "../stores/Tab";
    let email="";
    let username="";
    let password="";
    //let otp="";

    const signup = () => {
        fetch('http://127.0.0.1:8000/auth/users/', {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                "email":email,
                "password": password,
                "username": username
            }
        )}).then(res => res.json()).then((data) => {
            if (data.id) {
                tab.set("login");
            } else {
                console.log(data);
            }
        });
    }
</script>

<section class="text-gray-600 body-font bg-gray-100 rounded-xl mb-5">
<div class="container px-5 py-24 mx-auto flex flex-wrap items-center">
    <div class="lg:w-3/5 md:w-1/2 md:pr-16 lg:pr-0 pr-0">
    <h1 class="title-font font-medium text-3xl text-gray-900">Slow-carb next level shoindcgoitch ethical authentic, poko scenester</h1>
    <p class="leading-relaxed mt-4">Poke slow-carb mixtape knausgaard, typewriter street art gentrify hammock starladder roathse. Craies vegan tousled etsy austin.</p>
    </div>
    <form on:submit|preventDefault="{signup}"
    class="lg:w-2/6 md:w-1/2 bg-gray-100 rounded-lg p-8 flex flex-col md:ml-auto w-full mt-10 md:mt-0 border-4 rounded-xl mr-8">
        <h2 class="text-gray-900 text-lg font-medium title-font mb-5">Sign Up</h2>

        <div class="relative mb-4">
            <label for="email" class="leading-7 text-sm text-gray-600">Email</label>
            <input type="email" id="email" name="email" bind:value="{email}"
            class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
        </div>
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

        <!-- <div class="mb-3 flex justify-between"> 
            <div class="relative mb-4">
                <label for="otp" class="leading-7 text-sm text-gray-600">Otp</label>
                <input placeholder="6-digits" maxlength="6" type="text" id="otp" name="otp" class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
            <button  class="bg-white w-2/7 rounded-lg border text-gray-500 hover:text-white hover:bg-indigo-400 px-4 py-2 border-gray-300 mb-4 mt-6">Send Otp</button>
        </div> -->

        <button class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Signup</button>
    </form>
</div>
</section>