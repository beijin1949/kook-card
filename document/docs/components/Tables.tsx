import React from 'react';

interface TableProps {
    rowData: any[][];
}

const Table: React.FC<TableProps> = ({rowData}) => {
    return (
        <table className="d-table" cellPadding={0} cellSpacing={0}>
            <colgroup>
                <col style={{minWidth: '120px'}}/>
            </colgroup>
            <thead>
            <tr>
                <th style={{borderTopLeftRadius:'8px'}}>参数名</th>
                <th>类型</th>
                <th>是否必填</th>
                <th>默认值</th>
                <th style={{borderTopRightRadius:'8px'}}>说明</th>
            </tr>
            </thead>
            <tbody>
            {rowData.map((row, rowIndex) => (
                <tr key={rowIndex}>
                    {row.map((cell, cellIndex) => (
                        <td key={cellIndex}>
                            {cell}
                        </td>
                    ))}
                </tr>
            ))}
            </tbody>
        </table>
    );
};

export default Table;
