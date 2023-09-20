// Check full tutorial: https://dev.to/andrewchmr/react-d3-sunburst-chart-3cpd

import { useState, useEffect, useRef } from "react";
import * as d3 from "d3";
import oldData from "./data.json";

const SIZE = 975;
const RADIUS = SIZE / 2;


export const SunburstChart = ({ data }) => {
    const svgRef = useRef(null);
    const [viewBox, setViewBox] = useState("0,0,0,0");

    const partition = (data) =>
        d3.partition().size([2 * Math.PI, RADIUS])(
            d3
                .hierarchy(data)
                .sum((d) => d.value)
                .sort((a, b) => b.value - a.value)
        );

    const color = d3.scaleOrdinal(
        d3.quantize(d3.interpolateRainbow, Object.keys(data).length + 1)
    );

    const format = d3.format(",d");

    const arc = d3
        .arc()
        .startAngle((d) => d.x0)
        .endAngle((d) => d.x1)
        .padAngle((d) => Math.min((d.x1 - d.x0) / 2, 0.005))
        .padRadius(RADIUS / 2)
        .innerRadius((d) => d.y0)
        .outerRadius((d) => d.y1 - 1);

    const getAutoBox = () => {
        if (!svgRef.current) {
            return "";
        }

        const { x, y, width, height } = svgRef.current.getBBox();

        return [x, y, width, height].toString();
    };

    useEffect(() => {
        setViewBox(getAutoBox());
    }, []);

    const getColor = (d) => {
        while (d.depth > 1) d = d.parent;
        return color(d.data.name);
    };

    const getTextTransform = (d) => {
        const x = (((d.x0 + d.x1) / 2) * 180) / Math.PI;
        const y = (d.y0 + d.y1) / 2;
        return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
    };


    const root = partition(data);

    console.log(root)

    console.log(Object.keys(root.data))
    console.log(Object.entries(data))

    return (
        <svg width={SIZE} height={SIZE} viewBox={viewBox} ref={svgRef}>
            <g fillOpacity={0.6}>
                {Object.entries(root)
                    .map(([key, value]) => (
                        <path key={key} d={arc(value)}>
                            {console.log(key, value)}
                            <text>
                                {value}
                            </text>
                        </path>
                    ))}
            </g>
            <g
                pointerEvents="none"
                textAnchor="middle"
                fontSize={10}
                fontFamily="sans-serif"
            >
            </g>
        </svg>
    );
};
