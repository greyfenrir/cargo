import { mount } from '@vue/test-utils'
import EditForm from '@/components/EditForm.vue'

const factory = () => {
  const shipment = {from_addr: 'fr.a', to_addr: 't.a', state: 'Done'}
  return mount(
    EditForm, {
      props: {shipment}})
}

describe('EditForm.vue', () => {
  it('shows from_addr field', () => {    
    const wrapper = factory()
    const input_fields = wrapper.findAll('input[type="text"]')
    expect(input_fields.at(0).element.value).toBe(wrapper.props().shipment.from_addr)
    expect(input_fields.at(1).element.value).toBe(wrapper.props().shipment.to_addr)    
  })  

  it('emits edit-save event', () => {
    const wrapper = factory()
    // trigger an event when the 'Save' button is clicked
    wrapper.findAll('button').at(0).trigger('click')
  
    // check that 1 occurrence of the event has been emitted
    expect(wrapper.emitted('edit-save')).toBeTruthy()    
  })
  
})
