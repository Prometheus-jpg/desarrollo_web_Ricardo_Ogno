package com.tareas.tarea4.models;

import java.util.Objects;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table
public class Nota {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name="aviso_id")
    @NotNull
    private AvisoAdopcion aviso;

    @NotNull
    private Integer nota;

    public Nota() {
    }

    public Nota(AvisoAdopcion aviso, Integer nota){
        this.aviso = aviso;
        this.nota = nota;
    }

    public void setNota(Integer newNota) {
        this.nota = newNota;
    }
    
    public Integer getId() {
        return id;
    }
    
    public AvisoAdopcion getAviso() {
        return aviso;
    }
    
    public Integer getNota() {
        return nota;
    }

    public Boolean validateNota() {
        return (Objects.nonNull(nota) && nota>=1 && nota<=7); 
    }

}
