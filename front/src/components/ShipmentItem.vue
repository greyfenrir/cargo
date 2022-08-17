<template>
  <div>
    <ul>
        <li>
            From: {{ shipment.from_addr }}, 
            To: {{ shipment.to_addr }}, 
            State: {{ state }} 
            <button class="edit" v-on:click="$emit('edit-shipment', shipment.id)"> 
                Edit
            </button>
        </li>
    </ul>
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
    props: {
        shipment: {
            type: Object,
            required: true
        }
    }
}
</script>