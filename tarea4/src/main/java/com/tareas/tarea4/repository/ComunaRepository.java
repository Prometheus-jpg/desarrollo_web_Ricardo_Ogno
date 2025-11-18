package com.tareas.tarea4.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.tareas.tarea4.models.Comuna;

@Repository
public interface ComunaRepository extends JpaRepository<Comuna, Integer> {
   
}
