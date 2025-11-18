package com.tareas.tarea4.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.tareas.tarea4.service.AvisoService;

@Controller
public class AppController {
    
    @Autowired
    private AvisoService avisoService;

    @GetMapping("/")
    public String indexRoute(Model model) {
        List<Map<String, String>> modelData = avisoService.fetchAdopcionsList();
        model.addAttribute("data", modelData);
        return "avisosCalificados";
    }
    
}
