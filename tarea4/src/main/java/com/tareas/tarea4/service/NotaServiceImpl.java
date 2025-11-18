package com.tareas.tarea4.service;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.tareas.tarea4.models.Nota;
import com.tareas.tarea4.repository.NotaRepository;

@Service
public class NotaServiceImpl implements NotaService {

    @Autowired
    private NotaRepository notaRepository;

    @Override
    public Map<String,String> getNota(String idAviso) {
        Optional<Nota> nota = notaRepository.findByAviso_id(Integer.parseInt(idAviso));
        Map<String, String> notaData = new HashMap<>();
        notaData.put("idAviso", idAviso);
        notaData.put("nota", (nota.isPresent()) ? nota.get().getNota().toString() : "-");
        
        return notaData;
    }

    @Override
    public Nota updateNota(Nota nota, String idAviso) throws Exception{
        Optional<Nota> notaDB = notaRepository.findByAviso_id(Integer.parseInt(idAviso));
        
        if (nota.validateNota()) {    
            if (notaDB.isPresent()) {
                Integer newNota = (Integer) (nota.getNota()+notaDB.get().getNota())/2;
                notaDB.get().setNota(newNota);
                System.out.println("nota actualizada");
                return notaRepository.save(notaDB.get());
            }
            else {
                System.out.println("nota guardada");
                return notaRepository.save(nota);
            }
        }
        else {
            throw new IllegalArgumentException("nota invalidada");
        }
    }
    
}
