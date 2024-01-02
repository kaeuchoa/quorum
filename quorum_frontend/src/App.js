import { ChakraProvider } from '@chakra-ui/react'
import MainLayout from './layout/MainLayout';

function App() {
  return (
    <ChakraProvider>
      <div className="App">
        <MainLayout />
      </div>
    </ChakraProvider>

  );
}

export default App;
