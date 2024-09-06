
import { Button, Popover } from "flowbite-react";
import {useRoutes } from "react-router-dom";

export function MloDetailPopover({showMloInfo}) {
 
  setTimeout(() => {
    window.location.href = '/graph';
  },100)
  return (
    <Popover
      aria-labelledby="default-popover"
      content={
        <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
          <div className="border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700">
            <h3 id="default-popover" className="font-semibold text-gray-900 dark:text-white">Popover title</h3>
          </div>
          <div className="px-3 py-2">
            <p>And here's some amazing content. It's very engaging. Right?</p>
          </div>
        </div>
      }
    >
      <Button>Default popover</Button>
    </Popover>
  );
}
