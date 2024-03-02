<script>
    export let formData = {};
    export let handleSubmit;

</script>

<form on:submit={handleSubmit}>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" bind:value={formData.name}>

    <!-- Age -->
    <label for="age">Age</label>
    <input type="number" id="age" name="age" bind:value={formData.age}>

    <!-- Phone number -->
    <label for="phone-number">Phone number</label>
    <input type="text" id="phone-number" name="phone-number" bind:value={formData.phoneNumber}>

    <!-- Language Dropdown -->
    <label for="language">Language</label>
    <select id="language" name="language" bind:value={formData.language}>
        <option value="english">English</option>
        <option value="spanish">Spanish</option>
        <option value="french">French</option>
        <option value="german">German</option>
        <option value="italian">Italian</option>
        <option value="portuguese">Portuguese</option>
        <option value="chinese">Chinese</option>
        <option value="japanese">Japanese</option>
        <option value="korean">Korean</option>
        <option value="arabic">Arabic</option>
        <option value="russian">Russian</option>
        <option value="hindi">Hindi</option>
        <option value="bengali">Bengali</option>
        <option value="punjabi">Punjabi</option>
        <option value="urdu">Urdu</option>
        <option value="turkish">Turkish</option>
        <option value="dutch">Dutch</option>
        <option value="greek">Greek</option>
        <option value="hebrew">Hebrew</option>
        <option value="indonesian">Indonesian</option>
        <option value="malay">Malay</option>
        <option value="thai">Thai</option>
        <option value="vietnamese">Vietnamese</option>
        <option value="swahili">Swahili</option>
        <option value="tagalog">Tagalog</option>
        <option value="polish">Polish</option>
        <option value="ukrainian">Ukrainian</option>
        <option value="czech">Czech</option>
        <option value="slovak">Slovak</option>
        <option value="hungarian">Hungarian</option>
        <option value="finnish">Finnish</option>
        <option value="swedish">Swedish</option>
        <option value="norwegian">Norwegian</option>
        <option value="danish">Danish</option>
        <option value="icelandic">Icelandic</option>
        <option value="faroese">Faroese</option>
    </select>

    <!-- Commute -->
    <label for="commute">Commute</label>
    <select id="commute" name="commute" bind:value={formData.commute}>
        <option value="walk">Walk</option>
        <option value="bike">Bike</option>
        <option value="bus">Bus</option>
        <option value="car">Car</option>
        <option value="train">Train</option>
        <option value="subway">Subway</option>
        <option value="ferry">Ferry</option>
        <option value="helicopter">Helicopter</option>
    </select>

    <!-- No Cook? -->
    <label for="cook">Can you cook?</label>
    <select id="cook" name="cook" bind:value={formData.cook}>
        <option value="yes">Yes</option>
        <option value="no">No</option>
    </select>

    <!-- Family Size -->
    <label for="family">Family Size</label>
    <input type="number" id="family" name="family" bind:value={formData.family}>

    <!-- Desired visit day checkboxes -->
    <label for="day">Desired Visit Day</label>

    <input type="checkbox" id="monday" name="monday" value="monday" bind:checked={formData.monday}>
    <label for="monday">Monday</label>

    <input type="checkbox" id="tuesday" name="tuesday" value="tuesday" bind:checked={formData.tuesday}>
    <label for="tuesday">Tuesday</label>

    <input type="checkbox" id="wednesday" name="wednesday" value="wednesday" bind:checked={formData.wednesday}>
    <label for="wednesday">Wednesday</label>

    <input type="checkbox" id="thursday" name="thursday" value="thursday" bind:checked={formData.thursday}>
    <label for="thursday">Thursday</label>

    <input type="checkbox" id="friday" name="friday" value="friday" bind:checked={formData.friday}>
    <label for="friday">Friday</label>

    <input type="checkbox" id="saturday" name="saturday" value="saturday" bind:checked={formData.saturday}>
    <label for="saturday">Saturday</label>

    <input type="checkbox" id="sunday" name="sunday" value="sunday" bind:checked={formData.sunday}>
    <label for="sunday">Sunday</label>

    <button type="submit">Submit</button>
</form>

<style>
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
