from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage
affiliates = {}
donations = []

@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    amount = data.get('amount', 1222)
    affiliate_id = data.get('affiliate_id', None)

    # Calculate splits
    affiliate_cut = amount * 0.90
    kingdom_cut = amount * 0.09
    creator_cut = amount * 0.01

    # Record donation
    donations.append({
        "amount": amount,
        "affiliate_id": affiliate_id,
        "split": {"affiliate": affiliate_cut, "kingdom": kingdom_cut, "creator": creator_cut}
    })

    if affiliate_id:
        affiliates[affiliate_id] = affiliates.get(affiliate_id, 0) + affiliate_cut

    return jsonify({
        "status": "success",
        "affiliate_cut": affiliate_cut,
        "kingdom_cut": kingdom_cut,
        "creator_cut": creator_cut
    })

if __name__ == '__main__':
    app.run(debug=True)
