import {
  Drawer,
  DrawerBody,
  DrawerFooter,
  DrawerHeader,
  DrawerContent,
  Button,
  DrawerOverlay,
  DrawerCloseButton,
} from "@chakra-ui/react";
import { useDisclosure } from '@chakra-ui/react-use-disclosure';
import { useRef } from 'react';

const Sidebar = () => {
  const { isOpen, onOpen, onClose } = useDisclosure()
  const btnRef = useRef()

  return (
    <>
      <Button ref={btnRef} onClick={onOpen}>
        Menu
      </Button>
      <Drawer
        isOpen={isOpen}
        placement='left'
        onClose={onClose}
        finalFocusRef={btnRef}
      >
        <DrawerOverlay />
        <DrawerContent>
          <DrawerCloseButton />
          <DrawerHeader>Mobile Quorum</DrawerHeader>

          <DrawerBody>

          </DrawerBody>

          <DrawerFooter>
          </DrawerFooter>
        </DrawerContent>
      </Drawer>
    </>
  )
};

Sidebar.Large = function SidebarLarge() {
  return (
    <Drawer placement="left" isOpen>
      <DrawerContent>
        <DrawerHeader>Large Quorum</DrawerHeader>

        <DrawerBody></DrawerBody>

        <DrawerFooter></DrawerFooter>
      </DrawerContent>
    </Drawer>
  )
}

export default Sidebar