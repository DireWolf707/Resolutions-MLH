<script>
    export let resolution;
    export let period;
    export let interval;
    export let updateID;
    import {createEventDispatcher} from "svelte";
    const dispather = createEventDispatcher();
    let options = [
		'seconds','minutes','hours','days'
  	];
    
</script>

<div class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
  
      <!-- This element is to trick the browser into centering the modal contents. -->
      <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
  
      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
            </div>
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
              <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                {resolution} {period} {interval} {updateID}
              </h3>
              <div class="mt-2">Send me self-help books / guide videos every:<br>
                <input type="number" bind:value="{period}" class="w-1/6 border-2 radius-l">

                <!-- <select class="appearance-none">
                  <option>Yes</option>
                  <option>No</option>
                  <option>Maybe</option>
                </select>  -->

                <select bind:value={interval} class="border-2 radius-l">
                  {#each options as option}
                    <option value={option}>
                      {option}
                    </option>
                  {/each}
                </select>


              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
          <button type="button" on:click="{()=>dispather('schedule_modal',{period,interval})}"
          class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm">
            Schedule
          </button>
        </div>
      </div>
    </div>
  </div>