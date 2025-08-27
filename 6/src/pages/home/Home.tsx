// No Home.tsx
interface HomeProps {
  count: number;
}

const Home: React.FC<HomeProps> = ({ count }) => {
  return (
    <div>
      <h2>Componente Home</h2>
      <p>Contador no Home: {count}</p>
    </div>
  );
}

export default Home;
