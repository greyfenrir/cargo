<template>
    <div>
        <h3>List of shipments:</h3>        
        <ShipmentItem
            v-for="shipment of shipments"
            v-bind:shipment="shipment"
            v-on:edit-shipment="editShipment"
        />
    </div>
</template>
<script>
import ShipmentItem from '@/components/ShipmentItem'
export default {
    props: ['shipments'],
    components: { ShipmentItem },
    methods: {
        editShipment(id) {
            this.$emit('edit-shipment', id)
        }
    }
}
</script>