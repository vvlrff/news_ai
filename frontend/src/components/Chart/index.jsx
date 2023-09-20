import { Sunburst } from 'react-sunburst-chart';

const data = {
    name: 'root',
    children: [
        {
            name: 'A',
            children: [
                { name: 'A1', size: 1 },
                { name: 'A2', size: 2 },
            ],
        },
        {
            name: 'B',
            children: [
                { name: 'B1', size: 3 },
                { name: 'B2', size: 4 },
            ],
        },
    ],
};

const SunburstChart = () => {
    return (
        <div style={{ width: '500px', height: '500px' }}>
            <Sunburst
                data={data}
                scale="linear"
                tooltipContent={({ e }) => e.value}
                onClick={(e) => console.log(e)}
            />
        </div>
    );
};

export default SunburstChart;