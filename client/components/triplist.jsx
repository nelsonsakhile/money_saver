
const TripList = () => {
  return (
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
    )
};

export default TripCard