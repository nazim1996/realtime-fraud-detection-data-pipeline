from simulator.transaction_simulator import transaction_stream
from predictor.fraud_predictor import predict_transaction

for transaction in transaction_stream():
    result = predict_transaction(transaction)
    print("Transaction processed:", result)