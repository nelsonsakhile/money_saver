import React, { useState } from 'react';
import { View, FlatList, Text, StyleSheet } from 'react-native';
import { Card, Title, Paragraph } from 'react-native-paper';


const Home = () => {
  const [trips, setTrips] = useState([
    { id: 1, destination: 'Bali', budget: 1000 },
    { id: 2, destination: 'Tokyo', budget: 2000 },
    { id: 3, destination: 'Paris', budget: 1500 },
    { id: 4, destination: 'Rome', budget: 1200 },
    // ...more trips
  ]);

  const [financialData, setFinancialData] = useState({
    income: 5000,
    spending: 2500,
    savings: 2500,
  });

  return (
    <View style={styles.container}>
      <View style={styles.financialOverview}>
        <Card style={styles.financialCard}>
          <Card.Title title="Income" />
          <Card.Content>
            <Paragraph>${financialData.income}</Paragraph>
          </Card.Content>
        </Card>
        <Card style={styles.financialCard}>
          <Card.Title title="Spending" />
          <Card.Content>
            <Paragraph>${financialData.spending}</Paragraph>
          </Card.Content>
        </Card>
        <Card style={styles.financialCard}>
          <Card.Title title="Savings" />
          <Card.Content>
            <Paragraph>${financialData.savings}</Paragraph>
          </Card.Content>
        </Card>
      </View>
      <View style={styles.tripList}>
        <FlatList
          data={trips.slice(0, 4)} // Limit to 4 trips
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <Card style={styles.tripCard}>
              <Card.Title title={item.destination} />
              <Card.Content>
                <Paragraph>Budget: ${item.budget}</Paragraph>
              </Card.Content>
            </Card>
          )}
        />
      </View>
      
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f2f2f2',
  },
  financialOverview: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16, // Add margin to separate from trip list
  },
  financialCard: {
    flex: 1,
    margin: 8,
    backgroundColor: '#f0f0f0',
  },
  tripList: {
    flex: 1,
    backgroundColor: '#f2f2f2',
  },
  tripCard: {
    marginBottom: 16,
    backgroundColor: '#f0f0f0',
  },
});



export default Home;
