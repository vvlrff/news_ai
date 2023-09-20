import { PieChart, Pie, ResponsiveContainer, Tooltip } from "recharts";
import "./graph-master.css";

const PieGraph = ({ data }) => {
    const list = [];

    for (const key in data) {
        list.push({
            name: key,
            amount: data[key]["Общее количество"],
            fill:
                "#" +
                (((1 << 24) * Math.random()) | 0).toString(16).padStart(6, "0"),
        });
    }
    // console.log(list);
    // console.log(amount);
    const CustomTooltip = ({ payload, label, active }) => {
        if (active) {
            return (
                <div className="custom_tooltip">
                    <p className="desc">Категория: {payload[0].payload.name}</p>
                    <p className="label">{`Количество новостей: ${payload[0].value}`}</p>
                </div>
            );
        }

        return null;
    };

    // ! -----------------------------------------------------

    return (
        <>
            <ResponsiveContainer width="100%" height="100%">
                <PieChart width={400} height={400}>
                    <Pie
                        dataKey="amount"
                        data={list}
                        fill="#8884d8"
                        label
                        // onClick={(e) => handleClick(e.payload.payload)}
                    />
                    <Tooltip content={<CustomTooltip />} />
                </PieChart>
            </ResponsiveContainer>
        </>
    );
};

export default PieGraph;
