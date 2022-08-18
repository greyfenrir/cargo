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
const DRF_URI = 'http://127.0.0.1:8000/shipments/';
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
        fetch (DRF_URI)
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
            const response = fetch(DRF_URI + id, {
                method: 'DELETE'
            })
            console.log(response)
        },
        editSave(id, from, to, state) {
            // some checks here...
            this.shipment.from_addr = from
            this.shipment.to_addr = to
            this.shipment.state = state
            this.newShipment = false
            // todo: send to backend
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