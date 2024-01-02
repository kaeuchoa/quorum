import { useMediaQuery } from '@chakra-ui/media-query'

const useCustomBreakpoints = () => {
  const [maxWidthQuery] = useMediaQuery('(max-width: 576px)')
  
  return {
    isMobileView: maxWidthQuery
  }
}

export default useCustomBreakpoints