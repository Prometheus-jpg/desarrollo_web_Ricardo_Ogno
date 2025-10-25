Highcharts.chart("avisosPorDia", {
  chart: {
    type: "line",
  },
  title: {
    text: "Numero de Avisos de Adopcion por dia",
  },
  xAxis: {
    type: "datetime",
    dateTimeLabelFormats: {
      day: "%b %e, %Y",
    },
    title: {
      text: "Dia",
    },
  },
  yAxis: {
    title: {
      text: "Numero de Avisos",
    },
  },
  legend: {
    align: "left",
    verticalAlign: "top",
    borderWidth: 0,
  },

  tooltip: {
    shared: true,
    crosshairs: true,
  },

  series: [
    {
      name: "Avisos",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#FC2865",
    },
  ],
});

Highcharts.chart('avisosPorTipo', {
	chart: {
		type: 'pie'
	},
	title: {
		text: 'Distribución de Avisos por Tipo de Animales'
	},
	series: [{
		name: 'Tipos de Animales',
		data: [],
		tooltip: {
			pointFormat: '<b>{point.name}</b>: {point.y}'
		}
	}],
	plotOptions: {
		pie: {
			allowPointSelect: true,
			cursor: 'pointer',
			dataLabels: {
				enabled: true,
				format: '<b>{point.name}</b>: {point.y}'
			}
		}
	}
});

Highcharts.chart('avisosPorTipoMes', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Cantidad de Tipso de animal cada mes'
    },
    xAxis: {
        categories: [],
        crosshair: true,
        accessibility: {
            description: 'Meses'
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Cantidad de avisos'
        }
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [
        {
            name: 'Perro',
            data: []
        },
        {
            name: 'Gato',
            data: []
        }
    ]
});



fetch(`${window.origin}/get-stats-data`)
  .then((response) => response.json())
  .then(([dataFechas, dataTipos, dataTiposMes]) => {
    let parsedDataCant = dataFechas.map((item) => {
      const [year, month, day] = item.date
        .split("-")
        .map((part) => parseInt(part, 10));
      return [
        Date.UTC(year, month - 1, day), // javascript month indices start from 0 !
        item.count,
      ];
    });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "avisosPorDia"
    );

		const chart2 = Highcharts.charts.find(
      (chart2) => chart2 && chart2.renderTo.id === "avisosPorTipo"
    );

    const chart3 = Highcharts.charts.find(
      (chart3) => chart3 && chart3.renderTo.id === "avisosPorTipoMes"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedDataCant,
        },
      ],
    });

		chart2.update({
      series: [
        {
          data: [
							{ name: 'Perros', y: dataTipos[0].cant_p },
							{ name: 'Gatos', y: dataTipos[0].cant_g }
					],
        },
      ],
    });

    chart3.xAxis[0].setCategories(dataTiposMes[0].meses);
    chart3.series[0].setData(dataTiposMes[0].perros);
    chart3.series[1].setData(dataTiposMes[0].gatos);

  })
  .catch((error) => console.error("Error:", error));
