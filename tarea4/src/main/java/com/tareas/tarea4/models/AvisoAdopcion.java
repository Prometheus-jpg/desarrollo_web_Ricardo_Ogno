package com.tareas.tarea4.models;

import java.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table
public class AvisoAdopcion {
    
    @Id
    @SequenceGenerator(
        name = "aviso_sequence",
        sequenceName = "aviso_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "aviso_sequence"
    )
    private Integer id;

    @NotNull
    private LocalDateTime fecha_ingreso;

    @ManyToOne
    @JoinColumn(name="comuna_id")
    @NotNull
    private Comuna comuna;

    @NotNull
    private String email;
    
    @Enumerated(EnumType.STRING)
    @NotNull
    private Tipo tipo;

    public enum Tipo { gato, perro };

    @NotNull
    private Integer cantidad;

    @NotNull
    private Integer edad;

    @Enumerated(EnumType.STRING)
    @NotNull
    private UnidadMedida unidad_medida;

    public enum UnidadMedida { a, m };

    @NotNull
    private LocalDateTime fecha_entrega;


    private String sector;
    @SuppressWarnings("unused")
    private String celular;
    @SuppressWarnings("unused")
    private String descripcion;

    public Integer getId(){
        return id;
    }
    public LocalDateTime getFechaIngreso(){
        return fecha_ingreso;
    }
    public Comuna getComuna(){
        return comuna;
    }
    public String getEmail(){
        return email;
    }
    public Tipo getTipo(){
        return tipo;
    }
    public Integer getCantidad(){
        return cantidad;
    }
    public Integer getEdad(){
        return edad;
    }
    public UnidadMedida getUnidadMedida(){
        return unidad_medida;
    }
    public String getSector(){
        return sector;
    }
    


}
