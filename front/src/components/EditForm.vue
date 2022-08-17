<template>
  <div>
    <p>From: {{ shipment.from_addr }}</p>
    <p>To: {{ shipment.to_addr }}</p>
    <p>State: {{ state }}</p> 
    <p>
        <button class="save" v-on:click="$emit('edit-save', shipment.id)">Save</button>
        <button class="cancel" v-on:click="$emit('edit-cancel')">Cancel</button>
    </p>
  </div>
</template>

<script>
export default {
    computed: {
        state() {
            if (this.shipment.state === 'R') {
                return 'Received'
            }
            if (this.shipment.state === 'P') {
                return 'Processing'
            }
            if (this.shipment.state === 'F') {
                return 'Fulfilling'
            }
        }
    },
    props:
        ["shipment"]
}
</script>