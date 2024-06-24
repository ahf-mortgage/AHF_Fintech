import React, { useState } from 'react';


const Header = (props) => {
  const [sortColumn, setSortColumn] = useState(null);

  const columns = [
    { label: 'Name', key: 'name' },
    { label: 'Age', key: 'age' },
    { label: 'Email', key: 'email' },
  ];

  const handleSort = (column) => {
    const direction = sortColumn && sortColumn.key === column.key ? (sortColumn.direction === 'asc' ? 'desc' : 'asc') : 'asc';
    setSortColumn({ key: column.key, direction });
  };

  return (
    <div>
        <p>Hello world</p>
    </div>
  
  );
};

export default Header;