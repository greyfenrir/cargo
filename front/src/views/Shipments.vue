<template>
  <div class="home">
    <EditForm 
        v-if="editMode"
        v-bind:id="shipment.id"
        v-bind:from="shipment.from_addr"
        v-bind:to="shipment.to_addr"
        v-bind:state="shipment.state"
        v-on:edit-save="editSave"
        v-on:edit-cancel="editCancel"
    />
    <ShipmentList
        v-if="!editMode"
        v-bind:shipments="shipments"
        @edit-shipment="editShipment"
        @delete-shipment="deleteShipment"
        @add-shipment="addShipment"
    />
  </div>
</template>

<script>
import ShipmentList from '@/components/ShipmentList';
import EditForm from '@/components/EditForm.vue';
export default {
    data() {
        return {
            shipments: [],
            editMode: false,
            newShipment: false
        }
    },
    components: {
    ShipmentList,
    EditForm
},
    mounted() {
        fetch ('http://127.0.0.1:8000/shipments/')
            .then(response => response.json())
            .then(json => {this.shipments = json})
    },
    methods: {
        addShipment(){
            const shipment = {
                id: Date.now(),
                created: Date.now(),
                from_addr: "",
                to_addr: "",
                owner: "admin"
            }
            this.newShipment = true
            this.shipments.push(shipment)
            this.editShipment(shipment.id)
        },
        editShipment(id) {
            this.shipment = this.shipments.filter(s => s.id === id)[0]
            this.switchEditMode()
        },
        deleteShipment(id) {
            this.shipments = this.shipments.filter(s => s.id != id)
        },
        editSave(id, from, to, state) {
            // some checks here...
            this.shipment.from_addr = from
            this.shipment.to_addr = to
            this.shipment.state = state
            this.newShipment = false
            this.switchEditMode()
        },
        editCancel(id) {
            // handle new flag
            if (this.newShipment) {
                this.deleteShipment(id)
            }
            this.switchEditMode()
        },
        switchEditMode() {
            this.editMode = !this.editMode
        }
    }
}
</script>