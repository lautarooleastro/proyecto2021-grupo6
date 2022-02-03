<template>
  <div class="panel-body">
    <form>
      <vue-form-generator :schema="schema" :model="model" :options="formOptions">
      </vue-form-generator>
    </form>
  </div>
</template>

<script>
import Vue from 'vue'
import VueFormGenerator from 'vue-form-generator'
import 'vue-form-generator/dist/vfg.css'

Vue.use(VueFormGenerator)

export default {
  data () {
    return {

      model: {
        titulo: 1,
        categoria_id: '',
        descripcion: '',
        coordenadas: '',
        nombre_denunciante: '-34.92053918330889;-57.9541949099075',
        apellido_denunciante: '',
        email_denunciante: '',
        telcel_denunciante: ''
      },

      schema: {
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Titulo',
                model: 'titulo',
                id: 'titulo',
                placeholder: '',
                maxlength: 50,
                validator: "string",
                required: true
              },
              {
                type: "select",
                label: "categoria_id",
                placeholder: "Categoria",
                model: "categoria_id",
                id: 'categoria_id',
                values: function() {
                  return [
                    { id: "1", name: "Error de sistema" },
                    { id: "2", name: "Consulta" }
                  ]
                },
                default: "1",
                validator: "required"
              },
              {
                type: 'textArea',
                label: 'Descripcion',
                model: 'descripcion',
                id: 'descripcion',
                hint: "Max 500 characters",
                max: 500,
                placeholder: 'Descripción detallada',
                rows: 4,
                validator: "string",
                required: true
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Coordenadas',
                model: 'coordenadas',
                id: 'coordenadas',
                placeholder: '',
                maxlength: 50,
                validator: "string",
                required: true
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Nombre',
                model: 'nombre_denunciante',
                id: 'nombre_denunciante',
                placeholder: '',
                maxlength: 40,
                validator: "string",
                required: true
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Apellido',
                model: 'apellido_denunciante',
                id: 'apellido_denunciante',
                placeholder: '',
                maxlength: 40,
                validator: "string",
                required: true
              },
              {
                type: 'input',
                inputType: 'email',
                label: 'E-mail',
                model: 'email_denunciante',
                id: 'email_denunciante',
                placeholder: '',
                maxlength: 40,
                validator: "email",
                required: true
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Telefono',
                model: 'telcel_denunciante',
                id: 'telcel_denunciante',
                placeholder: '',
                maxlength: 25,
                validator: "string",
                required: true
              }
            ]
        },

      formOptions: {
        validateAfterLoad: true,
        validateAfterChanged: true,
        validateAsync: true
      }
    }
  }
}
</script>
