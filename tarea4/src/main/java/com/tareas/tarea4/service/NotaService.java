package com.tareas.tarea4.service;

import java.util.Map;

import com.tareas.tarea4.models.Nota;

public interface NotaService {
    Map<String, String> getNota(String idAviso);
    Nota updateNota(Nota nota, String idAviso) throws Exception;
}
