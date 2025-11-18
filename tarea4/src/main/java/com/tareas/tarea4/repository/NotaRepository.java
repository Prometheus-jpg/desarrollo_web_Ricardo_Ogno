package com.tareas.tarea4.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.tareas.tarea4.models.Nota;

@Repository
public interface NotaRepository extends JpaRepository<Nota, Integer> {
    Optional<Nota> findByAviso_id(Integer id);
} 
