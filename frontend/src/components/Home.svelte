<script>
    import user from "../stores/User";
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "firebase/app";
    import { getFirestore,collection,addDoc,onSnapshot,doc,deleteDoc,updateDoc,query,where } from "firebase/firestore";
    //variables
    let resolution="";
    let userID=$user.userID;   
    let updateID="";
    let resoltionList=[];
    const collectionName="resolutions"     
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

    onSnapshot(q,(snapshot)=>{
        let tempList=[];
        snapshot.docs.forEach((doc)=>{
            tempList.push({...doc.data(),id:doc.id})
        })
        resoltionList=tempList;
    })

    const add_res = () => {
        if (updateID) {
            const docRef=doc(db,collectionName,updateID);
            updateDoc(docRef,{
                resolution:resolution
            })
            updateID="";
        } else {
            addDoc(colRef,{
                resolution:resolution,
                userID:userID
            })
        }
        resolution="";
    }

    const update_res = (id,res) => {
        resolution=res;
        updateID=id;
    }

    const delete_res = (id) => {
        const docRef=doc(db,collectionName,id);
        deleteDoc(docRef);
    }

</script>

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
                        <button on:click="{()=>update_res(res.id,res.resolution)}"
                        class="flex text-white bg-yellow-500 border-0 py-2 px-2 focus:outline-none hover:bg-yellow-600 rounded text-sm mr-2">Update</button>
                        <button on:click="{()=>delete_res(res.id)}"
                        class="flex text-white bg-red-500 border-0 py-2 px-2 focus:outline-none hover:bg-red-600 rounded text-sm mr-2">Delete</button>
                        <button 
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