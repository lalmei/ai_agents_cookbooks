<script>
    import EntriesList from "./EntriesList.svelte";
    import IntroForm from "./IntroForm.svelte";

    let step = 0;

    function nextStep() {
        step += 1;
    }

    function prevStep() {
        step -= 1;
    }

    // Gather data from the database endpoint
    let entries = [];

    async function getEntries() {
        if (false) {
            fetch('http://localhost:3000/api/entries')
                .then(res => res.json())
                .then(data => {
                    entries = data;
                });
        }
        entries = [
            { title: 'Entry 1' },
            { title: 'Entry 2' },
            { title: 'Entry 3' }
        ]
    }

    getEntries();


    // Create a variable to be mutated by a child component
    let formData = {}

    async function handleSubmit(event) {
        event.preventDefault();

        let formText = "Please provide food resources that match the following criteria\n"
        for (const [key, value] of Object.entries(formData)) {
            formText += `${key}: ${value}\n`
        }

        // Send the form data to the server at the /formsubmit endpoint
        fetch('/formsubmit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(res => res.json())
            .then(data => {
                console.log(data);
                nextStep();
            });
    }
</script>


{#await getEntries()}
    <p>Loading...</p>
{:then}
    {#if step === 0}
        <EntriesList entries={entries} />
        <button on:click={nextStep}>Next</button>
    {:else if step === 1}

        <IntroForm bind:formData={formData} handleSubmit={handleSubmit}/>

        <button on:click={prevStep}>Previous</button>
    {:else}
        <p>Done!</p>
        <button on:click={prevStep}>Previous</button>
    {/if}
{:catch error}
    <p>{error.message}</p>
{/await}
