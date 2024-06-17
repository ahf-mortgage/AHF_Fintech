"use client";
import { Button, Navbar } from "flowbite-react";

export function AHFNavbar() {
  return (
    <Navbar fluid rounded>
      <div className="flex md:order-2">
        <Navbar.Toggle />
      </div>
      <Navbar.Collapse>
        <Navbar.Link href="/abovebreakpoint" className="w-auto h-auto lg:text-nowrap">Above breakpoint</Navbar.Link>
        <Navbar.Link href="#" className="w-auto h-auto lg:text-nowrap">AHF Annual Cap </Navbar.Link>
        <Navbar.Link href="#" className="w-auto h-auto lg:text-nowrap">Gross Income </Navbar.Link>
        <Navbar.Link href="#" className="w-auto h-auto lg:text-nowrap">W2 Branch Yearly Gross Income </Navbar.Link>
        <Navbar.Link href="#" className="w-auto h-auto lg:text-nowrap">Revenue Share </Navbar.Link>
        <Navbar.Link href="#" className="w-auto h-auto lg:text-nowrap">Revenue share passive income examples 5X5 Example </Navbar.Link>
       
      </Navbar.Collapse>
    </Navbar>
  );
}
