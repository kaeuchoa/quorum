import DetailView from "../core/DetailView/DetailView";
import Sidebar from "../core/Sidebar/Sidebar";
import useCustomBreakpoints from "../hooks/useCustomBreakpoints";

const MainLayout = () => {
  const { isMobileView } = useCustomBreakpoints();
  return (
    <>
      <nav>{isMobileView ? <Sidebar /> : <Sidebar.Large />}</nav>
      <main>
        {isMobileView ? (
          <DetailView heading="Menu Option">everything else</DetailView>
        ) : (
          <DetailView.Large heading="Menu Option">everything else</DetailView.Large>
        )}
      </main>
    </>
  );
};

export default MainLayout;
