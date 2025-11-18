package com.tareas.tarea4.controller;


import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.tareas.tarea4.models.Nota;
import com.tareas.tarea4.service.NotaService;


@RestController
public class ApiController {

    @Autowired
    private NotaService notaService;

    @PutMapping("/notas/{id}")
    public Nota updateNota(@RequestBody Nota nota, @PathVariable("id") String id) throws Exception{
        try {
            return notaService.updateNota(nota, id);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return nota;
        }
    }

    @GetMapping("/nota/{id}")
    public Map<String, String> getNota(@PathVariable("id") String idAviso) {
        return notaService.getNota(idAviso);
    }
    
}
