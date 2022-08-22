<template>
    <div>
        <h3>List of shipments:</h3>
        <ShipmentItem
            v-for="shipment of shipments"
            v-bind:shipment="shipment"
            :key="shipment.id"
            v-on:edit-shipment="editShipment"
            v-on:delete-shipment="deleteShipment"
        />
        <p>
        <button class="add" v-on:click="$emit('add-shipment')"> 
        Add new
        </button></p>
    </div>
</template>
<script>
import ShipmentItem from '@/components/ShipmentItem'
export default {
    props: ['shipments'],
    components: { ShipmentItem },
    methods: {
        editShipment(shipment) {
            this.$emit('edit-shipment', shipment)
        },
        deleteShipment(shipment) {
            this.$emit('delete-shipment', shipment)
        }
    }
}
</script>