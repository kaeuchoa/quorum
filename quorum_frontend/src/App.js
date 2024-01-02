import { ChakraProvider } from '@chakra-ui/react'
import MainLayout from './layout/MainLayout';

function App() {
  return (
    <ChakraProvider>
      <main className="App">
        <MainLayout />
      </main>
    </ChakraProvider>

  );
}

export default App;
