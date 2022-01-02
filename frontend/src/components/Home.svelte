<script>
    import user from "../stores/User";
    import Modal from "./Modal.svelte";
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "firebase/app";
    import { getFirestore,collection,addDoc,onSnapshot,doc,deleteDoc,updateDoc,query,where } from "firebase/firestore";
    //variables
    let resolution="";
    let userID=$user.userID;   
    let token=$user.token;
    let resoltionList=[];
    let schedule=false;
    //update var
    let updateID="";
    let period="";
    let interval=null;
    const collectionName="resolutions"   
    const baseURL="http://127.0.0.1:8000/schedule/"  
    // Your web app's Firebase configuration
    const firebaseConfig = {
    apiKey: "AIzaSyCrcGP5i9vVde2K2l2MoPZ--3f5dgfVSr0",
    authDomain: "resolutions-b92f1.firebaseapp.com",
    projectId: "resolutions-b92f1",
    storageBucket: "resolutions-b92f1.appspot.com",
    messagingSenderId: "334594601773",
    appId: "1:334594601773:web:d08858f1e014003489d9a4"
    };
    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    const colRef = collection(db,collectionName)
    const q = query(colRef,where("userID","==",userID))

    // realtime update (list)
    onSnapshot(q,(snapshot)=>{
        let tempList=[];
        snapshot.docs.forEach((doc)=>{
            tempList.push({...doc.data(),id:doc.id})
        })
        resoltionList=tempList;
    })
    // add and update
    const add_res = () => {
        if (updateID) {
            let r=resolution;
            let firebase_id=updateID;
            let i=interval;
            let p=period;
            const docRef=doc(db,collectionName,updateID);
            updateDoc(docRef,{
                resolution:resolution,
                period:period,
                interval:interval
            }).then(data =>{
                fetch(baseURL, {
                 method: 'PATCH',
                 headers: {
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'Authorization':`token ${token}`,
                 },
                 body: JSON.stringify(
                     {
                         "resolution": r,
                         "firebase_id": firebase_id,
                         "interval":i,
                         "period":p,
                     }
                 )})
            })
            updateID="";
            period = "";
            interval = null;
        } else {
            let r=resolution;
            addDoc(colRef,{
                resolution:r,
                userID:userID,
                period:1,
                interval:"days"
            }).then(res => res).then(data =>{
                fetch(baseURL, {
                 method: 'POST',
                 headers: {
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'Authorization':`token ${token}`,
                 },
                 body: JSON.stringify(
                     {
                         "resolution": r,
                         "firebase_id": data.id,
                         "interval":1,
                         "period":"days",
                     }
                 )})
            })

        }
        resolution="";
    }
    //update visual change
    const update_res = (id,res,p,i) => {
        resolution=res;
        updateID=id;
        period = i;
        interval = p;
    }
    //delete
    const delete_res = (id) => {
        const docRef=doc(db,collectionName,id);
        deleteDoc(docRef);
        fetch(baseURL, {
            method: 'DELETE',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization':`token ${token}`,
            },
            body: JSON.stringify(
                {
                    "firebase_id": id,
                }
            )});
    }

    const schedule_modal = (e,id,r,p,i) => {
        if (schedule) {
            let data = e.detail;
            interval = data.period;
            period = data.interval;
            add_res();

            updateID="";
            period="";
            interval=null;
            resolution ="";
        } else {
            updateID = id;
            resolution = r;
            period = p;
            interval = i;
        }
        schedule=!schedule;
    }

</script>

{#if schedule}
    <Modal on:schedule_modal={schedule_modal} {resolution} {period} {interval} {updateID}  />
{/if}

<div>
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div class="flex flex-wrap w-full mb-20 flex-col items-center text-center">

            <h2 class="text-2xl text-gray-900">
                I want to  <input type="text" bind:value="{resolution}" class="border-b-2 rounded-l focus:outline-none">
                <button on:click="{()=>add_res()}"
                    class="text-white text-base {updateID ? "bg-yellow-500 hover:bg-yellow-600" : "bg-indigo-500 hover:bg-indigo-600" } border-0 py-2 px-2  rounded">
                    {#if updateID}Update{:else}Add{/if}
                </button>
            </h2>
            
          </div>
          <div class="grid grid-cols-2 gap-4">
            {#each resoltionList as res (res.id) }
              <div>
                <div class="border border-gray-200 p-4 rounded-lg">
                <div class="flex justify-between">
                  <h2 class="text-lg text-gray-900 font-medium title-font mb-2">{res.resolution}</h2>
                    <div class="flex">
                        <button on:click="{()=>update_res(res.id,res.resolution,res.period,res.interval)}"
                        class="flex text-white bg-yellow-500 border-0 py-2 px-2 focus:outline-none hover:bg-yellow-600 rounded text-sm mr-2">Update</button>
                        <button on:click="{()=>delete_res(res.id)}"
                        class="flex text-white bg-red-500 border-0 py-2 px-2 focus:outline-none hover:bg-red-600 rounded text-sm mr-2">Delete</button>
                        <button on:click="{(e)=>schedule_modal(e,res.id,res.resolution,res.period,res.interval)}"
                        class="flex text-white bg-indigo-500 border-0 py-2 px-2 focus:outline-none hover:bg-indigo-600 rounded text-sm">Schedule</button>
                    </div>
                </div>
                </div>
              </div>
            {:else}
            No resolutions....
            {/each}
          </div>
          
        </div>
      </section>
</div>