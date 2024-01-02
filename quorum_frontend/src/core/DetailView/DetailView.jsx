import { Box, Heading } from "@chakra-ui/layout";

const DetailView = ({ heading, children }) => {
  return (
    <Box margin={4}>
      <Heading as="h1">{heading}</Heading>
      {children}
    </Box>
  );
};

DetailView.Large = function DetailViewLarge({ heading, children }) {
  return (
    <Box paddingStart={320} margin={4}>
      <Heading as="h1">{heading}</Heading>
      {children}
    </Box>
  );
}

export default DetailView;
