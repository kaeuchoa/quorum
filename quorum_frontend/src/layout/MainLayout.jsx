import Sidebar from "../core/Sidebar/Sidebar";
import useCustomBreakpoints from "../hooks/useCustomBreakpoints";

const MainLayout = () => {
  const { isMobileView } = useCustomBreakpoints();
  return <>{isMobileView ? <Sidebar /> : <Sidebar.Large />}</>;
};

export default MainLayout;
