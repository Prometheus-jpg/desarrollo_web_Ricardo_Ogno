package com.tareas.tarea4.service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.tareas.tarea4.models.AvisoAdopcion;
import com.tareas.tarea4.repository.AvisoAdopcionRepository;

@Service
public class AvisoServiceImpl implements AvisoService {
    
    @Autowired
    private AvisoAdopcionRepository avisoAdopcionRepository;

    @Override
    public List<Map<String, String>> fetchAdopcionsList() {
        List<AvisoAdopcion> avisos = avisoAdopcionRepository.findAll();
        List<Map<String, String>> avisosData = new ArrayList<>();

        for (AvisoAdopcion aviso : avisos) {
            Map<String, String> avisoData = new HashMap<>();
            avisoData.put("id", aviso.getId().toString());
            LocalDateTime fecha = aviso.getFechaIngreso();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");
            avisoData.put("fecha", fecha.format(formatter));
            avisoData.put("sector", (aviso.getSector()==null) ? null : aviso.getSector());
            String cant = aviso.getCantidad().toString();
            String tipo = aviso.getTipo().name();
            String edad = aviso.getEdad().toString();
            String um = aviso.getUnidadMedida().name();
            if (um=="m") {
                um ="meses";
            }
            else {
                um = "años";
            }
            avisoData.put("cantTipoEdadUm", cant+" "+tipo+", "+edad+" "+um);
            avisoData.put("comuna", aviso.getComuna().getNombre());

            avisosData.add(avisoData);
        }
        return avisosData;
    }
}
