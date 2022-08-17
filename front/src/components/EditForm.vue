<!-- <template>
  <div>
    <p>From: {{ shipment.from_addr }}</p>
    <p>To: {{ shipment.to_addr }}</p>
    <p>State: {{ state }}</p> 
    
  </div>
</template> -->
<template>
  <form>
    <p>
        <label>From: </label><input type="text" v-model="from"/>
        <label>To: </label><input type="text" v-model="to"/>
        <label>State: </label><input type="text" v-model="state"/>
    </p>
    <p>
        <button class="save" v-on:click="$emit('edit-save', id, from, to, state)">Save</button>
        <button class="cancel" v-on:click="$emit('edit-cancel')">Cancel</button>
    </p>
  </form>
</template>

<script>
export default {
    props:
        ["id", "from", "to", "state"]
}
</script>