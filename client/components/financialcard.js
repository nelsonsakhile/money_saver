

const FinCard = () => {
  return(
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
    )
}

export default FinCard;