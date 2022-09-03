<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.2"?>
<plugin>
  <!--
    Standard module definition extension point
  -->
  <extension point="dreisoft.tresos.launcher2.plugin.module"
             id="#{COMPONENT}_TS_#{VERSION}"
             name="#{COMPONENT}_TS_#{VERSION} Module">

    <module id="#{COMPONENT}_TS_#{VERSION}"
            label="#{COMPONENT}_TS_#{VERSION}"
            mandatory="false"
            allowMultiple="false"
            description="ECU Information"
            copyright="(c) #{YEAR} #{COMPANY}"
            swVersionMajor="#{MAJOR}"
            swVersionMinor="#{MINOR}"
            swVersionPatch="#{PATCH}"
            specVersionMajor="4"
            specVersionMinor="0"
            specVersionPatch="0"
            specVersionSuffix="0000"
            relVersionMajor="#{AR_MAJOR}"
            relVersionMinor="#{AR_MINOR}"
            relVersionPatch="#{AR_PATCH}"
            categoryType="#{COMPONENT}"
            categoryLayer="Drivers"
            categoryCategory="ECU Firmware"
            categoryComponent="ECUC">
    </module>
   </extension>

   <!--
    extension point defining the schema and data structure of the module
   -->
   <extension point="dreisoft.tresos.launcher2.plugin.configuration"
             id="#{COMPONENT}_TS_#{VERSION}_ConfigId"
             name="#{COMPONENT}_TS_#{VERSION} Configuration">
      <configuration moduleId="#{COMPONENT}_TS_#{VERSION}">

         <!-- schema definition -->
         <schema>
            <manager class="dreisoft.tresos.autosar2.resourcehandling.AutosarSchemaManager"/>
            <resource value="config/#{COMPONENT}.xdm" type="xdm"/>
         </schema>

         <!-- data definition -->
         <data>
            <manager class="dreisoft.tresos.autosar2.resourcehandling.AutosarConfigManager"/>
            <schemaNode path="ASPath:/#{AR_PACKAGE}/#{COMPONENT}"/>
         </data>

         <editor id="#{COMPONENT}_TS_#{VERSION}_EditorId"
            label="Default"
            tooltip="#{COMPONENT}">
            <class class="dreisoft.tresos.launcher2.editor.GenericConfigEditor">
               <parameter name="schema" value="ASPath:/#{AR_PACKAGE}/#{COMPONENT}"/>
               <parameter name="title" value="#{COMPONENT}"/>
            </class>
         </editor>
      </configuration>
   </extension>

   <extension
        point="dreisoft.tresos.guidedconfig.api.plugin.guidedconfigwizard">
      <guidedconfigwizard id="#{COMPONENT}">
        <backend class="#{PACKAGE}.#{BACKEND_CLASS}"/>
        <gui class="#{PACKAGE}.#{PAGE_CLASS}"/>
        <resultGui
              class="dreisoft.tresos.guidedconfig.api.gui.page.ChangedDCtxtsResultWidget"
              plugin="dreisoft.tresos.guidedconfig.api.plugin">
        </resultGui>
      </guidedconfigwizard>
   </extension>
   <extension
        point="dreisoft.tresos.guidedconfig.api.plugin.trigger">
      <trigger>
        <autoconfigure
              id="#{COMPONENT}" wizardId="#{COMPONENT}">
           <display
                 label="#{COMPONENT} Autoconfiguration"
                 tooltip="#{COMPONENT} Autoconfiguration">
           </display>
           <visibility></visibility>
         </autoconfigure>
      </trigger>
   </extension>
  
    <extension
        point="dreisoft.tresos.guidedconfig.api.plugin.pushservice">
      <pushoperation
           desc="#{COMPONENT} Autoconfigure Operation"
           id="#{COMPONENT}AutoconfigureOperation"
           name="#{COMPONENT} Autoconfigure Operation">
         <operationclass
              class="dreisoft.tresos.guidedconfig.demo7.ExampleAutoconfigureOperation">
         </operationclass>
         <event>
            <with variable="class">
               <equals value="dreisoft.tresos.guidedconfig.demo7.ExampleAutoconfigureEvent"/>
            </with>
         </event>
      </pushoperation>
   </extension>

</plugin>
