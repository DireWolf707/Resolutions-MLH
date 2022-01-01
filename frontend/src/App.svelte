<script>
	import Signup from "./components/Signup.svelte";
	import Login from "./components/Login.svelte";
	import Header from "./components/Header.svelte";
	import Home from "./components/Home.svelte";
	//stores
	import user from "./stores/User";
	import tab from "./stores/Tab";

	const Tabs = ["login","signup","home"];
	let currTab;
    tab.subscribe(tab => currTab=tab);

	let curretUser;
	user.subscribe(user => curretUser=user);

</script>


<Header />
<main class="px-4 py-2">

	{#if currTab=="login"}
		<Login/>
	{:else if currTab=="signup"}
		<Signup/>
	{:else if currTab=="home" && user.token}
		<Home/>
	{/if}
	
</main>

<style>
</style>